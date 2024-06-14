import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('myfile.csv')

# Group by the categorical column and sum the quantitative column
grouped_data = df.groupby('A')['B'].sum()

# Plotting
plt.figure(figsize=(8, 8))

# Create a donut chart
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.6, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.title('Donut Chart')

# Display the chart
plt.show()
