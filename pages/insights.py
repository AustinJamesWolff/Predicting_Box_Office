# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

model_xgb_2 = load('assets/model_xgb_2.joblib')


# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights


            """
        ),

    ],
)

layout = dbc.Row([column1])