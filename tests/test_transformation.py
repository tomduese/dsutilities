#import the libraries we use
import pytest
from pandas.testing import assert_series_equal
from pandas.testing import assert_frame_equal
#import the python file we want to test (* means all in that file)
from src.data_pipeline.transformation import *


#write the pytest with parametrization and test_<function_name> as name
@pytest.mark.parametrize("input_series, expected_result", [
    (pd.Series([1, 2, 3, 2.5, 4]), pd.Series([0, 0, 1, 0, 1])),
    (pd.Series([]), pd.Series([])),
    (pd.Series([10, 10, 10, 10]), pd.Series([0, 0, 0, 0]))
])
def test_is_greater_than_average(input_series, expected_result):
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_result)
    assert  type(output_series) is pd.Series

# you can skip tests if you don't want to run
@pytest.mark.skip(reason="it fails")
def test_is_greater_than_average_with_nan():
    input_series = pd.Series([1,2,np.nan])
    expected_series = pd.Series([0,1,np.nan]) # or exception
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_series)
    
#or you can use the xfail marker to indicate that you expect a test to fail
@pytest.mark.xfail
def test_is_greater_than_average_with_nan():
    input_series = pd.Series([1,2,np.nan])
    expected_series = pd.Series([0,1,np.nan]) # or exception
    output_series = is_greater_than_average(series=input_series)
    assert_series_equal(output_series, expected_series)
    
#write the pytest with parametrization and test_<function_name> as name
#here we are testing if two pandas DataFrames are equal and if there type is correct
@pytest.mark.parametrize("input_frame, expected_result", [
    (pd.DataFrame({'brand': ['Abercrombie', 'Abercrombie', 'Abercrombie', 'Abercrombie'], 
              'menWomen': ['men', 'men', 'women', 'women'], 
              'size_greater_than_average': [1,1,0,1]}), 
     pd.DataFrame({'brand': ['Abercrombie', 'Abercrombie'], 
              'menWomen': ['men', 'women'], 
              'size_greater_than_average': [2,1]})),
    (pd.DataFrame({'brand': ['Abercrombie', 'Calvin Klein', 'Abercrombie', 'Abercrombie'], 
              'menWomen': ['men', 'men', 'women', 'women'], 
              'size_greater_than_average': [1,1,0,0]}), 
     pd.DataFrame({'brand': ['Abercrombie', 'Abercrombie','Calvin Klein'], 
              'menWomen': ['men', 'women','men'], 
              'size_greater_than_average': [1,0,1]}))
    
])
def test_is_greater_than_average(input_frame, expected_result):
    output_frame = get_sum_score_by_brand_and_gender(input_frame, "brand", "menWomen", "size_greater_than_average")
    assert_frame_equal(output_frame, expected_result)
    assert  type(output_frame) is pd.DataFrame