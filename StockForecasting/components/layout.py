import pandas as pd
import dash
from dash import dcc, html

import dash_bootstrap_components as dbc
from dash import html, dcc
from components.plotting import plot_stock_forecast

def create_layout():
    return dbc.Container([
        html.H1("Stock Forecasting Dashboard"),
        dcc.Dropdown(id='stock-dropdown', options=[
            {'label': 'AAPL', 'value': 'AAPL'},
            {'label': 'GOOGL', 'value': 'GOOGL'}
        ]),
        dcc.DatePickerRange(id='date-picker-range', start_date='2023-01-01', end_date='2023-12-31'),
        dcc.Graph(id='stock-graph')
    ])

from dash.dependencies import Input, Output
from models.data_fetcher import fetch_stock_data

from components.layout import create_layout
from models.forecasting_model import forecast_stock_prices
from components.plotting import plot_stock_forecast

app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])

app.layout = create_layout()

@app.callback(
    Output('stock-graph', 'figure'),
    [Input('stock-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_graph(ticker, start_date, end_date):
    stock_data = fetch_stock_data(ticker, period='1y')
    future_days, forecasted_prices = forecast_stock_prices(stock_data)
    
    fig = plot_stock_forecast(stock_data, future_days, forecasted_prices)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)



