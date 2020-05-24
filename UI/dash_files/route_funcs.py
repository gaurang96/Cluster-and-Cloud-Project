import json

#data from couch is requested here and used in the flask routes

def dump_data():
	return json.dumps("everything is a-ok")


def dump_aurin(database):
	database.connect()
	view_data = database.collect_view('aurin', 'view_1')

	j_data = view_data #perform any transformations needed beforehand
	return json.dumps(j_data)

def dump_twitter(database):
	database.connect()
	view_data = database.collect_view('twitter', 'view_1')

	j_data = view_data #perform any transformations needed beforehand
	return json.dumps(j_data)