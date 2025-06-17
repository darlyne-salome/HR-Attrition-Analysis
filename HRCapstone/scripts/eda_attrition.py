import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('C:/Users/darly/OneDrive/Documents/HRCapstone/data/employee_data.csv')

# Clean column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

print("Data loaded successfully.")
print(df.head())

# Plot example
sns.countplot(x='attrition', data=df)
plt.title('Attrition Distribution')

# Save to path
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_distribution.png')

plt.show()

# Quick summary
print("Basic Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nAttrition value counts:")
print(df['attrition'].value_counts())

# Visualize attrition count
sns.countplot(data=df, x='attrition')
plt.title('Attrition Distribution')
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_distribution.png')
plt.show()

# Clear the previous figure
plt.clf()

# Overtime vs Attrition
sns.countplot(x='overtime', hue='attrition', data=df, palette='Set2')
plt.title('Attrition by Overtime Status')
plt.xlabel('Overtime')
plt.ylabel('Number of Employees')
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_by_overtime.png')
plt.show()

# Clear the previous figure
plt.clf()

# Plot: Job Role vs Attrition
plt.figure(figsize=(12, 6))
sns.countplot(x='jobrole', hue='attrition', data=df, palette='pastel')
plt.title('Attrition by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()  # Prevent label overlap
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_by_jobrole.png')
plt.show()

# Clear the previous figure
plt.clf()

# Plot: Monthly Income vs Attrition
plt.figure(figsize=(8, 6))
sns.boxplot(x='attrition', y='monthlyincome', data=df, palette='coolwarm')
plt.title('Monthly Income Distribution by Attrition Status')
plt.xlabel('Attrition')
plt.ylabel('Monthly Income')
plt.tight_layout()
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/monthlyincome_vs_attrition.png')
plt.show()

# Clear the previous figure
plt.clf()

# Create age groups
df['age_group'] = pd.cut(df['age'], bins=[17, 25, 35, 45, 55, 65],
                         labels=['18–25', '26–35', '36–45', '46–55', '56–65'])

# Plot: Attrition by Age Group
plt.figure(figsize=(8, 6))
sns.countplot(x='age_group', hue='attrition', data=df, palette='Set3')
plt.title('Attrition by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_by_age_group.png')
plt.show()

# Clear the previous figure
plt.clf()

# Plot: Years at Company vs Attrition
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='yearsatcompany', hue='attrition', multiple='stack', bins=15, palette='muted')
plt.title('Attrition by Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.savefig('C:/Users/darly/OneDrive/Documents/HRCapstone/output/attrition_by_yearsatcompany.png')
plt.show()



