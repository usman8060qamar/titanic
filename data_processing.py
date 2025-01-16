# data_processing.py
import pandas as pd

# data_processing.py
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)


def check_null_values(df):
    """
    Check and return the number of null values in each column of the DataFrame.
    Args:
    df (pd.DataFrame): The DataFrame to check.

    Returns:
    pd.Series: Series with null counts for each column.
    """
    return df.isnull().sum()

def fill_missing_values(df, column_name, value):
    """
    Fill missing values in a specific column with the given value.
    Args:
    df (pd.DataFrame): The DataFrame in which to fill missing values.
    column_name (str): The column name where missing values need to be filled.
    value: The value to fill missing values with.

    Returns:
    pd.DataFrame: DataFrame with filled missing values.
    """
    df[column_name].fillna(value, inplace=True)
    return df

def fill_forward(df, column_name):
    """
    Fill missing values in a column using forward fill method.
    Args:
    df (pd.DataFrame): The DataFrame to apply forward fill.
    column_name (str): The column name where missing values need to be filled using forward fill.

    Returns:
    pd.DataFrame: DataFrame with forward-filled missing values.
    """
    df[column_name].fillna(method="ffill", inplace=True)
    return df
