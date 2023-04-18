import pandas as pd
from sklearn.preprocessing import StandardScaler

# scale_type can be any scaler-object from sklearn.preprocessing (scale_type= )
# MinMaxScaler()
# minmax_scale()
# MaxAbsScaler()
# StandardScaler()
# RobustScaler()
# Normalizer()
# QuantileTransformer()
# PowerTransformer()


def scale_columns(df_train, df_test, col_list=[], scale_type=StandardScaler()):
    """Takes train and test data as dataframe, scales the specified columns and returns new dataframes with transformed columns."""

    scaled_columns_train = pd.DataFrame(
        scale_type.fit_transform(df_train[col_list]),
        columns=col_list,
        index=df_train.index,
    )
    scaled_columns_test = pd.DataFrame(
        scale_type.transform(df_test[col_list]), columns=col_list, index=df_test.index
    )

    df_train_preprocessed = pd.concat(
        [scaled_columns_train, df_train.drop(col_list, axis=1)], axis=1
    )
    df_test_preprocessed = pd.concat(
        [scaled_columns_test, df_test.drop(col_list, axis=1)], axis=1
    )
    return df_train_preprocessed, df_test_preprocessed


# Example:
# scale_cols = ['age','serum_cholestoral','resting_blood_pressure','maximum_heartrate_achieved','oldpeak']

# X_train_preprocessed, X_test_preprocessed = scale_columns(X_train, X_test, scale_cols)
