def dataframe_insights(df):
    """
    Generate insights for a given DataFrame:
    - Missing values (total and percentage)
    - Data types of columns
    - Number of unique values in each column
    - Top 5 most common values for each column (if column is non-numeric)

    :param df: Input DataFrame
    """
    total_rows = len(df)

    print("Column Insights:")
    print("============================================")

    for col in df.columns:
        print(f"Column: {col}")
        print("----------------------------------------")

        # Missing values (total and percentage)
        missing_values = df[col].isna().sum()
        missing_percentage = (missing_values / total_rows) * 100
        print(f"Missing Values: {missing_values} ({missing_percentage:.2f}%)")

        # Data type
        dtype = df[col].dtype
        print(f"Data Type: {dtype}")

        # Number of unique values
        unique_values = df[col].nunique()
        print(f"Unique Values: {unique_values}")

        # Top 5 most common values (if column is non-numeric)
        if pd.api.types.is_object_dtype(dtype):
            top_values = df[col].value_counts().head(5)
            print("Top 5 Most Common Values:")
            print(top_values)

        print("============================================")

def nice_summary(df):
    """
    Generate a DataFrame that contains all of:
        - .info()
        - .nunique()
        - .isnull() amount
        - .isnull() percentage
        - zero value amount
        - .describe()

    Args:
        df: input DataFrame

    Returns:
        DataFrame: 14 informational columns. Input DF columns as rows.
    """
    return pd.concat([    
                pd.DataFrame({
                'Dtype': df.dtypes,
                'nunique': df.nunique(),
                'Non-Null Count': df.count(),
                'Missing': df.isnull().sum(),        
                'Missing %': round((df.isnull().sum()/df.shape[0])*100, 2),
                'Zero Count': (df == 0).sum(),
                })
                ,df.describe().round(2).T.iloc[:,1:]
            ], axis=1) \
            .fillna('-') \
            .reset_index() \
            .rename(columns={'index': 'Columns'}) \
            .replace({'Missing': 0, 'Missing %': 0}, '-')