# visuals.py

import matplotlib.pyplot as plt
import seaborn as sns

# 🖼 Set a global Seaborn style
sns.set(style='whitegrid')


# 📊 Plot Total Cases Over Time
def plot_total_cases(df, country='India'):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='date', y='total_cases', color='blue')
    plt.title(f'Total COVID-19 Cases in {country} Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 📊 Plot Daily New Cases and Deaths
def plot_daily_trends(df, country='India'):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='date', y='new_cases', label='New Cases', color='orange')
    sns.lineplot(data=df, x='date', y='new_deaths', label='New Deaths', color='red')
    plt.title(f'Daily New COVID-19 Cases & Deaths in {country}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 🔮 Plot Prophet Forecast
def plot_forecast(actual_df, forecast_df):
    plt.figure(figsize=(12, 6))
    plt.plot(actual_df['ds'], actual_df['y'], label='Historical Cases', color='blue')
    plt.plot(forecast_df['ds'], forecast_df['yhat'], label='Forecast', linestyle='--', color='green')
    plt.fill_between(forecast_df['ds'], forecast_df['yhat_lower'], forecast_df['yhat_upper'],
                     color='gray', alpha=0.3, label='Confidence Interval')
    plt.title('COVID-19 Case Forecast')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
