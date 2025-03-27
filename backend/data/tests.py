import pandas as pd
import numpy as np

from preprocessing import (
    DataPreProcessingBuilder,
    NullData,
    RemoveDuplicates,
    ConversiontoFloats,
    WhitespaceCleaner,
    DropColumn,
)


def test_null_data():
    """Test that NullData drops rows containing NaN values."""
    df = pd.DataFrame({"A": [1, np.nan, 2], "B": [3, 4, 5]})
    processor = NullData()
    result = processor.process(df)
    expected = pd.DataFrame({"A": [1.0, 2.0], "B": [3.0, 5.0]}, index=[0, 2])
    pd.testing.assert_frame_equal(result, expected)


def test_remove_duplicates():
    """Test that RemoveDuplicates removes duplicate rows."""
    df = pd.DataFrame({"A": [1, 1, 2], "B": [3, 3, 4]})
    processor = RemoveDuplicates()
    result = processor.process(df)
    expected = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=[0, 2])
    pd.testing.assert_frame_equal(result, expected)


def test_conversion_to_floats():
    """Test that ConversiontoFloats converts all columns to float."""
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    processor = ConversiontoFloats()
    result = processor.process(df)
    # Check that each column's dtype is float
    assert all(result.dtypes == float)


def test_whitespace_cleaner():
    """Test that WhitespaceCleaner strips leading and trailing whitespace from a string."""
    processor = WhitespaceCleaner()
    input_str = "  hello world  "
    result = processor.process(input_str)
    expected = "hello world"
    assert result == expected


def test_drop_column():
    """Test that DropColumn removes a specified column from the DataFrame."""
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    processor = DropColumn("B")
    result = processor.process(df)
    expected = pd.DataFrame({"A": [1, 2]})
    pd.testing.assert_frame_equal(result, expected)


def test_data_preprocessing_builder():
    """
    Test that the DataPreProcessingBuilder correctly chains operations.
    We'll chain null_data() and remove_duplicates() for simplicity.
    """
    df = pd.DataFrame({"A": [1, np.nan, 1], "B": [3, 4, 3]})

    builder = DataPreProcessingBuilder()
    pipeline = builder.load_df(df).null_data().remove_duplicates().build()
    result = pipeline.clean()

    # After dropping NaN, we have rows [0, 2].
    # Then removing duplicates keeps row [0] and drops row [2].
    expected = pd.DataFrame({"A": [1.0], "B": [3.0]}, index=[0])
    pd.testing.assert_frame_equal(result, expected)
