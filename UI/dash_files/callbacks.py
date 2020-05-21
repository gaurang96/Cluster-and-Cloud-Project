import dash
from dash.dependencies import Input, Output


def reg_table_callback(app):
	@app.callback(Output('aurin-table', 'data'),[Input('go-val', 'n_clicks')])

	def update_table(n_clicks):
	    data = [{'idx' : 0, 'Year' : 0 , 'Month' : 0, 'Value' : 0}]
	    if n_clicks > 0:
	        data = [{i : n_clicks for i in ['idx', 'Year', 'Month', 'Value']}]

	    return data
