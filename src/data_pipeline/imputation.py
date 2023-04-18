import pandas as pd
import numpy as np


def impute(series):
    mean_val = series.mean()
    return series.fillna(mean_val)


# Add your functions to impute min and max
# function to impute NaNs with min value
def impute_min(series: pd.Series) -> pd.Series:
    min = series.min()
    return series.fillna(min)


# function to impute NaNs with max value
def impute_max(series: pd.Series) -> pd.Series:
    max = series.max()
    return series.fillna(max)
