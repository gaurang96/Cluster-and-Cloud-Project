import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import tabs


context = "This Application provides a series of visualisations that help encapsulate the relationship of Unemployment in Victoria and Twitter Sentiment within the context of Covid-19."
github = "The code for this assignment can be found at:"
link = html.A(href = "https://github.com/gaurang96/Cluster-and-Cloud-Project" , children = "https://github.com/gaurang96/Cluster-and-Cloud-Project", style = {'color': '#FFFFFF'})

def get_title():
	return dbc.Row(
            [
                dbc.Col(
                    children = 
                    [
                        # Title
                        html.H1(children="Cluster and Cloud Computing Assignment 2", style = {'color': '#55ACEE', 'font-weight' :'bold'}),
                        # Subtitle
                        html.H4(children= "Inferences Into Twitter Sentiment About Unemployment in relation to the Covid-19 Crisis", style = {'color': '#CCD6DD'})
                    ],
                    style = {'padding-top': '25px', 'padding-left' : '10px'}
                )
            ],
            style = {'height' : "150px", 'background-color' : "#292F33"}
        )

def get_sidePanel():
	return dbc.Col(
                    [
                        # Callback Input
                        dbc.Row(children = "Click to get data from couchdb.", style = {'color': '#CCD6DD', 'padding-bottom': '10px', 'padding-left' : '10px', 'padding-top': '50px'}),
                        dbc.Row(dbc.Button('Connect to Database', color='primary', id='t-val', n_clicks=0, block = True), style = {'padding-bottom': '50px', 'padding-left' : '10px', 'padding-right': '10px'}),
                        dbc.Row(html.Div(children = context, style = {'color': '#CCD6DD', 'padding-bottom': '50px', 'padding-left' : '10px', 'padding-right': '10px'})),
                        dbc.Row(html.Div(children = github, style = {'color': '#CCD6DD', 'padding-left' : '10px', 'padding-right': '10px'})),
                        dbc.Row(html.Div(children = link, style = {'padding-left' : '10px', 'padding-right': '10px'}))


                    ],
                    width = 2,
                    style = {'background-color' : "#292F33", "height" : "85vh"}
                )

def get_body():
	return dbc.Row([get_sidePanel(), tabs.get_tabs()], )


def get_layout():
	return dbc.Container(children = [get_title(), get_body()], fluid = True)

def get_stylesheet():
	return [dbc.themes.BOOTSTRAP]
