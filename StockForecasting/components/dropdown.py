# components/layout.py

import dash_core_components as dcc
import dash_html_components as html

def create_layout():
    return html.Div([
        html.H1("Stock Price Forecasting Dashboard"),
        dcc.Dropdown(
            id='stock-dropdown',
            options=[
                {'label': 'Apple', 'value': 'AAPL'},
                {'label': 'Google', 'value': 'GOOGL'},
                # Add more stocks
            ],
            value='AAPL'
        ),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date='2023-01-01',
            end_date='2024-01-01'
        ),
        dcc.Graph(id='stock-graph')
    ])
