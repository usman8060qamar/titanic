# analysis.py
import pandas as pd

def calculate_mean(df, column_name):
    """
    Calculate the mean of a given column in the DataFrame.
    Args:
    df (pd.DataFrame): The DataFrame to calculate the mean for.
    column_name (str): The column name for which to calculate the mean.

    Returns:
    float: The mean of the column.
    """
    return df[column_name].mean()
