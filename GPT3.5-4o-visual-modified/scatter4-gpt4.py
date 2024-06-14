import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.markers as mmarkers

# Read the CSV file
df = pd.read_csv('iowa-electricity-extended.csv')

# Convert 'year' to datetime
df['year'] = pd.to_datetime(df['year'])

# Define marker shapes for each source
source_markers = {
    'Fossil Fuels': 'o',
    'Renewables': '*',
    'Nuclear Energy': '^',
    'Other': '*',        # Star
}

# Create the scatter plot
fig, ax = plt.subplots()

for source, marker in source_markers.items():
    # Filter data for the current source
    source_data = df[df['source'] == source]
    
    # Plot data
    scatter = ax.scatter(
        source_data['year'], 
        source_data['net_generation'], 
        s=source_data['consumption']/100,  # Size of points
        label=source,
        marker=marker,
        alpha=0.7
    )

# Add legend, labels, and title
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Net Generation')
ax.set_title('Net Generation vs. Year with Consumption-based Point Sizes')

# Show plot
plt.show()
