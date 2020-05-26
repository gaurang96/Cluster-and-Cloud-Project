import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

# tab formats
tab_styles = {'width' : "25vh"}
tab_offsets = {'padding-left' : '20px', 'padding-top': '20px'}
chart_style = {'height': "75vh", 'width': "125vh"}

# to return to layout body
def get_tabs():
	return dbc.Col(
		[
			dbc.Tabs(
			    [
			        dbc.Tab(get_tab1(), label="Positive Sentiment", tab_style = tab_styles),
			        dbc.Tab(get_tab2(), label="Negative Sentivement", tab_style = tab_styles),
			        dbc.Tab(get_tab3(), label="Recent Sentiment Trends", tab_style = tab_styles),
			        dbc.Tab(get_tab4(), label="Unemployment Rates", tab_style = tab_styles)
			    ]
		    )
    	], 
    	style = {'padding-left' : "15px", 'background-color' : '#E1E8ED'},
    	width = 10
    )

# composition of tab 1
def get_tab1():
	graph = dcc.Graph(id = 'positive-chart', style = chart_style)
	body  = dbc.Col([graph], style = tab_offsets)

	return body

# composition of tab 2
def get_tab2():
	graph = dcc.Graph(id = 'negative-chart', style = chart_style)
	body  = dbc.Col([graph], style = tab_offsets)

	return body

# composition of tab 3
def get_tab3():
	graph = dcc.Graph(id = 'trends-chart', style = chart_style)
	body  = dbc.Col([graph], style = tab_offsets)

	return body

# composition of tab 4
def get_tab4():
	graph = dcc.Graph(id = 'unemployment-chart', style =chart_style)
	body  = dbc.Col([graph], style = tab_offsets)

	return body
