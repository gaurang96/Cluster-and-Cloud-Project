import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import graphs
import dash_table
import os

# tab formats
tab_styles = {'width' : "25vh"}
tab_offsets = {'padding-left' : '20px', 'padding-top': '20px'}

# to return to layout body
def get_tabs():
	return dbc.Col(
		[
			dbc.Tabs(
			    [
			        dbc.Tab(get_tab1(), label="Positive Sentiment", tab_style = tab_styles),
			        dbc.Tab(get_tab2(), label="Negative Sentivement", tab_style = tab_styles),
			        dbc.Tab(get_tab3(), label="Cities by Negativity", tab_style = tab_styles),
			        dbc.Tab(get_tab4(), label="Unemployment Trends", tab_style = tab_styles)
			    ]
		    )
    	], 
    	style = {'padding-left' : "15px"},
    	width = 10
    )


# composition of tab 1
def get_tab1():
	body  = dbc.Col([
		dbc.Row(html.Div(id = 'header', children = ["this tab should return data that is from aurin"])),
		dbc.Row(get_table('aurin-table', ['idx', 'Year', 'Month', 'Value']))
		],
		style = tab_offsets
	)

	return body



# composition of tab 2
def get_tab2():
	graph = dcc.Graph(id = 'twitter_graph', style = {'height': "75vh", 'width': "100vh"})
	body = html.Div(children = ["Tweets Summary", html.Div(id = 'test', children = "data should be posted here"), graph], style = tab_offsets)
	return body



# composition of tab 3
def get_tab3():
	body = html.Div("Inferences", style = tab_offsets)
	return body



# composition of tab 4
def get_tab4():
	body = dbc.Col([
		dcc.Graph(id = "unemployment-chart", style = {'height': "75vh", 'width': "100vh"})],
		style = tab_offsets
		)

	return body



# Generic functions 
def get_table(tid, colnames):
	style_cell = {'height': 'auto', 'textAlign' : 'center'}
	style_table = {'width' : '800px', 'height': '400px', 'overflowY': 'auto', 'overflowX' : 'none'}
	t_cols = [{'name': i, 'id': i } for i in colnames]
	table = dash_table.DataTable(id = tid, columns = t_cols, style_table = style_table, style_cell = style_cell)
	return table