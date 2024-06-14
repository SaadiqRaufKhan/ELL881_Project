import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('myfileDotPlot2Values.csv')

# Group the data by category in column A
grouped = df.groupby('A')['B']

# Initialize lists to store category names and ranges
categories = []
ranges = []

# Iterate over groups to extract category names and ranges
for category, group_data in grouped:
    categories.append(category)
    ranges.append((group_data.min(), group_data.max()))

# Plotting
plt.figure(figsize=(10, 6))

# Plot each category
for i, (category, group_data) in enumerate(grouped):
    y_values = [i] * len(group_data)  # Horizontal position for this category
    plt.plot(group_data, y_values, 'o', label=category)

# Plot range lines
for i, (category, (min_val, max_val)) in enumerate(zip(categories, ranges)):
    plt.plot([min_val, max_val], [i, i], color='black')

plt.yticks(range(len(categories)), categories)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Range Plot')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
