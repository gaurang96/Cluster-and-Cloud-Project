import json

#data from couch is requested here and used in the flask routes

def dump_data():
	return json.dumps("everything is a-ok")

