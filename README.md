
# Titanic Data Cleaning and Analysis Project

This project focuses on cleaning and analyzing the Titanic dataset using Python and Pandas. It is designed with a modular approach, where different functionalities are separated into distinct files for better code organization. The project also includes a constants file for managing fixed values and setup instructions for creating a Python virtual environment.

---

## **Project Structure**

```
project/
│
├── constants.py         # Centralized file for constants
├── data_processing.py   # Functions for loading and cleaning data
├── analysis.py          # Functions for data analysis
├── main.py              # Main script to run the project
├── requirements.txt     # Dependencies for the project
└── README.md            # Documentation
```

---

## **Features**

- **Centralized Constants**: 
  - All fixed values (e.g., file paths, default values, and column names) are stored in a single `constants.py` file.

- **Load and Clean Data**: 
  - Load data from a CSV file.
  - Check for missing values.
  - Fill missing values using specified methods (e.g., mean, forward fill).

- **Analyze Data**: 
  - Calculate the mean for specific columns.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**

Clone the project repository to your local machine:
```bash
git clone <repository-url>
cd <repository-folder>
```

### **Step 2: Create a Virtual Environment**

Create a Python virtual environment to isolate project dependencies:
```bash
python -m venv env
```

### **Step 3: Activate the Virtual Environment**

#### On Windows:
```bash
.\env\Scripts\activate
```
If you encounter an error like `running scripts is disabled`, temporarily bypass the execution policy:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\env\Scripts\activate
```

#### On macOS/Linux:
```bash
source env/bin/activate
```

### **Step 4: Install Dependencies**

Install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **Step 5: Run the Project**

Execute the `main.py` script to clean and analyze the dataset:
```bash
python main.py
```

---

## **Dependencies**

The project uses the following Python library:
- `pandas` (version 1.5.3)

Dependencies are managed through the `requirements.txt` file. To install them, use:
```bash
pip install -r requirements.txt
```

---

## **How It Works**

1. **Load Data**:
   - The script reads the Titanic dataset from a CSV file (`train.csv`).

2. **Clean Data**:
   - Missing values are identified and filled using:
     - Mean for numerical columns (e.g., `Age`).
     - Default values for categorical columns (e.g., `Cabin`).
     - Forward-fill for sequential data (e.g., `Embarked`).

3. **Centralized Constants**:
   - Fixed values such as file paths, column names, and default values are managed in `constants.py`. This ensures easy modification and better code organization.

4. **Analyze Data**:
   - The script calculates the mean of specific columns for insights.

5. **Output Results**:
   - Displays cleaned data and missing values summary.

---

## **Troubleshooting**

### **Script Activation Error on Windows**
If you encounter an error like:
```
File cannot be loaded because running scripts is disabled on this system.
```
Run the following command in PowerShell:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### **Missing Dependencies**
If a required library is missing, ensure you have installed all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **License**
This project is licensed under the MIT License.

---

## **Contributions**
Contributions are welcome! Feel free to submit a pull request or report issues.

---

## **Contact**
For any questions or feedback, please contact:
- **Name**: Usman Qamar
- **Email**: [your-email@example.com]
