# ================================
# COVID-19 Dashboard for India
# Author: Rishabh
# ================================

# 🔧 Import modules
from utils import suppress_warnings, load_covid_data, clean_data
from forecasting import format_for_prophet, make_forecast
from visuals import plot_total_cases, plot_daily_trends, plot_forecast

# 📊 Suppress warnings
suppress_warnings()

# 📥 Load and clean data
df = load_covid_data()
india_df = clean_data(df, country='India')

# 🛑 Validate data
if india_df is None or india_df.empty:
    print("❌ Error: Data could not be loaded or is empty.")
    exit()

# 🎨 Plot historical trends
plot_total_cases(india_df, country='India')
plot_daily_trends(india_df, country='India')

# 🔮 Forecast future cases
formatted_df = format_for_prophet(india_df, metric='total_cases')
forecast_df = make_forecast(formatted_df, periods=30)

# 📈 Plot forecast
if forecast_df is not None:
    plot_forecast(formatted_df, forecast_df)
