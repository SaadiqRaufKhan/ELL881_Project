import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('iowa-electricity.csv')

# Ensure the 'year' column is in datetime format
df['year'] = pd.to_datetime(df['year'])

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot data for each source
for source in df['source'].unique():
    source_data = df[df['source'] == source]
    plt.plot(source_data['year'], source_data['net_generation'], label=source, color='purple')

# Add title and labels
plt.title('Net Generation of Electricity in Iowa by Source')
plt.xlabel('Year')
plt.ylabel('Net Generation')

# Add legend
plt.legend(title='Source')

# Show the plot
plt.show()
