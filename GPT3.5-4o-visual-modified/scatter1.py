import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("iowa-electricity-extended.csv")

# Convert the 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'])

# Check the unique values in the 'source' column
unique_sources = data['source'].unique()
print("Unique sources:", unique_sources)

# Define colors and markers for each source
source_colors = {
    'Nuclear Energy': 'purple', 
    'Fossil Fuels': 'yellow',
    'Renewables': 'red'
}

source_markers = {
    'Fossil Fuels': 'o',
    'Renewables': '*',
    'Nuclear Energy': '^',
    'Other': '*',        # Star
}

# Create a scatterplot
plt.figure(figsize=(10,6))
for source in unique_sources:
    subset = data[data['source'] == source]
    plt.scatter(
        subset['year'], 
        subset['net_generation'], 
        s=subset['consumption']/100, 
        c=source_colors.get(source, 'grey'),  # Default to grey if source not found
        marker=source_markers.get(source, 'o'),  # Default to circle if source not found
        label=source,
        alpha=0.7
    )

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Net Generation vs Year')
plt.legend(title='Source')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
