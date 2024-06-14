import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('iowa-electricity.csv')

# Convert 'year' column to datetime format
df['year'] = pd.to_datetime(df['year'])

# Group data by 'source'
grouped = df.groupby('source')

# Plot each group with opacity set to 0.5
plt.figure(figsize=(10, 6))
for name, group in grouped:
    plt.plot(group['year'], group['net_generation'], label=name, alpha=0.5)

plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.title('Net Generation Over Time by Source')
plt.legend()
plt.grid(True)
plt.show()
