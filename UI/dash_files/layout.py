import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import tabs


def get_table(tid):
	style_cell = {'height': 'auto', 'textAlign' : 'center'}
	style_table = {'width' : '800px', 'height': '400px', 'overflowY': 'auto', 'overflowX' : 'none'}
	t_cols = [{'name': i, 'id': i } for i in ['idx', 'Year', 'Month', 'Value']]
	t_data = [{'idx' : 0, 'Year' : 0 , 'Month' : 0, 'Value' : 0}]

	table = dash_table.DataTable(id = tid, columns = t_cols,  data = t_data, style_table = style_table, style_cell = style_cell)
	return table

def get_title():
	return dbc.Row(
            [
                dbc.Col(
                    children = 
                    [
                        # Title
                        html.H1(children="Cluster and Cloud Computing Assignment 2", style = {'color': '#55ACEE'}),
                        # Subtitle
                        html.Div(children= "Inferences Into Twitter Sentiment About Unemployment Caused by the Covid-19 Crisis", style = {'color': '#292F33'})
                    ]
                )
            ],
            style = {'height' : "150px", 'background-color' : "#CCD6DD"}
        )

def get_sidePanel():
	return dbc.Col(
                    [
                        # Callback Input
                        html.Div(children = "click 'go' to get the data from couchdb", style = {'color': '#292F33'}),
                        html.Button('Go', id='go-val', n_clicks=0),
                        html.Div(children = "this column may also be used for short explanations.", style = {'color': '#292F33'})

                    ],
                    width = 2,
                    style = {'background-color' : "#CCD6DD", "height" : "85vh"}
                )

def get_mainPanel():
	return dbc.Col(
                    [   
                        html.Div(children = "this is the visualisation column", style = {'color': '#292F33'}),
                        html.Div(children = "Table will show the view", style = {'color': '#292F33'}),

                        # Callback Output
                        get_table('aurin-table')
                    ],
                    width = 10
                )

def get_body():
	return dbc.Row([get_sidePanel(), tabs.get_tabs()], )


def get_layout():
	return dbc.Container(children = [get_title(), get_body()], fluid = True)

def get_stylesheet():
	return [dbc.themes.BOOTSTRAP]