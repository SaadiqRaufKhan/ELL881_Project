import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
data = pd.read_csv("iowa-electricity.csv")

# Convert the 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Create a list of years from the data
years = data['year'].dt.strftime('%Y-%m-%d').tolist()

# Extract unique sources
sources = data['source'].unique()

# Prepare data for radar chart
num_years = len(years)
num_sources = len(sources)

# Create a dictionary to hold net_generation values for each source
net_generation = {source: np.zeros(num_years) for source in sources}

# Populate the net_generation dictionary with data from the DataFrame
for source in sources:
    net_generation[source] = data[data['source'] == source]['net_generation'].values

# Convert the net_generation dictionary to a list of lists
net_generation_values = [net_generation[source] for source in sources]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))

# Arrange the angles evenly
angles = np.linspace(0, 2 * np.pi, num_years, endpoint=False).tolist()

# Repeat the first value to close the circle
net_generation_values = [np.concatenate((val, [val[0]])) for val in net_generation_values]
angles += angles[:1]

# Draw the radar chart
for i in range(num_sources):
    ax.plot(angles, net_generation_values[i], label=sources[i])
    ax.fill(angles, net_generation_values[i], alpha=0.25)

# Display year labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(years)
ax.yaxis.grid(True)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Title
plt.title('Net Generation by Source Over Years')

# Show the radar chart
plt.show()
