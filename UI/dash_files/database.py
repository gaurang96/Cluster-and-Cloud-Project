import cloudant
import couchdb

class database:
	def __init__(self, ip, user, pw):
		self.ip = ip
		self.client = cloudant.client.Cloudant(user, pw, url="http://{}:{}@{}/".format(user, pw, self.ip))

	def connect(self):
		self.client.connect()
		print("client connected")

	def collect_view(self, db, view_name, doc_id ='_design/view', group = False, gl = 0, skip = 0):
		return (self.client[db].get_view_result(doc_id, view_name, raw_result=True,group=group, group_level=gl ,skip=skip))

	def disconnect(self):
		self.client.disconnect()

'''db = database('172.26.132.96:5984/', 'admin', '123')
db.connect()

out = db.collect_view('twitterdata', 'myview')
'''
