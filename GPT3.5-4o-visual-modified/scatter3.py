import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("iowa-electricity-extended.csv")

# Convert the 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'])

# Normalize the 'year' values to use for point sizes
# Here, we use the year part only and normalize it for better visual scaling
data['year_numeric'] = data['year'].dt.year
year_min = data['year_numeric'].min()
year_max = data['year_numeric'].max()
data['year_normalized'] = (data['year_numeric'] - year_min) / (year_max - year_min)

# Define colors for each source
source_colors = {
    'Nuclear Energy': 'purple', 
    'Renewables': 'orange',
    'Fossil Fuels': 'brown'
}

# Create a scatterplot
plt.figure(figsize=(10,6))
for source in data['source'].unique():
    subset = data[data['source'] == source]
    plt.scatter(
        subset['net_generation'], 
        subset['consumption'], 
        s=subset['year_normalized'] * 1000,  # Scale the size for visibility
        c=source_colors.get(source, 'grey'),  # Default to grey if source not found
        alpha=0.6,  # Set a fixed transparency for better visual distinction
        label=source
    )

# Add labels and legend
plt.xlabel('Net Generation')
plt.ylabel('Consumption')
plt.title('Net Generation vs Consumption with Year-based Point Sizes')
plt.legend(title='Source')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
