from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


from models.data_fetcher import fetch_stock_data
from models.forecasting_model import calculate_sma, linear_regression_forecast
from components.layout import create_layout
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.layout = create_layout()

@app.callback(
    Output('stock-graph', 'figure'),
    [Input('stock-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_graph(ticker, start_date, end_date):
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    # Simple Moving Average
    stock_data['SMA'] = calculate_sma(stock_data, window=20)
    
    # Linear Regression Forecast
    future_days, forecasted_prices = linear_regression_forecast(stock_data, forecast_days=30)
    
    fig = {
        'data': [
            go.Scatter(
                x=stock_data.index,
                y=stock_data['Close'],
                mode='lines',
                name=f'{ticker} Actual'
            ),
            go.Scatter(
                x=stock_data.index,
                y=stock_data['SMA'],
                mode='lines',
                name=f'{ticker} SMA (20 days)'
            ),
            go.Scatter(
                x=future_days,
                y=forecasted_prices,
                mode='lines',
                name=f'{ticker} Forecast'
            ),
        ],
        'layout': go.Layout(
            title=f'Stock Prices for {ticker}',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Price'},
            hovermode='closest'
        )
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
