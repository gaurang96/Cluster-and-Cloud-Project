import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# App setup
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Data Pipeline (TBD)
Data = None
# App objects
table_header = [html.Thead(html.Tr([html.Th("City"), html.Th("Population")]))]

row1 = html.Tr([html.Td("Sydney"), html.Td("5,230,000")])
row2 = html.Tr([html.Td("Melbourne"), html.Td("4,930,000")])
row3 = html.Tr([html.Td("Brisbane"), html.Td("2,460,000")])
row4 = html.Tr([html.Td("Canberra"), html.Td("450,000")])

table_body = [html.Tbody([row1, row2, row3, row4])]

fig_1 = {
	'data': [
		{'x' : [1, 2, 3, 4], 'y': [1, 2, 3, 5], 'type': 'bar', 'name': 'group_A'},
		{'x' : [1, 2, 3, 4], 'y': [1, 4, 9, 16], 'type': 'bar', 'name': 'group_B'},
	],

	'layout' : {
		'title' : "this is a sample Bar Chart"
	}
}

graph_1 = dcc.Graph(id = 'graph_1', figure = fig_1)
# App Functions 

# Callbacks


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
						html.Div(children = "this is the filter column (optional)"),

					],
					width = 3
				),

				dbc.Col(
					[	
						html.Div(children = "this is the visualisation column"),
						html.Div(children = "this is a table"),
						dbc.Table(table_header + table_body, bordered=True),
						html.Div(children = ""),
						html.Div(children = ""),
					
						graph_1

					],
					width = 9
				) 

			]
		)
	]
)


if __name__ == '__main__':
    app.run_server(debug=True)


    # request filters for data and confirm 
    # send request for data
    # recieve data and visualise it 