
# Task 1: Load and Explore the Dataset
# We’ll load the Iris dataset using sklearn, display the first few rows, inspect the data types, and handle missing values.

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
iris = load_iris()

# Convert to pandas DataFrame for easier manipulation
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Display the first few rows of the dataset
print(df.head())

# Explore the data types and check for missing values
print(df.info())
print(df.isnull().sum())  # Check for missing values

# Clean the dataset by dropping rows with missing values (if any)
df_cleaned = df.dropna()

# # Alternatively, you can fill missing values (if necessary) using df.fillna(value)
# Explanation:
# Loading the dataset: The load_iris() function loads the Iris dataset, which is already split into features (iris.data) and labels (iris.target). We combine them into a DataFrame.
# Displaying the data: df.head() shows the first 5 rows of the dataset.
# Checking for missing values: df.isnull().sum() helps to check if there are any missing values in the dataset.

# Task 2: Basic Data Analysis
# In this step, we compute basic statistics and perform group-based analysis.
# # Compute basic statistics of the numerical columns
print(df.describe())

# Perform grouping by the 'species' column and compute the mean of numerical columns
grouped = df.groupby('species').mean()
print(grouped)

# Look for patterns: For example, which species has the highest average sepal length
max_sepal_length_species = grouped['sepal length (cm)'].idxmax()
print(f"Species with highest average sepal length: {max_sepal_length_species}")

# #Task 3: Data Visualization
# Now, we’ll create four types of visualizations: a line chart, bar chart, histogram, and scatter plot. We will use matplotlib and seaborn for this task.

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

# 1. Line Chart (Trends over time, for example, a time-series of sales data)
# For the Iris dataset, we don't have a time column, so we'll demonstrate it using the sepal length
plt.figure(figsize=(10, 6))
sns.lineplot(x=range(len(df)), y=df['sepal length (cm)'])
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# 2. Bar Chart (Comparison of average petal length per species)
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 3. Histogram (Distribution of sepal lengths)
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot (Relationship between sepal length and petal length)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', data=df, hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# #Explanation:
# #Line Chart: We plot the sepal length across all records to visualize any trend. The X-axis represents the index, and the Y-axis represents sepal length.
# Bar Chart: We show the average petal length per species using a barplot.
# Histogram: A histogram of the sepal length column to visualize its distribution.
# Scatter Plot: A scatter plot to visualize the relationship between sepal length and petal length, with color coding by species.
# Error Handling
# To handle potential errors during the data reading or processing steps, you can use a try-except block.

try:
    # Load the dataset
    df = pd.read_csv('path/to/your/dataset.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("No data in the file. Please check the file contents.")
except Exception as e:
    print(f"An error occurred: {e}")
# This will ensure that your program can handle common issues like missing files or incorrect data.

# Summary of Steps:
# Task 1: We loaded the dataset, explored its structure, and handled missing values.
# Task 2: We performed basic statistics and grouped the data by a categorical feature to identify patterns.
# Task 3: We created four visualizations to analyze the dataset in a more graphical format.
# Error Handling: We used try-except to handle common file reading errors.
# With this approach, you’ve completed the tasks of loading, cleaning, analyzing, and visualizing data in Python using pandas, matplotlib, and seaborn!



