import pandas as pd


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


import re

def clean_columnnames(df):
    df.columns = [re.sub(r'\W', '', col.lower().replace(' ', '_').lstrip('0123456789_')) for col in df.columns]
    return df
