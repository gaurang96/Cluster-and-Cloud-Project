import flask
import dash
import layout

# flask server
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/',
    external_stylesheets = layout.get_stylesheet()
)
app.layout = layout.get_layout()

# main dashboard

@server.route('/')
def index():
    return 'Hello Flask app'
    
	
if __name__ == '__main__':
    app.run_server(debug=True)
