# main.py
import pandas as pd
from data_processing import load_data, check_null_values, fill_missing_values, fill_forward
from analysis import calculate_mean

# Load the data
file_path = "train.csv"
df = load_data(file_path)

# Check for missing values
print("Missing values before cleaning:")
print(check_null_values(df))

# Fill missing values
mean_age = calculate_mean(df, "Age")
df = fill_missing_values(df, "Age", mean_age)
df = fill_missing_values(df, "Cabin", "Unknown cabin")
df = fill_forward(df, "Embarked")

# Check missing values after filling
print("Missing values after cleaning:")
print(check_null_values(df))

# Final output
print("Cleaned Data:")
print(df.head(20))
