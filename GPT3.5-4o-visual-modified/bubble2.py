import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV file into a DataFrame
df = pd.read_csv('iowa-electricity-extended.csv')

# Convert 'year' column to datetime
df['year'] = pd.to_datetime(df['year'])

# Define a dictionary to map source to marker shape
marker_shapes = {'Coal': 'o', 'Natural Gas': 's', 'Nuclear Energy': '^', 'Renewables': 'd', 'Fossil Fuels': '*'}

# Plot the bubble chart
plt.figure(figsize=(10, 6))
for source, group in df.groupby('source'):
    plt.scatter(group['year'], group['net_generation'], s=group['consumption']/100, 
                label=source, alpha=0.7, marker=marker_shapes.get(source, 'o'))

# Customize the plot
plt.title('Iowa Electricity Generation and Consumption Over Time')
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.legend(title='Source')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
