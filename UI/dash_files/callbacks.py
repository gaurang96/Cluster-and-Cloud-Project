import dash
from dash.dependencies import Input, Output
import requests

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
def graph_callback(app, in_id, in_type, out_id, out_type):
	@app.callback(Output(out_id, out_type), [Input(in_id, in_type)])
	def graph_update(event):
		pass

def test_callback(app):
	@app.callback(Output('test', 'children'), [Input('go-val', 'n_clicks')])
	def test(n_clicks):
		if n_clicks > 0:
			return requests.get("http://127.0.0.1:8050/api/test_data").json()
