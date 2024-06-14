import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a DataFrame
df = pd.read_csv('myfile.csv')

# Sort DataFrame by column B (quantitative)
df_sorted = df.sort_values(by='B')

# Extracting column A and column B
categories = df_sorted['A']
quantities = df_sorted['B']

# Plotting a pie chart
plt.figure(figsize=(8, 8))
plt.pie(quantities, labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart Sorted by Column B')
plt.show()
