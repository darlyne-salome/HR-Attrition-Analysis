import pandas as pd

# Loading the CSV 
df = pd.read_csv("C:/Users/darly/OneDrive/Documents/HRCapstone/employee_data.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Show the first 5 rows
print("First 5 rows:")
print(df.head())

# Check for missing values
print("\n Missing values per column:")
print(df.isnull().sum())

# Check column names
print("\n Columns:")
print(df.columns)


