import dash_bootstrap_components as dbc
import dash_html_components as html

tab_styles = {'width' : '250px'}
tab_offsets = {'padding-left' : '20px', 'padding-top': '20px'}

def get_tabs():
	return dbc.Row(
		[
			dbc.Tabs(
			    [
			        dbc.Tab(get_tab1(), label="Tab 1", tab_style = tab_styles),
			        dbc.Tab(get_tab2(), label="Tab 2", tab_style = tab_styles),
			        dbc.Tab(get_tab3(), label="Tab 3", tab_style = tab_styles),
			        dbc.Tab(get_tab4(), label="Tab 4", tab_style = tab_styles)
			    ]
		    )
    	], 
    	style = {'padding-left' : "15px"}
    )

def get_tab1():
	body  = html.Div("Aurin Summary", style = tab_offsets)
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