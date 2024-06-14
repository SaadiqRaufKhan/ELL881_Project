import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('myfile.csv')

# Sort the data based on the quantitative values in descending order
data_sorted = data.sort_values(by='B', ascending=False)

# Extract the categories and quantities
categories = data_sorted['A']
quantities = data_sorted['B']

# Create the pie chart
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    quantities,
    startangle=90,
    counterclock=False,
    autopct='%1.1f%%',
    pctdistance=1.15,
    wedgeprops=dict(width=0.3)
)

# Remove the default labels (categories)
for text in texts:
    text.set_text('')

# Style the pie chart
plt.setp(autotexts, size=10, weight='bold', color='black')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Add a legend with categories
ax.legend(wedges, categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Show the plot
plt.show()
