import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# We will use the Iris Dataset 
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# Now we will clean the dataset
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
# Remove duplicate records
df.drop_duplicates(inplace=True)
print("\nNumber of rows after removing duplicates:", len(df))
# Detect outliers in numerical columns using the IQR method
numerical_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for col in numerical_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    # Define outliers as points outside 1.5 * IQR
    outliers = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))

    # Remove outliers
    df = df[~outliers]

print("\nNumber of rows after removing outliers:", len(df))

# Now we will standardize the data
df['species'] = df['species'].str.lower()
df['species'] = df['species'].replace({'setosa': 'setosa', 'versicolor': 'versicolor', 'virginica': 'virginica'})
print("\nUnique values in 'species':", df['species'].unique())

# Use Exploratory Data Analysis (EDA)
# Univariate Analysis
print("\nSummary statistics for numerical columns:")
print(df.describe())
print("\nFrequency distribution for 'species':")
print(df['species'].value_counts())

plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], bins=30, kde=True)
plt.title('Distribution of Sepal Length')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x=df['petal_width'])
plt.title('Box Plot of Petal Width')
plt.show()

# Bivariate Analysis
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df)
plt.title('Scatter Plot: Sepal Length vs Sepal Width')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Petal Length by Species')
plt.show()

plt.figure(figsize=(8, 6))
sns.violinplot(x='species', y='petal_width', data=df)
plt.title('Petal Width Distribution by Species')
plt.show()

# Multivariate Analysis 
sns.pairplot(df, hue='species')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

grouped = df.groupby('species')['petal_length'].mean()
grouped.plot(kind='bar', figsize=(8, 6))
plt.title('Mean Petal Length by Species')
plt.ylabel('Mean Petal Length')
plt.show()

# Save the cleaned dataset to a new CSV file
df.to_csv('DAI Assignment 23116045.csv', index=False)

