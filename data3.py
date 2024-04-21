import pandas as pd

# Load the dataset
file_path = "path/to/your/dataset.csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(data.head())

# Check the shape of the dataset (number of rows and columns)
print("\nDataset shape:", data.shape)

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Summary statistics of numerical columns
print("\nSummary statistics:")
print(data.describe())

# Data visualization (example: histogram of wine quality)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.hist(data['quality'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
