import flask
import atexit
import dash
import json
import layout
import callbacks
import route_funcs
import database

# data stores
ip = "172.26.132.96:5984"
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
callbacks.unemp_callback(app, 't-val', 'n_clicks', 'unemployment-chart')

def dump_data(database, idx):
	view_data = database.collect_data(idx)
	view_data.pop('_id', None)
	view_data.pop('_rev', None)

	return json.dumps(view_data)

@server.route('/')
def index():
    return "Hello World"

@server.route('/api/positive', methods=['GET'])
def get_pos(db = db):
	return dump_data(db, 0)

@server.route('/api/negative', methods=['GET'])
def get_neg(db = db):
	return dump_data(db, 1)

@server.route('/api/trend', methods=['GET'])
def get_trend(db = db):
	return dump_data(db, 2)

@server.route('/api/unemployment', methods=['GET'])
def connect_unemployment(db = db):
	return dump_data(db, 3)

@atexit.register
def shutdown():
  db.disconnect()


if __name__ == '__main__':
    app.run_server(debug=True)
