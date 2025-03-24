import pandas as pd
import numpy as np
import pytest

# Adjust the imports below to match your project structure.
from preprocessing import (
    DataPreProcessingBuilder,
    DataPreProcessing,
    NullData,
    RemoveDuplicates,
    ConversiontoFloats,
    WhitespaceCleaner,
    DropColumn
)

# Test for NullData processor
def test_null_data():
    # Create a DataFrame with some NaN values
    df = pd.DataFrame({
        'a': [1, np.nan, 3],
        'b': [4, 5, np.nan]
    })
    processor = NullData()
    result = processor.process(df)
    # Expected: rows with any NaN values are dropped (only the first row remains)
    expected = pd.DataFrame({'a': [1.0], 'b': [4.0]}, index=[0])
    pd.testing.assert_frame_equal(result, expected)

# Test for RemoveDuplicates processor
def test_remove_duplicates():
    # Create a DataFrame with duplicate rows
    df = pd.DataFrame({
        'a': [1, 1, 2],
        'b': [3, 3, 4]
    })
    processor = RemoveDuplicates()
    result = processor.process(df)
    # Expected: the duplicate row is removed. Pandas keeps the first occurrence.
    expected = pd.DataFrame({'a': [1, 2], 'b': [3, 4]}, index=[0, 2])
    pd.testing.assert_frame_equal(result, expected)

# Test for ConversiontoFloats processor
def test_conversion_to_floats():
    # Create a DataFrame with integer data
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })
    processor = ConversiontoFloats()
    result = processor.process(df)
    # Check that the dtype of each column is float
    assert all(result.dtypes == float)

# Test for WhitespaceCleaner processor
def test_whitespace_cleaner():
    processor = WhitespaceCleaner()
    input_str = "  hello world  "
    result = processor.process(input_str)
    expected = "hello world"
    assert result == expected

# Test for DropColumn processor
def test_drop_column():
    # Create a DataFrame with multiple columns
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9]
    })
    processor = DropColumn('b')
    result = processor.process(df)
    # Expected: column 'b' is removed
    expected = pd.DataFrame({
        'a': [1, 2, 3],
        'c': [7, 8, 9]
    })
    pd.testing.assert_frame_equal(result, expected)

# Test for DataPreProcessingBuilder and DataPreProcessing integration
def test_datapreprocessing_builder():
    # Create a DataFrame that will be processed by a chain of operations
    df = pd.DataFrame({
        'a': [1, np.nan, 1, 2],
        'b': [' 3', ' 4', ' 3', ' 5']
    })

    # Build a pipeline that drops NaNs and then removes duplicates.
    # Note: We are not including the whitespace cleaning or conversion to floats in this test,
    # since the operations on different data types (strings vs. numbers) might conflict.
    builder = DataPreProcessingBuilder()
    pipeline = builder.load_df(df).null_data().remove_duplicates().build()
    
    result = pipeline.clean()
    # Expected behavior:
    # 1. Drop rows with NaNs -> leaving rows with indices [0, 2, 3]
    # 2. Remove duplicate rows -> rows 0 and 2 are duplicates so one is dropped.
    expected = df.dropna().drop_duplicates()
    pd.testing.assert_frame_equal(result, expected)

# Optional: a test that chains all processors.
# You might need to tailor the test data such that every processor works on the intended type.
def test_full_pipeline():
    # Create a DataFrame with a mix of issues:
    # - NaN values in column 'a'
    # - Duplicate rows
    # - Integers in column 'a' (to be converted to floats)
    # - Extra whitespace in column 'b'
    df = pd.DataFrame({
        'a': [1, np.nan, 1, 2],
        'b': [' 3', ' 4', ' 3', ' 5']
    })

    builder = DataPreProcessingBuilder()
    # Here, we apply the following steps:
    # 1. Drop rows with NaN (null_data)
    # 2. Remove duplicate rows (remove_duplicates)
    # 3. Convert data types to floats (to_float) on column 'a'
    # 4. Clean whitespace on a string (white_spaces) on column 'b'
    pipeline = builder.load_df(df).null_data().remove_duplicates().to_float().white_spaces().build()
    
    # Note: Since ConversiontoFloats and WhitespaceCleaner are applied to the entire DataFrame,
    # and DataFrame objects do not have a .strip() method, this full chain may raise an error.
    # In practice, you might want to apply such processors to specific columns or adjust their logic.
    with pytest.raises(AttributeError):
        # Expecting an error due to improper handling of DataFrame vs. string
        pipeline.clean()
