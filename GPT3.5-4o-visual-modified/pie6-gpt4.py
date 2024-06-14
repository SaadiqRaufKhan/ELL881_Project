import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Load the data from the CSV file
df = pd.read_csv('myfile.csv')

# Sort the data by the quantitative values in descending order
df_sorted = df.sort_values(by='B', ascending=False)

# Prepare data for the pie chart
sizes = df_sorted['B']
labels = [f'{value}' for value in sizes]

# Create the pie chart
fig, ax = plt.subplots()
wedges, texts = ax.pie(sizes, startangle=90, counterclock=False, wedgeprops=dict(width=0.3))

# Add quantities outside of the pie
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2.0 + wedge.theta1
    y = np.sin(np.deg2rad(angle))
    x = np.cos(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(angle)
    ax.annotate(labels[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                horizontalalignment=horizontalalignment, arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_aspect('equal')

# Display the plot
plt.show()
