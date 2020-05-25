import flask
import atexit
import dash
import layout
import callbacks
import route_funcs
import database

# data stores
ip = "172.26.132.96:5984/"
user = "admin"
pw = "123"
db = database.database(ip, user, pw)
db.connect()
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
callbacks.table_callback(app, 'a-val', 'n_clicks', 'aurin-table', 'data')
callbacks.twitter_graph(app, 't-val', 'n_clicks', 'twitter_graph')

@server.route('/')
def index():
    return "Hello World"

@server.route('/api/aurin', methods=['GET'])
def connect_aurin(db = db):
	return route_funcs.dump_aurin(db)

@server.route('/api/twitter', methods=['GET'])
def connect_twitter(db = db):
	return route_funcs.dump_twitter(db)

@atexit.register
def shutdown():
  db.disconnect()

if __name__ == '__main__':
    app.run_server(debug=True)
