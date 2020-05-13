import flask
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import couchdb

full_db = couchdb.Server("http://user:123@172.26.132.80:5984/")
sample = full_db['jacks-db']
server = flask.Flask(__name__)

@server.route('/')
def index():
    return 'Hello Flask app'

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

# App Functions 
# accesses n values from the couch db
def get_couch_data(n_rows):
    rows = []
    for key in range(0, n_rows):
        row = html.Tr([html.Td(key), html.Td(sample[str(key)]['vals'])])
        rows.append(row)

    return rows

# Callbacks

# create a button that will collect and display data from couch db when clicked
# output 'collected data' as table
# input "go-click" as button_click
@app.callback(
    Output('couch-table', 'children'),
    [Input( 'go-val', 'n_clicks')])

def get_data(n_clicks):
    if n_clicks > 0:
        table_body = [html.Tbody(get_couch_data(20))]
        table_header = [html.Thead(html.Tr([html.Th("Key"), html.Th("Value")]))]

    return table_header + table_body


app.layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    children = 
                    [
                        # Title
                        html.H1(children='This is a sample display'),
                        # Subtitle
                        html.Div(children= "Dash: A web application framework for Python")
                    ]
                )
            ]
        ),

        dbc.Row(

            [
                dbc.Col(
                    [
                        # Callback Input
                        html.Div(children = "click 'go' to get the data from couchdb"),
                        html.Button('Go', id='go-val', n_clicks=0),

                    ],
                    width = 3
                ),

                dbc.Col(
                    [   
                        html.Div(children = "this is the visualisation column"),
                        html.Div(children = "this is a table"),
                        html.Div(children = ""),
                        html.Div(children = ""),
                        # Callback Output
                        dbc.Table(id = 'couch-table', bordered=True),
                    ],
                    width = 9
                ) 

            ]
        )
    ]
)

# deploy
if __name__ == '__main__':
    app.run_server(debug=True)