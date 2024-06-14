import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('myfile.csv')

# Extract data for pie chart
labels = df['A']
sizes = df['B']

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Make labels bold
for label in plt.gca().get_xticklabels():
    label.set_fontweight('bold')

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart with Bold Labels')
plt.show()
