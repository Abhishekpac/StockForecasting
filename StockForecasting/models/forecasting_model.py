from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


import pandas as pd

def calculate_sma(data: pd.DataFrame, window: int) -> pd.Series:
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain 'Close' column.")
    return data['Close'].rolling(window=window).mean()
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def linear_regression_forecast(stock_data: pd.DataFrame, forecast_horizon: int = 30):
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Days'] = (stock_data['Date'] - stock_data['Date'].min()).dt.days

    X = stock_data[['Days']]
    y = stock_data['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(stock_data['Days'].max() + 1, stock_data['Days'].max() + 1 + forecast_horizon).reshape(-1, 1)
    forecasted_prices = model.predict(future_days)

    future_dates = pd.date_range(start=stock_data['Date'].max(), periods=forecast_horizon + 1, closed='right')
    return future_dates, forecasted_prices


def forecast_stock_prices(stock_data: pd.DataFrame, forecast_horizon: int = 30):
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Days'] = (stock_data['Date'] - stock_data['Date'].min()).dt.days
    
    X = stock_data[['Days']]
    y = stock_data['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(stock_data['Days'].max() + 1, stock_data['Days'].max() + 1 + forecast_horizon).reshape(-1, 1)
    forecasted_prices = model.predict(future_days)

    return future_days.flatten(), forecasted_prices
