import pandas as pd
import matplotlib.pyplot as plt
import random

# Load the data from the CSV file
data = pd.read_csv('myfile.csv')

# Extract columns A and B
categories = data['A']
values = data['B']

# Generate random colors for each bar
colors = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(len(categories))]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=colors)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Different Colored Bars')

# Show the plot
plt.show()
