import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('myfile.csv')

# Ensure the column names match your CSV file's columns
categories = df['A']
values = df['B']

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(values, labels=categories, autopct='%1.1f%%', textprops={'weight': 'bold'})

# Set the title of the pie chart
plt.title('Pie Chart of Categories in Bold Labels', weight='bold')

# Show the pie chart
plt.show()
