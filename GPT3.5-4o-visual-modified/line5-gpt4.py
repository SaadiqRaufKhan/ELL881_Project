import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV file
file_path = 'iowa-electricity.csv'
data = pd.read_csv(file_path)

# Ensure the 'year' column is in datetime format
data['year'] = pd.to_datetime(data['year'])

# Plotting
plt.figure(figsize=(10, 6))

# Loop through each source to plot separately
for source in data['source'].unique():
    source_data = data[data['source'] == source]
    plt.plot(source_data['year'], source_data['net_generation'], label=source, color='green')
    plt.scatter(source_data['year'], source_data['net_generation'], color='purple', marker='s')  # purple squares

# Adding title and labels
plt.title('Net Generation Over Time by Source')
plt.xlabel('Year')
plt.ylabel('Net Generation')
plt.legend(title='Source')
plt.grid(True)

# Show the plot
plt.show()
