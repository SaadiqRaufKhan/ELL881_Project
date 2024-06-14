import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Load the data
file_path = 'iowa-electricity-extended.csv'
df = pd.read_csv(file_path)

# Attempt to parse the 'year' column with multiple formats
def parse_dates(date):
    for fmt in ('%Y-%m-%d', '%m/%d/%y', '%m/%d/%Y'):
        try:
            return pd.to_datetime(date, format=fmt)
        except ValueError:
            continue
    raise ValueError(f'No valid date format found for {date}')

df['year'] = df['year'].apply(parse_dates)

# Define shapes for each source
shapes = {
    'Fossil Fuels': 'd',
    'Renewables': '*',
    'Nuclear Energy': '^',
    'Other': 'X'
}

# Assign a shape to each row based on the 'source' column
df['shape'] = df['source'].apply(lambda x: shapes.get(x, 'o'))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each source with a different shape
for source, group in df.groupby('source'):
    ax.scatter(
        group['year'],
        group['consumption'],
        s=group['net_generation'] / 100,  # Scale the size for better visualization
        label=source,
        marker=shapes[source],
        alpha=0.6,
        edgecolors='w',
        linewidth=0.5
    )

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Consumption')
ax.set_title('Iowa Electricity Consumption vs Net Generation')
ax.legend(title='Source')

# Improve x-axis date formatting
ax.xaxis.set_major_formatter(plt.FixedFormatter(df['year'].dt.strftime("%Y-%m")))

plt.xticks(rotation=45)
plt.grid(True)
plt.show()
