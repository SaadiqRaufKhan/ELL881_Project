import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('myfile.csv')

# Sort values by column B in descending order
df = df.sort_values(by='B', ascending=False)

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(df['B'], labels=None, startangle=90, counterclock=False, autopct='%1.1f%%', pctdistance=0.85)
plt.legend(df['A'], loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.subplots_adjust(left=0.1, right=0.7)  # Adjusting to fit legend outside the pie chart
plt.show()
