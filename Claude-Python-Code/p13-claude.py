import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('iowa-electricity.csv')

# Convert the 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Create a line chart
plt.figure(figsize=(12, 6))
for source in data['source'].unique():
    source_data = data[data['source'] == source]
    plt.plot(source_data['year'], source_data['net_generation'], label=source)

plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Iowa Electricity Net Generation by Source')
plt.legend()
plt.show()