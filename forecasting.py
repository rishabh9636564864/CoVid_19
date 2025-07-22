# forecasting.py

from prophet import Prophet
import pandas as pd

# 🧠 Prepare data in Prophet-friendly format
def format_for_prophet(df, metric='total_cases'):
    try:
        data = df[['date', metric]].rename(columns={'date': 'ds', metric: 'y'})
        return data
    except Exception as e:
        print(f"❌ Error formatting data for Prophet: {e}")
        return None

# 🔮 Generate future forecast
def make_forecast(df, periods=30):
    try:
        model = Prophet()
        model.fit(df)

        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)

        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    except Exception as e:
        print(f"❌ Forecasting failed: {e}")
        return None
