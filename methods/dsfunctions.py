def rename_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df
