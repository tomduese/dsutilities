def rename_columns(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df

# Define function for calculating adjusted r-squared
def adjusted_r_squared(r_squared, X):
    adjusted_r2 = 1 - ((1 - r_squared) * (len(X) - 1) / (len(X) - X.shape[1] - 1))
    return adjusted_r2 