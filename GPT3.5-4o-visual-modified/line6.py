import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('iowa-electricity.csv')

# Convert 'year' column to datetime type
df['year'] = pd.to_datetime(df['year'])

# Group data by 'source' and plot lines
fig, ax = plt.subplots()
for key, grp in df.groupby('source'):
    ax.plot(grp['year'], grp['net_generation'], label=key, linestyle='--')

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Net Generation')
ax.set_title('Net Generation by Source')
ax.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.show()
