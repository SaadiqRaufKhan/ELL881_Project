import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('myfile.csv')

# Ensure the columns are named 'A' and 'B'
# If they are not, you can change 'A' and 'B' to the actual column names
categories = df['A']
quantities = df['B']

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, quantities, color='skyblue')

# Add labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

# Add titles and labels
plt.title('Bar Chart with Quantities on Top')
plt.xlabel('Categories')
plt.ylabel('Quantities')

# Show the plot
plt.show()
