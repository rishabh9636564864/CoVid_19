# utils.py

import pandas as pd
import warnings

# ⚠️ Ignore FutureWarnings (e.g., SettingWithCopyWarning)
def suppress_warnings():
    warnings.simplefilter(action="ignore", category=FutureWarning)


# 🔄 Fetch dataset from Our World in Data
def load_covid_data(url=None):
    default_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    source = url if url else default_url
    try:
        df = pd.read_csv(source)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


# 🧹 Clean and format dataset
def clean_data(df, country='India'):
    if df is None:
        return None

    try:
        country_df = df[df['location'] == country].copy()
        country_df['date'] = pd.to_datetime(country_df['date'])
        columns = ['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
        country_df = country_df[columns]
        country_df.dropna(inplace=True)
        return country_df
    except Exception as e:
        print(f"Error cleaning data: {e}")
        return None
