import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('myfile.csv')

# Sort the DataFrame by column B in descending order
df_sorted = df.sort_values(by='B', ascending=False)

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(df_sorted['B'], labels=df_sorted['A'], startangle=90, counterclock=False, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart of Column B Sorted by Column A')
plt.show()
