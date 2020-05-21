import flask
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import couchdb
from cloudant.client import Cloudant
from cloudant import design_document
import cloudant

'''serviceUsername = "user"
servicePassword = "123"
serviceURL = "http://user:123@172.26.132.80:5984/"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()'''

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
# accesses values from the couch db
'''def get_aurin_data():
    rows = []
    r_dict = {}
    aurinView = cloudant.view.View(cloudant.design_document.DesignDocument(client['aurin'], document_id='view'), 'myview')
    
    # purely gets values only from this section of the view
    for doc in aurinView.result:
        if doc['key'] == 'djsb_salm_smoothed_unemployment_lga_2010_18.24600':
            r_dict = doc['value']['props']

    r_dict.pop('lga_code18', None)
    r_dict.pop('lga_name18', None)
    l_dicts = []
    for key in r_dict.keys():
        kd = {'idx': key, 'Year': int(key[4:]), 'Month': key[:3], 'Value' : r_dict[key]}
        l_dicts.append(kd)
    
    return l_dicts'''

# Callbacks

# create a button that will collect and display data from couch db when clicked
# output 'collected data' as table
# input "go-click" as button_click
@app.callback(
    Output('aurin-table', 'data'),
    [Input( 'go-val', 'n_clicks')])

def get_data(n_clicks):
    data = [{'idx' : 0, 'Year' : 0 , 'Month' : 0, 'Value' : 0}]
    if n_clicks > 0:
        data = [{'idx' : 1, 'Year' : 1 , 'Month' : 1, 'Value' : 1}]

    return data


#layout atts

style_cell = {'height': 'auto', 'textAlign' : 'center'}
style_table = {'width' : '800px', 'height': '400px', 'overflowY': 'auto', 'overflowX' : 'none'}
t_cols = [{'name': i, 'id': i } for i in ['idx', 'Year', 'Month', 'Value']]
t_data = [{'idx' : 0, 'Year' : 0 , 'Month' : 0, 'Value' : 0}]

# app layout

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
                        html.Div(children = "Table will show the "),

                        # Callback Output
                        dash_table.DataTable(id = 'aurin-table', columns = t_cols,  data = t_data, style_table = style_table, style_cell = style_cell)
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