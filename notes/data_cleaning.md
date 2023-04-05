
##__Data cleaning in pandas__

### change data types

```python
# change "date" dtype to datetime with format %Y/%m/%d
df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")
# change data type to float
df = df.astype({"precipitation": float})
# remove unit from "temp_min" column, change dtype to float
df["temp_min"] = df.temp_min.str.strip(" F").astype("float")
df.temp_min.dtype
```

### Replacing in pandas

```python
# replace the `$`-character with a numpy NaN value
df["precipitation"] = df.precipitation.replace("$", np.NaN)
# change data type to float
df = df.astype({"precipitation": float})
df.precipitation.dtypes
```

### Round 
```python
# rounding wind data
df["wind"] = df.wind.round(2)
df.head(5)
```

### Distinct values 

```python
# display number of distinct elements
df.weather.nunique()
# display all distinct elements
df["weather"].unique()
# reducing number of categorical values by mapping with a word-dictionary
```


### Missing numbers

```python
# import missingno
import missingno as msno
# display number of missing values per column
df.isna().sum()
# plotting percentage of missing values per column
```

### Drop NaNs 

```python
# drop all rows if they contain at least one missing value (in any column)
df.dropna()
df.dropna(how='all')
df.dropna(thresh=2)
```


### Fill NaNs

```python
# use fillna to impute missing values
df.fillna(method="bfill", inplace=True)
df.fillna(0)
df.fillna({'precipitation': 0, 'temp_min': 0, 'temp_max': 42, 'wind': 0, 'weather': 'no_weather'})
df.fillna(method='ffill') # forward fill
df.fillna(method='bfill') #backward fill
df.fillna(method='ffill', axis=1)
df.fillna(method='ffill', limit=1)
```

### Make columns python friendly

```
import pandas as pd

def make_columns_python_friendly(df):
    """
    Modify DataFrame column names to be more Python friendly:
    - Replace spaces with underscores
    - Convert all characters to lowercase
    - Remove special characters

    :param df: Input DataFrame
    :return: Modified DataFrame with Python friendly column names
    """
    import re

    def clean_column_name(column):
        column = column.lower()  # Convert to lowercase
        column = column.replace(" ", "_")  # Replace spaces with underscores
        column = re.sub(r'\W', '', column)  # Remove special characters
        column = re.sub(r'^(\d)', r'_\1', column)  # Add underscore if starts with a number
        return column

    # Apply the transformation to each column name
    df.columns = [clean_column_name(col) for col in df.columns]

    return df

# Example usage:
data = {
    'Column 1': [1, 2, 3],
    'ColUmn_2': [4, 5, 6],
    'Column$3': [7, 8, 9],
    '1stColumn': [10, 11, 12]
}

df = pd.DataFrame(data)
print("Original column names:")
print(df.columns)

df = make_columns_python_friendly(df)
print("\nPython friendly column names:")
print(df.columns)

```


