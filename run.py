# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from pages import index

# Imports from this application
from app import app, server

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand="Austin Wolff",
    brand_href='/', 
    children=[
        # dbc.NavItem(dcc.Link('LinkedIn', href='https://www.linkedin.com/in/austin-james-wolff/', className='nav-link')), 
        # dbc.NavItem(dcc.Link('Research', href='https://www.linkedin.com/pulse/building-predictive-models-random-forest-xgboost-grid-austin-wolff/', className='nav-link')),
        dbc.NavItem(html.A('Research', href='https://www.linkedin.com/pulse/building-predictive-models-random-forest-xgboost-grid-austin-wolff/', target="_blank", className='nav-link')),
        dbc.NavItem(html.A('Limitations', href='https://www.linkedin.com/pulse/using-multiple-linear-regression-examine-what-variables-austin-wolff/#Conclusion', target="_blank", className='nav-link')),
        dbc.NavItem(html.A('GitHub', href='https://github.com/AustinJamesWolff/Data-Science-Portfolio/tree/main/Box_Office_XGBoost_Regression', target="_blank", className='nav-link')), 
        dbc.NavItem(html.A('LinkedIn', href='https://www.linkedin.com/in/austin-james-wolff/', target="_blank", className='nav-link'))
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Austin Wolff ', className='mr-2'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/AustinJamesWolff/Data-Science-Portfolio/tree/main/Box_Office_XGBoost_Regression', target="_blank"), 
                    html.Span(' ', className='mr-2'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/austin-james-wolff/', target="_blank")
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    elif pathname == '/pagename':
        return pagename.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)