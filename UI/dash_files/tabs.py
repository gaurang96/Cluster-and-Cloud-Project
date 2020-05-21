import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table

tab_styles = {'width' : '250px'}
tab_offsets = {'padding-left' : '20px', 'padding-top': '20px'}

def get_tabs():
	return dbc.Row(
		[
			dbc.Tabs(
			    [
			        dbc.Tab(get_tab1(), label="Aurin", tab_style = tab_styles),
			        dbc.Tab(get_tab2(), label="Twitter", tab_style = tab_styles),
			        dbc.Tab(get_tab3(), label="Inferences", tab_style = tab_styles),
			        dbc.Tab(get_tab4(), label="Credits", tab_style = tab_styles)
			    ]
		    )
    	], 
    	style = {'padding-left' : "15px"}
    )

def get_tab1():
	body  = dbc.Col([
		dbc.Row(html.Div(children = ["this tab should return data that is from aurin"])),
		dbc.Row(get_table('aurin-table', ['id', 'year', 'month', 'value']))
		],
		style = tab_offsets
	)

	return body




def get_tab2():
	body = html.Div("Tweets Summary", style = tab_offsets)
	return body




def get_tab3():
	body = html.Div("Inferences", style = tab_offsets)
	return body




def get_tab4():
	body = html.Div("Group member details and credits", style = tab_offsets)
	return body




def get_table(tid, colnames):
	style_cell = {'height': 'auto', 'textAlign' : 'center'}
	style_table = {'width' : '800px', 'height': '400px', 'overflowY': 'auto', 'overflowX' : 'none'}
	t_cols = [{'name': i, 'id': i } for i in colnames]
	t_data = [{col : 0 for col in colnames}]

	table = dash_table.DataTable(id = tid, columns = t_cols,  data = t_data, style_table = style_table, style_cell = style_cell)
	return table