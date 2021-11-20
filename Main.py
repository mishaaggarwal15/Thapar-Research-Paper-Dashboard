from mimetypes import suffix_map
import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from pkg_resources import resource_string
import plotly.graph_objs as go
from dash.dependencies import Input, Output



app = dash.Dash()

myheading1 = 'Thapar Research Paper Dashboard'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                title= myheading1,
                update_title='Loading...',
                suppress_callback_exceptions=True)
colors = {"background": "#D6EAF8", 'text': '#3b75af'}

dept = []
sum_years_1 = []
sum_years_2 = []
years = ['2018', '2019', '2020', '2021']

@app.callback(
    Output('graph1', 'figure'),
    Input('first-dropdown', 'value')
)
def update_output_1(value):
    dept.clear()
    sum_years_1.clear()
    for j in range(4):
        sum = []
        for i in range(9):
            x = str(i)
            year = years[j]
            extension = '.csv'
            filename = x + '_' + year + extension

            df = pd.read_csv('final_data/{}'.format(filename))
            sum.append(df['count'].sum())
        sum_years_1.append(sum)
    print(sum_years_1)
    for i in range(4):
        dept.append(sum_years_1[i][int(value)])
    
    return {
        'data': [
            {'x': years, 'y': dept, 'type': 'bar', 'name': 'SF'}

        ],
        'layout': {
            'title': 'Department-Wise Data Visualization',
            'paper_bgcolor':"#D6EAF8"
        }
    }

@app.callback(
    Output('graph2', 'figure'),
    Input('second-dropdown', 'value')
)
def update_output_2(value):
    dept.clear()
    sum_years_2.clear()
    for j in range(4):
        sum = []
        for i in range(9):
            x = str(i)
            year = years[j]
            extension = '.csv'
            filename = x + '_' + year + extension

            df = pd.read_csv('final_data/{}'.format(filename))
            sum.append(df['count'].sum())
        sum_years_2.append(sum)
    
    data = sum_years_2[int(value)]
    return {
        'data': [
            {'x': ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu'], 'y': data, 'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'title': 'Year-Wise Data Visualization',
            'paper_bgcolor':"#D6EAF8"
        }
        
    }


dept = ['CSED', 'CSED_derabassi', 'Chemical', 'EIC', 'ECE', 'Mechanical', 'Biotech', 'Civil', 'Distant_Edu']
app.layout = html.Div([
    html.Div(style={'marginTop': 0,'marginBottom': 0, 'backgroundColor': colors['background']}, children=[
    html.H1('Thapar Research Paper Dashboard', style={
            'textAlign': 'center',
            'color': colors['text'],
            'marginBottom': 0,'marginTop': 0
        }),
            html.P('Analysis of papers published by college per year', style={
            'textAlign': 'center',
            'color': colors['text'],
            'marginBottom': 8,'marginTop': 0
        }),
            ]),
    
    html.Label('Choose a Year'),
    dcc.Dropdown(
        id = 'second-dropdown',
        options = [
            {'label':'2018', 'value' : '0'},
            {'label':'2019', 'value' : '1'},
            {'label':'2020', 'value' : '2' },
            {'label':'2021', 'value' : '3'},            
        ],
        clearable=False,
        placeholder = 'Select Year',
        value = '0'
            ),
    dcc.Graph(id='graph2'),  
    html.Label('Choose a Department'),
    dcc.Dropdown(
        id = 'first-dropdown',
        options = [
            {'label':'CSED', 'value' : '0'},
            {'label':'CSED_derabassi', 'value' : '1'},
            {'label':'Chemical', 'value' : '2' },
            {'label':'EIC', 'value' : '3'},
            {'label':'ECE', 'value' : '4' },
            {'label':'Mechanical', 'value' : '5'},
            {'label':'Biotech', 'value' : '6' },
            {'label':'Civil', 'value' : '7'},
            {'label':'Distant_Edu', 'value' : '8' },
            
        ],
        clearable=False,
        placeholder = 'Select a Department',
        value = '0'
            ),
    dcc.Graph(id='graph1'),
    html.Div([
    html.Br(),
        html.Div([html.A('Developed by Misha Aggarwal', href='https://github.com/mishaaggarwal15/currency_predictor', target='_blank')]),
        html.Br(),
    ],style = {'marginTop': 0,'marginBottom': 0, 'backgroundColor': colors['background'],'textAlign': 'center'})
])
                



if __name__ == '__main__':
    app.run_server(debug=True)