# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load
import pandas as pd


# Imports from this application
from app import app

# app = dash.Dash(__name__)

# model_xgb_2 = load('assets/model_xgb_2.joblib') # Uses Total_Gross_Bankability
# model_xgb_3 = load('assets/model_xgb_3.joblib') # NO Total_Gross_Bankability
model_xgb_4 = load('assets/model_xgb_4.joblib') # NO Total_Gross_Bankability, NO Region


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout



column1 = html.Div(
    
    dbc.Container(
    [
        html.Div(
                [dcc.Markdown(
                   
                    """
                    
                    # Estimate Your Movie's Box Office Using AI

                    Simply enter your movie's details (like budget) and get a rough estimate of what your box office might be.






                    
                    """
                )
                ], 
                # style={'width': '100%', 'display': 'flex', 
                # 'align-items': 'center', 
                # 'justify-content': 'center'
                # }
        )
    ],
    # md=4,
    ), style={'text-align':'center', 'padding-top':'50px'}
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
hover_name="country", log_x=True, size_max=60)

column2 = html.Div(

        dbc.Container(
            # [
            #     dcc.Graph(figure=fig),
            # ],
            # [
        # dbc.Row(
            [
                # dcc.Markdown("### Enter Your Movie's Details:", className='mb-5'),
                dcc.Markdown("#### Genre:"),
                dcc.Dropdown(
                    id='genre',
                    options = [
                        {'label':'Comedy', 'value':'Comedy'},
                        {'label' : 'Action', 'value' : 'Action'},
                        {'label' : 'Drama', 'value' : 'Drama'},
                        {'label' : 'Crime', 'value': 'Crime'},
                        {'label' : 'Biography', 'value': 'Biography'},
                        {'label' : 'Adventure', 'value' : 'Adventure'},
                        {'label' : 'Animation', 'value' : 'Animation'},
                        {'label' : 'Horror', 'value' : 'Horror'},
                        {'label' : 'Fantasy', 'value' : 'Fantasy'},
                        {'label' : 'Mystery', 'value' : 'Mystery'},
                    ],
                    # value="Comedy",
                    placeholder='Select Genre...',
                    # className='mb-5'
                    style = {'margin-bottom':'30px'},
                    ),
                dcc.Markdown("#### Budget:"),
                dcc.Input(id='budget', type='number', 
                placeholder='Budget...',
                style = {'margin-bottom':'30px'}),
                dcc.Markdown("#### Runtime:"),
                dcc.Input(id='runtime' ,type='number', 
                placeholder='Number of Minutes...',
                style = {'margin-bottom':'30px'}),
                dcc.Markdown("#### Rated:"),
                dcc.Dropdown(
                    id='rating',
                    options = [
                        {'label':'G', 'value':'G'},
                        {'label' : 'PG', 'value' : 'PG'},
                        {'label' : 'PG-13', 'value' : 'PG-13'},
                        {'label' : 'R', 'value': 'R'}
                    ],
                    # value="G",
                    placeholder='Select MPAA Rating...',
                    # className='mb-5'
                    style = {'margin-bottom':'30px'}
                    ),
                dcc.Markdown("#### Release Year:"),
                dcc.Input(id='year' ,type='number',
                placeholder='Year Released...', 
                style = {'margin-bottom':'30px'}),
                dcc.Markdown("#### Month:"),
                dcc.Dropdown(
                    id='month',
                    options = [
                        {'label':'January', 'value':'January'},
                        {'label' : 'February', 'value' : 'February'},
                        {'label' : 'March', 'value' : 'March'},
                        {'label' : 'April', 'value': 'April'},
                        {'label' : 'May', 'value': 'May'},
                        {'label' : 'June', 'value' : 'June'},
                        {'label' : 'July', 'value' : 'July'},
                        {'label' : 'August', 'value' : 'August'},
                        {'label' : 'September', 'value' : 'September'},
                        {'label' : 'October', 'value' : 'October'},
                        {'label' : 'November', 'value' : 'November'},
                        {'label' : 'December', 'value' : 'December'},
                    ],
                    # value="January",
                    placeholder='Month Released...',
                    # className='mb-5'
                    style = {'margin-bottom':'30px'}
                    ),
                dcc.Markdown("#### IMDb Score:"),
                dcc.Input(id='score', type='number', placeholder='Estimated Score...',),
                html.Br(),
                dcc.Markdown(
                    """
                    
                    """
                ),

            ]

        ), style={'padding': 50}
)
    # ]
    #     )


column3 = html.Div(

    dbc.Container(
    [
        html.H2("Estimated Box Office:", 
                className="mb-5",
                style={
                    'margin-top': '40px'
                    }
                    ),
        html.H3(id='prediction-content', 
                className='mb-5', 
                style={
                        # 'border':'1px solid grey', 
                        'margin-left':'20px',
                        'margin-right':'20px',
                        'margin-top': '-10px',
                        # 'padding':'10px', 
                        # 'color':'black', 
                        # 'background-color':'white'
                        }
                ),
        dcc.Markdown("""
                    These predictions are imperfect due to limited data and high variance.
                    See "Limitations" for more details.""", 
                className='mb-5', 
                style={'margin-left':'20px',
                        'margin-right':'20px',
                        'margin-top': '-10px',
                        'font-style':'italic',
                        # 'padding':'10px', 
                        # 'color':'black', 
                        # 'background-color':'white'
                        }
        )
    ]

    ), style={'text-align':'center', 
            'margin-top':'10px',
            'margin-left':'50px',
            'margin-right':'50px',
            'margin-bottom':'100px',
            'border':'1px solid grey',
            # 'margin-top': '-10px'
            }
)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('genre', 'value'), Input('budget', 'value'), Input('runtime','value'),
    Input('rating', 'value'), Input('year', 'value'), Input('month', 'value'),
    Input('score', 'value')
    ]
)

def predict(genre, budget, runtime, rating, year, month, score):
    df = pd.DataFrame(
        columns=['rating', 'genre', 'year', 'month', 'score', 'budget', 'runtime'],
        data=[[rating, genre, year, month, score, budget, runtime]]
    )
    y_pred = model_xgb_4.predict(df)[0]
    if y_pred < 0:
        return 0
    else:
        return '{:,}'.format(y_pred.round(2))


layout = dbc.Container([
                        column1, 
                        column2, 
                        column3])
