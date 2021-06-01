from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import pandas as pd
data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
countries = data['location'].unique()
iso_codes = data['iso_code'].unique()
app = DjangoDash('covid_dash')
app.css.append_css({'external_url': '/_static/css/dash.css'})
app.layout = html.Div([
    # first row
    html.Div([
        html.Div([
            dcc.Dropdown(id='country-dropdown', multi=True, options=[{'label': country, 'value': iso_code} for country, iso_code in zip(countries, iso_codes)])
        ], className='three columns'),
        html.Div([dcc.DatePickerRange(id='date-picker',
                                      clearable=True)], className='three columns'),
    ]),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('country-dropdown', 'value'), Input('date-picker', 'start_date'), Input('date-picker', 'end_date')]
)
def update_div(country, start, end):
    if start is None:
        start = ''
    if end is None:
        end = ''
    return country