import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'iowa-electricity-extended.csv'
data = pd.read_csv(file_path)

# Convert the 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'])

# Extract the necessary columns
years = data['year']
sources = data['source']
net_generation = data['net_generation']
consumption = data['consumption']

# Scale down the consumption values for smaller triangles
scaled_consumption = consumption / 10  # Adjust the divisor to change the size

# Create a figure and axis
fig, ax = plt.subplots()

# Define a scatter plot with triangles and size based on scaled 'consumption'
scatter = ax.scatter(years, net_generation, s=scaled_consumption, c=sources.astype('category').cat.codes, 
                     alpha=0.6, marker='^', cmap='viridis')

# Adding a legend for the sources
handles, labels = scatter.legend_elements(prop="colors", alpha=0.6)
source_legend = ax.legend(handles, sources.astype('category').cat.categories, title="Source")

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Net Generation')
ax.set_title('Bubble Chart of Net Generation vs. Year with Consumption-based Sizes')

# Display the plot
plt.show()
