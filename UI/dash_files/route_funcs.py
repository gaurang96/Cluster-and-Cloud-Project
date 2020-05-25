import json

#data from couch is requested here and used in the flask routes
#any processing of the data can be done in these functions

def dump_aurin(database):
	view_data = database.collect_view('aurin', 'lg', doc_id = '_design/lg')

	j_data = view_data #perform any transformations needed beforehand
	return json.dumps(j_data)


def dump_twitter(database):
	view_data = database.collect_view('twitterdata', 'myview', group = True, gl = 2, skip = 100)
	j_data = {}
	# bins the keys into 0.1, 0.2,... 1
	# change to whatever necessary
	for v in view_data['rows']:
		binned_v = round(float(v['key'][0]),1)
		if binned_v not in j_data.keys():
			j_data[binned_v] = {'long' : [v['key'][1][0]], 'lat' : [v['key'][1][1]]}

		else:
			j_data[binned_v]['long'].append(v['key'][1][0])
			j_data[binned_v]['lat'].append(v['key'][1][1])

	return json.dumps(j_data)