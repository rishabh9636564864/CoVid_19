# ================================
# Interactive COVID-19 Dashboard for India
# Author: Rishabh
# ================================

# 🔧 Import custom helper functions and libraries
from utils import suppress_warnings, load_covid_data, clean_data
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Suppress warning messages (like SettingWithCopyWarning)
suppress_warnings()

# 📥 Load full global COVID dataset
df = load_covid_data()

# 🇮🇳 Clean and filter data for India
india_df = clean_data(df, country='India')

# 🛑 Check if data is loaded successfully
if india_df is None or india_df.empty:
    print("❌ Error: Data could not be loaded or is empty.")
    exit()

# 🎨 Set Seaborn theme
sns.set(style='whitegrid')

# 📊 Plot 1: Total COVID-19 Cases Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=india_df, x='date', y='total_cases', color='blue')
plt.title('📈 Total COVID-19 Cases in India Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Cases', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Plot 2: Daily New Cases and Deaths
plt.figure(figsize=(12, 6))
sns.lineplot(data=india_df, x='date', y='new_cases', label='New Cases', color='orange')
sns.lineplot(data=india_df, x='date', y='new_deaths', label='New Deaths', color='red')
plt.title('📊 Daily New COVID-19 Cases & Deaths in India', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
