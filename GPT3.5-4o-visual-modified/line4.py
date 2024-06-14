import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv('iowa-electricity.csv')

# Convert 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Group data by 'source'
grouped_data = data.groupby('source')

# Plotting
plt.figure(figsize=(10, 6))

for name, group in grouped_data:
    plt.plot(group['year'], group['net_generation'], marker='o', linestyle='-', label=name)

plt.title('Net Generation Over Time by Source')
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
