import cloudant
import couchdb

class database:
	def __init__(self, ip, user, pw):
		self.ip = ip
		self.client = cloudant.client.Cloudant(user, pw, url="http://{}:{}@{}/".format(user, pw, self.ip))

	def connect(self):
		self.client.connect()
		print("client connected")

	def collect_view(self, db, view_name, doc_id ='view'):
		return cloudant.view.View(cloudant.design_document.DesignDocument(self.client[db], document_id=doc_id), view_name)

	def disconnect(self):
		self.client.disconnect()



db = database('172.26.134.13:5984', 'admin', '123')
db.connect()
