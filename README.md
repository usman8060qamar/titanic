
Data Cleaning and Analysis Project

This project is designed to clean and analyze data from a CSV file. It includes functions for loading data, checking for missing values, and filling missing values using different strategies. The project is split into three main Python files:

- main.py: The main script that runs the data cleaning and analysis process.
- analysis.py: Contains functions for performing data analysis, such as calculating the mean of a column.
- data_processing.py: Contains functions for data manipulation, such as loading the data and filling missing values.

Project Structure

.
├── main.py
├── analysis.py
├── data_processing.py
└── train.csv

1. main.py
The main script that orchestrates the entire process. It performs the following tasks:
- Loads the data from a CSV file (train.csv).
- Checks for missing values in the data.
- Fills missing values in the Age, Cabin, and Embarked columns.
- Prints the number of missing values before and after the cleaning process.
- Displays the first 20 rows of the cleaned data.

2. analysis.py
Contains a function to calculate the mean (average) value of a specified column in the dataset.
- calculate_mean(df, column_name): This function calculates and returns the mean value of a given column in the DataFrame.

3. data_processing.py
Contains functions for data manipulation and cleaning. It provides the following functionality:
- load_data(file_path): Loads the data from a CSV file and returns it as a pandas DataFrame.
- check_null_values(df): Returns the count of missing (null) values for each column in the DataFrame.
- fill_missing_values(df, column_name, value): Fills missing values in a specified column with a given value.
- fill_forward(df, column_name): Fills missing values in a column using forward filling (replaces missing values with the previous valid value).

Requirements
To run this project, you need to install the following Python packages:
- pandas: For data manipulation and analysis.

You can install the required packages using pip:

pip install pandas

How to Use

1. Clone the repository or download the project files.
2. Place your CSV file (train.csv) in the project directory.
3. Run main.py to load the data, check for missing values, clean the data, and display the results.

Example command to run main.py:

python main.py

Example Output
Missing values before cleaning:
Age            100
Cabin          200
Embarked       10
dtype: int64

Missing values after cleaning:
Age            0
Cabin          0
Embarked       0
dtype: int64

Cleaned Data:
   PassengerId  Age    Cabin  Embarked  ...
0            1   22  Unknown cabin      C  ...
1            2   38  Unknown cabin      Q  ...
...

License
This project is licensed under the MIT License - see the LICENSE file for details.
