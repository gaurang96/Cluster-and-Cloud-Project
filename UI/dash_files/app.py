import flask
import dash
import layout
import callbacks
import route_funcs
import database

# data stores
ip = ""
user = ""
pw = ""
#db = database.database(ip, user, pw)

# app and server
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/app/',
    external_stylesheets = layout.get_stylesheet()
)
app.layout = layout.get_layout()

# invoke callbacks 
callbacks.table_callback(app, 'go-val', 'n_clicks', 'aurin-table', 'data')
callbacks.graph_callback(app, 'go-val', 'n_clicks', 'twitter_graph')
callbacks.test_callback(app)

@server.route('/')
def index():
    return "Hello World"

@server.route('/api/test_data', methods=['GET'])
def connect():
	return route_funcs.dump_data()

#@server.route('/api/aurin', methods=['GET'])
#def connect(db):
#	return route_funcs.dump_aurin()

#@server.route('/api/twitter', methods=['GET'])
#def connect(db):
#	return route_funcs.dump_twitter()

#@atexit.register
#def shutdown():
#  database.disconnect()

if __name__ == '__main__':
    app.run_server(debug=True)
