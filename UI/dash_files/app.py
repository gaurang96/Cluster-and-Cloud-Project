import flask
import dash
import layout
import callbacks
import route_funcs

# flask server
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/app/',
    external_stylesheets = layout.get_stylesheet()
)

# set the layout 
app.layout = layout.get_layout()

# invoke callbacks 
callbacks.table_callback(app, 'go-val', 'n_clicks', 'aurin-table', 'data')

callbacks.test_callback(app)

@server.route('/')
def index():
    return "Hello World"

@server.route('/api/test_data', methods=['GET'])
def connect():
	return route_funcs.dump_data()
#@atexit.register
#def shutdown():
#  database.disconnect()

if __name__ == '__main__':
    app.run_server(debug=True)
