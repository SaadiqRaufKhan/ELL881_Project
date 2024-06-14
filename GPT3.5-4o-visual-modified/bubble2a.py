import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv('iowa-electricity-extended.csv')

# Convert 'year' column to datetime
data['year'] = pd.to_datetime(data['year'])

# Define the size of the points based on the 'source' column
sizes = {'Coal': 100, 'Natural Gas': 200, 'Nuclear': 300, 'Renewables': 400}

# Map source to size
data['size'] = data['source'].map(sizes)

# Plot the bubble chart
plt.figure(figsize=(10, 6))
for source in data['source'].unique():
    plt.scatter(data[data['source'] == source]['year'],
                data[data['source'] == source]['net_generation'],
                s=data[data['source'] == source]['size'],
                alpha=0.5,
                label=source)

plt.title('Net Generation vs. Year (Bubble Chart)')
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.legend(title='Source')
plt.grid(True)
plt.show()
