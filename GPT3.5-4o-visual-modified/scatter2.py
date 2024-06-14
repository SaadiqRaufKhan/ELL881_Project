import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("iowa-electricity-extended.csv")

# Convert the 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'])

# Normalize the 'consumption' values for alpha (opacity) between 0 and 1
data['consumption_normalized'] = (data['consumption'] - data['consumption'].min()) / (data['consumption'].max() - data['consumption'].min())

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
        subset['year'], 
        subset['net_generation'], 
        s=50,  # Fixed size for visibility
        c=source_colors.get(source, 'grey'),  # Default to grey if source not found
        alpha=subset['consumption_normalized'],  # Set opacity based on normalized consumption
        label=source
    )

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Net Generation vs Year with Consumption-based Opacity')
plt.legend(title='Source')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
