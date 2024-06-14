import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = 'myfile.csv'
data = pd.read_csv(file_path)

# Ensure the columns are correctly named
categorical_column = 'A'
quantitative_column = 'B'

# Extract the data for the pie chart
categories = data[categorical_column]
values = data[quantitative_column]

# Generate the pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Column A and B')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Show the plot
plt.show()
