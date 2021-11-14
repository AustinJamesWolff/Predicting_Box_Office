# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load


# Imports from this application
from app import app

# app = dash.Dash(__name__)

# model_xgb_2 = load('assets/model_xgb_2.joblib') # Uses Total_Gross_Bankability
# model_xgb_3 = load('assets/model_xgb_3.joblib') # NO Total_Gross_Bankability
model_xgb_4 = load('assets/model_xgb_4.joblib') # NO Total_Gross_Bankability, NO Region


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# row = html.Div(
#     [
#         row1 = dbc.Row(
#             [
#                 dcc.Markdown(
#                     """
                
#                     ## Estimate Your Movie's Box Office Using AI

#                     Simply enter your movie's details (like budget) and
#                     get a rough estimate of what your box office might be.

#                     """
#                 )
                
#             ],
#             md=4,
#         )
#     ],
       
#     [
#         row2 = dbc.Row(
#             [
#                 dcc.Markdown("## Enter Your Movie's Details", className='mb-5'),
#                 dcc.Markdown("#### Genre: (Select One)"),
#                 dcc.Dropdown(
#                     id='genre',
#                     options = [
#                         {'label':'Comedy', 'value':'Comedy'},
#                         {'label' : 'Action', 'value' : 'Action'},
#                         {'label' : 'Drama', 'value' : 'Drama'},
#                         {'label' : 'Crime', 'value': 'Crime'},
#                         {'label' : 'Biography', 'value': 'Biography'},
#                         {'label' : 'Adventure', 'value' : 'Adventure'},
#                         {'label' : 'Animation', 'value' : 'Animation'},
#                         {'label' : 'Horror', 'value' : 'Horror'},
#                         {'label' : 'Fantasy', 'value' : 'Fantasy'},
#                         {'label' : 'Mystery', 'value' : 'Mystery'},
#                     ],
#                     value="Comedy",
#                     className='mb-5'),
#                 dcc.Markdown("#### Budget: (Please Enter A Number)"),
#                 dcc.Input(value='budget', type='text')


#             ]

#         )
#     ]
# )





# column1 = dbc.Col(
#             [
#                 dcc.Markdown(
#                     """
                
#                     ## Estimate Your Movie's Box Office Using AI

#                     Simply enter your movie's details (like budget) and
#                     get a rough estimate of what your box office might be.

#                     """
#                 )
                
#             ],
#             md=4,
#         )

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
# hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#             [
#                 dcc.Graph(figure=fig),
#             ]
#         )

# layout = dbc.Row([column1, column2])







app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True
        ),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run_server(debug=True)