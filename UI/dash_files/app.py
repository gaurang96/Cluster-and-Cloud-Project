import flask
import atexit
import dash
import json
import layout
import callbacks
import database

# data stores
ip = "172.26.132.96:5984"
user = "admin"
pw = "123"
db = database.database(ip, user, pw)
db.connect()

# app and server
host ='127.0.0.1' # '172.26.134.13'
port = '8050' #'3000'
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/app/',
    external_stylesheets = layout.get_stylesheet()
)
app.layout = layout.get_layout()

# invoke callbacks 
callbacks.positive_callback(app, 't-val', 'n_clicks', 'positive-chart', host, port)
callbacks.negative_callback(app, 't-val', 'n_clicks', 'negative-chart', host, port)
callbacks.trend_callback(app, 't-val', 'n_clicks', 'trends-chart', host, port)
callbacks.unemp_callback(app, 't-val', 'n_clicks', 'unemployment-chart', host, port)


def dump_data(database, idx):
	view_data = database.collect_data(idx)
	view_data.pop('_id', None)
	view_data.pop('_rev', None)

	return json.dumps(view_data)

@server.route('/')
def index():
    return "Hello World"

@server.route('/api/')
def api_home():
    return "This is has been intentionally left blank"

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
    app.run_server(port = port , host = host, debug=False)
