import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.markers as mmarkers

# Load the data
file_path = 'iowa-electricity-extended.csv'
data = pd.read_csv(file_path)

# Convert 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Define marker styles for different sources
source_to_marker = {
    'Fossil Fuels': 'o',
    'Renewables': '*',
    'Nuclear Energy': '^',
    'Other': 'X'
}

# Extract the unique sources
unique_sources = data['source'].unique()

# Plotting
plt.figure(figsize=(12, 8))

for source in unique_sources:
    subset = data[data['source'] == source]
    plt.scatter(subset['year'], subset['net_generation'],
                s=subset['consumption'] / 300,  # Adjust size for better visualization
                marker=source_to_marker.get(source, 'o'),
                label=source,
                alpha=1)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Iowa Electricity Generation and Consumption')
plt.legend(title='Source')
plt.grid(True)
plt.show()