import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('myfile.csv')

# Extract data from columns A and B
categories = df['A']
quantities = df['B']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(quantities, labels=categories, autopct='%1.1f%%')
plt.title('Pie')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()
