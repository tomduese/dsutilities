# import the libraries we use
import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_series_equal

# import the python file we want to test
from src.data_pipeline.imputation import impute, impute_max, impute_min


# write the pytest with parametrization and test_<function_name> as name
@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 2.0, 3.0])),
        (pd.Series([1, 2, 3, np.nan, 4, np.nan]), pd.Series([1, 2, 3, 2.5, 4, 2.5])),
    ],
)
def test_impute(input_series, expected_result):
    assert_series_equal(impute(input_series), expected_result)


# add the tests for imputing min and max
@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 3.0, 3.0])),
        (pd.Series([1, 2, 3, np.nan, 4, np.nan]), pd.Series([1, 2, 3, 4, 4, 4.0])),
    ],
)
def test_impute_max(input_series, expected_result):
    assert_series_equal(impute_max(input_series), expected_result)


@pytest.mark.parametrize(
    "input_series, expected_result",
    [
        (pd.Series([1.0, np.nan, 3.0]), pd.Series([1.0, 1.0, 3.0])),
        (pd.Series([1, 2, 3, np.nan, 4, np.nan]), pd.Series([1, 2, 3, 1, 4, 1.0])),
    ],
)
def test_impute_min(input_series, expected_result):
    assert_series_equal(impute_min(input_series), expected_result)
