import pandas as pd
import numpy as np
import re


def rename_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def drop_duplicates(df):
    # check how many duplicated rows exist in the data frame
    if df.duplicated().value_counts()["True"] > 0:
        # remove duplicates
        df = df.drop_duplicates()
        # reset index inplace
        df.reset_index(inplace=True, drop=True)
    df.head(5)
    return df


def clean_columnnames(df):
    df.columns = [
        re.sub(r"\W", "", col.lower().replace(" ", "_").lstrip("0123456789_"))
        for col in df.columns
    ]
    return df


def check_for_missing_values(df):
    """
    This function takes a pandas DataFrame as input and returns a DataFrame containing the number and percentage
    of missing values in each column of the input DataFrame.

    Parameters:
        df (pandas.DataFrame): A pandas DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame containing the number and percentage of missing values in each column of
        the input DataFrame.
    """
    missing = pd.DataFrame(df.isnull().sum(), columns=["Amount"])
    missing["Percentage"] = round((missing["Amount"] / df.shape[0]) * 100, 2)
    missing[missing["Amount"] != 0]
    return missing


def load_carseats():
    df = pd.read_csv("dsutilities/data/carseats.csv")
    df = clean_columnnames(df)
    shelveloc_dummies = pd.get_dummies(df.shelveloc, prefix="selveloc", drop_first=True)
    df.drop(["shelveloc"], axis=1, inplace=True)
    df = pd.concat([df, shelveloc_dummies], axis=1)
    df = clean_columnnames(df)
    df.urban.replace({"Yes": 1, "No": 0}, inplace=True)
    df.us.replace({"Yes": 1, "No": 0}, inplace=True)
    df.urban.astype(np.int16)
    df.us.astype(np.int16)
    return df
