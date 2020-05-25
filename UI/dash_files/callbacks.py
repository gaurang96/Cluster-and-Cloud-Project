import dash
from dash.dependencies import Input, Output
import requests
import numpy as np

# callback for each interactive function
#requests are used to interact with the GET calls from the api

# Update Table
def table_callback(app, in_id, in_type, out_id, out_type):
	@app.callback(Output(out_id, out_type), [Input(in_id, in_type)])

	def update_table(n_clicks):
	    data = [{'idx' : 0, 'Year' : 0 , 'Month' : 0, 'Value' : 0}]
	    if n_clicks > 0:
	        data = [{i : n_clicks for i in ['idx', 'Year', 'Month', 'Value']}]

	    return data

# Update Graph
def unemp_callback(app, in_id, in_type, out_id):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		unemp = requests.get('http://127.0.0.1:8050/api/unemployment').json()
		data = [{'x' : list(unemp['city'].values()), 'y': list(unemp['unemployment_rate'].values()), 'type' : 'bar'}]
		layout = {'title': "Unemployment Rates"}

		return {'data': data, 'layout': layout}

def time_series(app, in_id, in_type, out_id):
	return None

# Update Graph
def twitter_graph(app, in_id, in_type, out_id,):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		if event > 0:
			d_json = requests.get("http://127.0.0.1:8050/api/twitter").json()

			data = [{'x' : d_json[d]['long'], 'y' : d_json[d]['lat'], 'mode': 'markers', 'name': d} for d in d_json]
		return {'data': data, 'layout':{'title': "Twitter Data Graph"}}

