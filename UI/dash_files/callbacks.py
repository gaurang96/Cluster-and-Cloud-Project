import dash
from dash.dependencies import Input, Output
import requests
import numpy as np

# callback for each interactive function
#requests are used to interact with the GET calls from the api

# Update Graph
def unemp_callback(app, in_id, in_type, out_id):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Unemployment Rates", 'xaxis': {'title': 'Victoiran LGAs'}, 'yaxis': {'title', 'Unemployment Rate (%)'}}

		if event > 0:
			unemp = requests.get('http://127.0.0.1:8050/api/unemployment').json()
			data = [{'x' : list(unemp['city'].values()), 'y': list(unemp['unemployment_rate'].values()), 'type' : 'bar'}]
			

		return {'data': data, 'layout': layout}

def trend_callback(app, in_id, in_type, out_id):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Historic Trend Line"}
		
		if event > 0:
			trends = requests.get('http://127.0.0.1:8050/api/trend').json()
			data = [{'x' : list(trends['positive_neutral_negative'].keys()), 'y': list(trends['positive_neutral_negative'].values()), 'type' : 'line'}]
			

		return {'data': data, 'layout': layout}

def positive_callback(app, in_id, in_type, out_id, x = 25):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Suburbs with the Most Positive Sentiments", 'xaxis_title': 'Suburbs and Cities of Victoria', 'yaxis_title': 'Twitter Sentiment Ratio'}

		if event > 0:
			pos = requests.get('http://127.0.0.1:8050/api/positive').json()
			data = [{'x' : list(pos['city'].values())[:x], 'y': list(pos['positve_ratio'].values())[:x], 'text': list(pos['total'].values())[:x],
					 'type' : 'bar', 'name': 'Positive Sentiment', 'marker': {'color': '#96c9b5'}},
					{'x' : list(pos['city'].values())[:x], 'y': list(pos['negative_ratio'].values())[:x], 'text': list(pos['total'].values())[:x],
					 'type' : 'bar', 'name': 'Negative Sentiment', 'marker': {'color': '#e76767'}}]

		return {'data': data, 'layout': layout}


def negative_callback(app, in_id, in_type, out_id, x = 25):
	@app.callback(Output(out_id, 'figure'), [Input(in_id, in_type)])
	def graph_update(event):
		data = [{'x': [], 'y' : []}]
		layout = {'title': "Suburbs with the Most Negatve Sentiments", 'xaxis_title': 'Suburbs and Cities of Victoria', 'yaxis_title': 'Twitter Sentiment Ratio'}

		if event > 0:
			neg = requests.get('http://127.0.0.1:8050/api/negative').json()
			data = [{'x' : list(neg['city'].values())[:x], 'y': list(neg['negative_ratio'].values())[:x], 'text': list(neg['total'].values())[:x],
					 'type' : 'bar', 'name' : 'Negative Sentiment', 'marker': {'color': '#e76767'}},
					{'x' : list(neg['city'].values())[:x], 'y': list(neg['positve_ratio'].values())[:x], 'text': list(neg['total'].values())[:x], 
					 'type' : 'bar', 'name': 'Positive Sentiment', 'marker': {'color': '#96c9b5'}}]

		return {'data': data, 'layout': layout}


