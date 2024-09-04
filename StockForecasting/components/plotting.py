import plotly.graph_objects as go
import pandas as pd
import plotly.graph_objs as go

def plot_stock_forecast(stock_data, future_days, forecasted_prices):
    trace_actual = go.Scatter(
        x=stock_data['Date'],
        y=stock_data['Close'],
        mode='lines',
        name='Actual Prices'
    )

    trace_forecast = go.Scatter(
        x=pd.to_datetime(stock_data['Date'].max() + pd.to_timedelta(future_days, unit='D')),
        y=forecasted_prices,
        mode='lines',
        name='Forecasted Prices',
        line=dict(dash='dash')
    )

    layout = go.Layout(
        title='Stock Price Forecast',
        xaxis={'title': 'Date'},
        yaxis={'title': 'Price'},
        hovermode='closest'
    )

    figure = go.Figure(data=[trace_actual, trace_forecast], layout=layout)
    return figure


def plot_stock_forecast(stock_data, future_days, forecasted_prices):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], mode='lines', name='Historical'))
    fig.add_trace(go.Scatter(x=future_days, y=forecasted_prices, mode='lines', name='Forecast'))

    fig.update_layout(title='Stock Price Forecast', xaxis_title='Date', yaxis_title='Price')
    return fig
