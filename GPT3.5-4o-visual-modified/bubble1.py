import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
data = pd.read_csv('/Users/saadiqraufkhan/Documents/IITD/Major Project 2/gpt3.5 visual variables python/iowa-electricity-extended.csv')

# Extracting relevant columns
years = pd.to_datetime(data['year'])
sources = data['source']
net_generation = data['net_generation']
consumption = data['consumption']

# Calculate the angle of the triangle based on the consumption
angles = consumption / consumption.max() * 360

# Plotting the bubble chart
plt.figure(figsize=(10, 6))

for i in range(len(years)):
    x = years[i]
    y = net_generation[i]
    angle = np.radians(angles[i])
    size = consumption[i] * 10  # Adjusting size for better visualization
    plt.scatter(x, y, s=size, marker=(3, 0, angle), label=sources[i])

plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Bubble Chart with Triangular Points')
plt.legend(title='Source', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
