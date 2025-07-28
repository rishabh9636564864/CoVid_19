Explanation Line-by-Line**

1. import pandas as pd:  
   -Keyword** `import` tells Python to load a module.
   - We’re importing **Pandas**, the go-to library for handling tabular data.
   - `as pd` creates a **shortcut** so you can write `pd.DataFrame` instead of the long `pandas.DataFrame`.

2. `import matplotlib.pyplot as plt`:  
   - This is used for plotting **basic charts**.
   - `pyplot` is a sub-module in **matplotlib**.
   - We alias it as `plt` for easier use.

3. `import seaborn as sns`:  
   - Seaborn is built on top of matplotlib, and it’s great for more **aesthetic plots** and easier statistical visualizations.
   - `sns` is just a convenient nickname.

4. `df = pd.read_csv(...)`:  
   - This reads the COVID-19 dataset directly from a **URL** (you can also use a local file).
   - The `.read_csv()` method loads the data as a **DataFrame**.
   What Is a DataFrame?
        A DataFrame is a two-dimensional, tabular data structure:
        Think of it as a table with rows and columns
        Each column can hold different data types (e.g., integers, strings, floats)
        It has labels for both rows (called index) and columns

5. `india_df = df[df['location'] == 'India']`:  
   - This filters rows where the **location column** is India.
   - It uses a **boolean mask** which is a very fast way to filter in Pandas.
   A boolean mask is:
        A list or array of boolean values (True or False)
        Used to select elements from another array or DataFrame
        Created by applying a conditional expression to data

6. `india_df['date'] = pd.to_datetime(...)`:  
   - Converts the **date column** from string to `datetime64` type so we can do time-based operations.
   - Essential for any **time-series analysis or plotting**.

7. `columns_to_keep = [...]`:  
   - Creates a **list of columns** that are relevant for this dashboard.
   - Keeps it **focused** and easy to visualize later.

8. `india_df = india_df[columns_to_keep]`:  
   - This trims the DataFrame to include only our selected columns.

9. `india_df.dropna(inplace=True)`:  
   - Drops any rows that have missing values (`NaN`).
   - `inplace=True` modifies the DataFrame without making a copy (saves memory).
