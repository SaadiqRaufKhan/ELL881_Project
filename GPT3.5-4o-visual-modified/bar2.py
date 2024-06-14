# attempts: 1

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('myfile.csv')

# Extract columns A and B
categories = data['A']
values = data['B']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='lightgreen')

# Add title and labels
plt.title('Bar Chart from myfile.csv')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()
