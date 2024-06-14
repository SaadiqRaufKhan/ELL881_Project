import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('myfile.csv')

# Sort the DataFrame by column B (quantitative) in descending order
df_sorted = df.sort_values(by='B', ascending=False)

# Extracting data for the pie chart
labels = df_sorted['A']
sizes = df_sorted['B']

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart of Column A (Categorical) sorted by Column B (Quantitative)')
plt.show()
