import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('iowa-electricity.csv')

# Convert 'year' column to datetime type
data['year'] = pd.to_datetime(data['year'])

# Group data by 'source'
grouped_data = data.groupby('source')

# Plot each group
plt.figure(figsize=(10, 6))
for name, group in grouped_data:
    plt.plot(group['year'], group['net_generation'], marker='s', linestyle='-', color='green', label=name)

# Add legend, title, and labels
plt.legend()
plt.title('Net Generation by Source in Iowa')
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.grid(True)

# Show plot
plt.show()
