import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(file_path)

def check_null_values(df):
    """
    Check for missing values in the DataFrame.
    
    Args:
    df (pd.DataFrame): The DataFrame to check for null values.

    Returns:
    pd.Series: Count of missing values per column.
    """
    return df.isnull().sum()

def fill_missing_values(df, column_name, fill_value):
    """
    Fill missing values in a specified column with a given value.
    
    Args:
    df (pd.DataFrame): The DataFrame to fill missing values in.
    column_name (str): The column to fill.
    fill_value: The value to fill in.

    Returns:
    pd.DataFrame: The DataFrame with missing values filled.
    """
    df[column_name].fillna(fill_value, inplace=True)
    return df

def fill_forward(df, column_name):
    """
    Fill missing values in a specified column using forward fill.
    
    Args:
    df (pd.DataFrame): The DataFrame to fill missing values in.
    column_name (str): The column to forward fill.

    Returns:
    pd.DataFrame: The DataFrame with missing values filled using forward fill.
    """
    df[column_name].fillna(method="ffill", inplace=True)
    return df
