import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('iowa-electricity.csv')

# Convert 'year' column to datetime type
df['year'] = pd.to_datetime(df['year'])

# Set the width of lines
line_width = 10

# Group by 'source' and plot each group separately
for name, group in df.groupby('source'):
    plt.plot(group['year'], group['net_generation'], label=name, linewidth=line_width)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Net Generation by Source Over Time')
plt.legend()

# Show the plot
plt.show()
