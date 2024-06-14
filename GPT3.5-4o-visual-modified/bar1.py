# attempts: 1

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('myfile.csv')

# Extract columns A and B
categories = df['A']
values = df['B']

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color='skyblue')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart of Columns A and B')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
