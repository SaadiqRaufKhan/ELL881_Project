import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'iowa-electricity-extended.csv'
df = pd.read_csv(file_path)

# Ensure the 'year' column is in datetime format
df['year'] = pd.to_datetime(df['year'])

# Extract the year as an integer for plotting
df['year_numeric'] = df['year'].dt.year

# Generate the scatterplot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['net_generation'], df['consumption'], 
                      s=(df['year_numeric'] - df['year_numeric'].min()) * 10,  # Scale the size
                      c=df['year_numeric'], cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)

# Add a colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Year')

# Set plot labels and title
plt.xlabel('Net Generation')
plt.ylabel('Consumption')
plt.title('Scatterplot of Net Generation vs. Consumption by Year')

# Show the plot
plt.grid(True)
plt.show()
