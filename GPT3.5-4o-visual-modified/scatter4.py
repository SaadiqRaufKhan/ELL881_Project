import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
data = pd.read_csv('iowa-electricity-extended.csv')

# Convert 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Define color map for different sources
color_map = {
    'Nuclear Energy': 'purple', 
    'Renewables': 'orange',
    'Fossil Fuels': 'brown'
}

# Plot scatterplot
plt.figure(figsize=(10, 6))
for source, group in data.groupby('source'):
    sizes = group['consumption']/100  # Calculate sizes for each group
    plt.scatter(group['year'], group['net_generation'], s=sizes, c=color_map[source], label=source, alpha=0.7)

# Add labels and legend
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Net Generation vs. Year')
plt.legend(title='Source')

# Show plot
plt.grid(True)
plt.show()
