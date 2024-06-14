import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
data = pd.read_csv('myfile.csv')

# Extract columns A and B
categories = data['A']
values = data['B']

# Define a sequential color palette based on column B values
cmap = sns.color_palette("viridis", as_cmap=True)

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=cmap(values))
plt.title('Pie Chart with Sequential Color Palette')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show plot
plt.show()
