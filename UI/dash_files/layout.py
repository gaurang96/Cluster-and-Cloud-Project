import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import tabs


context = "provide a brief summary of this webapp here."

def get_title():
	return dbc.Row(
            [
                dbc.Col(
                    children = 
                    [
                        # Title
                        html.H1(children="Cluster and Cloud Computing Assignment 2", style = {'color': '#55ACEE'}),
                        # Subtitle
                        html.Div(children= "Inferences Into Twitter Sentiment About Unemployment in relation to the Covid-19 Crisis", style = {'color': '#292F33'})
                    ]
                )
            ],
            style = {'height' : "150px", 'background-color' : "#CCD6DD"}
        )

def get_sidePanel():
	return dbc.Col(
                    [
                        # Callback Input
                        dbc.Row(children = "click to get data from couchdb", style = {'color': '#292F33', 'padding-bottom': '10px', 'padding-left' : '10px'}),
                        dbc.Row(dbc.Button('Connect to Database', color='primary', id='t-val', n_clicks=0, block = True), style = {'padding-bottom': '10px', 'padding-left' : '10px', 'padding-right': '10px'}),
                        dbc.Row(html.Div(children = context, style = {'color': '#292F33', 'padding-bottom': '10px', 'padding-left' : '10px'}))

                    ],
                    width = 2,
                    style = {'background-color' : "#CCD6DD", "height" : "85vh"}
                )

def get_body():
	return dbc.Row([get_sidePanel(), tabs.get_tabs()], )


def get_layout():
	return dbc.Container(children = [get_title(), get_body()], fluid = True)

def get_stylesheet():
	return [dbc.themes.BOOTSTRAP]
