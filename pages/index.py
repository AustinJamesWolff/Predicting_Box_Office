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
       
    # [
    #     row2 = dbc.Row(
    #         [
    #             dcc.Markdown("## Enter Your Movie's Details", className='mb-5'),
    #             dcc.Markdown("#### Genre: (Select One)"),
    #             dcc.Dropdown(
    #                 id='genre',
    #                 options = [
    #                     {'label':'Comedy', 'value':'Comedy'},
    #                     {'label' : 'Action', 'value' : 'Action'},
    #                     {'label' : 'Drama', 'value' : 'Drama'},
    #                     {'label' : 'Crime', 'value': 'Crime'},
    #                     {'label' : 'Biography', 'value': 'Biography'},
    #                     {'label' : 'Adventure', 'value' : 'Adventure'},
    #                     {'label' : 'Animation', 'value' : 'Animation'},
    #                     {'label' : 'Horror', 'value' : 'Horror'},
    #                     {'label' : 'Fantasy', 'value' : 'Fantasy'},
    #                     {'label' : 'Mystery', 'value' : 'Mystery'},
    #                 ],
    #                 value="Comedy",
    #                 className='mb-5'),
    #             dcc.Markdown("#### Budget: (Please Enter A Number)"),
    #             dcc.Input(value='budget', type='text')


    #         ]

    #     )
    # ]
# )





column1 = dbc.Container(
    [
        html.Div(
                [dcc.Markdown(
                   
                    """
                    
                    ## Estimate Your Movie's Box Office Using AI

                    Simply enter your movie's details (like budget) and
                    get a rough estimate of what your box office might be.






                    
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

    
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
hover_name="country", log_x=True, size_max=60)

column2 = dbc.Container(
            # [
            #     dcc.Graph(figure=fig),
            # ],
            # [
        # dbc.Row(
            [
                dcc.Markdown("### Enter Your Movie's Details", className='mb-5'),
                dcc.Markdown("#### Genre: (Select One)"),
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
                    value="Comedy",
                    className='mb-5'),
                dcc.Markdown("#### Budget: (Please Enter A Number)"),
                dcc.Input(id='budget', type='number'),
                dcc.Markdown("#### Runtime: (Please Enter Number Of Minutes)"),
                dcc.Input(id='runtime' ,type='number'),
                dcc.Markdown("#### Rated: (Please Select MPAA Rating)"),
                dcc.Dropdown(
                    id='rating',
                    options = [
                        {'label':'G', 'value':'G'},
                        {'label' : 'PG', 'value' : 'PG'},
                        {'label' : 'PG-13', 'value' : 'PG-13'},
                        {'label' : 'R', 'value': 'R'}
                    ],
                    value="G",
                    className='mb-5'),
                dcc.Markdown("#### Release Year: (Please Enter Release Year)"),
                dcc.Input(id='year' ,type='number'),
                dcc.Markdown("#### Month: (Please Select Month Released)"),
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
                    value="January",
                    className='mb-5'),
                dcc.Markdown("#### IMDb Score: (Please Enter Est. Score)"),
                dcc.Input(id='score' ,type='number'),
                html.Br()
            ]

        )
    # ]
    #     )


column3 = dbc.Container(
    [
        html.H2("Estimated Box Office", className="mb-5"),
        html.Div(id='prediction-content', className='lead')
    ]

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
        columns=['genre', 'budget', 'runtime', 'rating', 'year', 'month', 'score'],
        data=[[genre, budget, runtime, rating, year, month, score]]
    )
    y_pred = model_xgb_4.predict(df)[0]
    if y_pred < 0:
        return 0
    else:
        return '{:,}'.format(y_pred.round(2))


layout = dbc.Container([column1, column2, column3])
