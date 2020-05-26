import dash
from dash.dependencies import Input, Output
import requests

# callback for each interactive function
#requests are used to interact with the GET calls from the api

# these need to replicate that of the server
host ='127.0.0.1'
port = '8050' 

# Update Graph
def unemp_callback(app, in_id, in_type, out_id):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Unemployment Rates", 'xaxis': {'title': 'Victoiran LGAs'}, 'yaxis': {'title': 'Unemployment Rate (%)'}, 
				  'paper_bgcolor' : 'rgba(0,0,0,0)', 'plot_bgcolor' : 'rgba(0,0,0,0)'}

		if event > 0:
			unemp = requests.get('http://{}:{}/api/unemployment'.format(host, port)).json()
			data = [{'x' : list(unemp['city'].values()), 'y': list(unemp['unemployment_rate'].values()),
					 'type' : 'bar', 'marker' : {'color': '#55ACEE'}}]
			
		return {'data': data, 'layout': layout}

def trend_callback(app, in_id, in_type, out_id):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Change in Happiness Index", 'xaxis': {'title': 'Days from Today', 'autorange': 'reversed'}, 'yaxis': {'title': 'Positve Tweets Difference'},
				  'paper_bgcolor' : 'rgba(0,0,0,0)', 'plot_bgcolor' : 'rgba(0,0,0,0)'}
		
		if event > 0:
			trends = requests.get('http://{}:{}/api/trend'.format(host, port)).json()
			data = [{'x' : ["{}".format(len(trends['positive_neutral_negative'])-i) for i in range(0, len(trends['positive_neutral_negative']) + 1)],
					 'y': list(trends['positive_neutral_negative'].values()),
					 'type' : 'line', 'marker' : {'color': '#55ACEE'}}]	

		return {'data': data, 'layout': layout}

def positive_callback(app, in_id, in_type, out_id, x = 25):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Suburbs with the Most Positive Sentiments", 'xaxis': {'title': 'Cities and Suburbs'}, 'yaxis': {'title': 'Sentiment Ratio'},
				  'paper_bgcolor' : 'rgba(0,0,0,0)', 'plot_bgcolor' : 'rgba(0,0,0,0)'}

		if event > 0:
			pos = requests.get('http://{}:{}/api/positive'.format(host, port)).json()
			data = [{'x' : list(pos['city'].values())[:x], 'y': list(pos['positve_ratio'].values())[:x], 'text': list(pos['total'].values())[:x],
					 'type' : 'bar', 'name': 'Positive Sentiment', 'marker': {'color': '#96c9b5'}},
					{'x' : list(pos['city'].values())[:x], 'y': list(pos['negative_ratio'].values())[:x], 'text': list(pos['total'].values())[:x],
					 'type' : 'bar', 'name': 'Negative Sentiment', 'marker': {'color': '#e76767'}}]

		return {'data': data, 'layout': layout}


def negative_callback(app, in_id, in_type, out_id, x = 25):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Suburbs with the Most Negative Sentiments", 'xaxis': {'title': 'Cities and Suburbs'}, 'yaxis': {'title': 'Sentiment Ratio'}, 
				  'paper_bgcolor' : 'rgba(0,0,0,0)', 'plot_bgcolor' : 'rgba(0,0,0,0)'}

		if event > 0:
			neg = requests.get('http://{}:{}/api/negative'.format(host, port)).json()
			data = [{'x' : list(neg['city'].values())[:x], 'y': list(neg['negative_ratio'].values())[:x], 'text': list(neg['total'].values())[:x],
					 'type' : 'bar', 'name' : 'Negative Sentiment', 'marker': {'color': '#e76767'}},
					{'x' : list(neg['city'].values())[:x], 'y': list(neg['positve_ratio'].values())[:x], 'text': list(neg['total'].values())[:x], 
					 'type' : 'bar', 'name': 'Positive Sentiment', 'marker': {'color': '#96c9b5'}}]

		return {'data': data, 'layout': layout}


