import pandas as pd
from data_processing import load_data, check_null_values, fill_missing_values, fill_forward
from analysis import calculate_mean
from constants import (TRAIN_CSV_PATH, DEFAULT_CABIN_VALUE, AGE_COLUMN, CABIN_COLUMN, EMBARKED_COLUMN,PRINT_MISSING_VALUES)

# Load the data
df = load_data(TRAIN_CSV_PATH)

# Check for missing values
if PRINT_MISSING_VALUES:
    print("Missing values before cleaning:")
    print(check_null_values(df))

# Fill missing values
mean_age = calculate_mean(df, AGE_COLUMN)
df = fill_missing_values(df, AGE_COLUMN, mean_age)
df = fill_missing_values(df, CABIN_COLUMN, DEFAULT_CABIN_VALUE)
df = fill_forward(df, EMBARKED_COLUMN)

# Check missing values after filling
if PRINT_MISSING_VALUES:
    print("Missing values after cleaning:")
    print(check_null_values(df))

# Final output
print("Cleaned Data:")
print(df.head(20))
