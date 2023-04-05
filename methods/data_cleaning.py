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
        column = re.sub(r"\W", "", column)  # Remove special characters
        column = re.sub(
            r"^(\d)", r"_\1", column
        )  # Add underscore if starts with a number
        return column

    # Apply the transformation to each column name
    df.columns = [clean_column_name(col) for col in df.columns]

    return df
