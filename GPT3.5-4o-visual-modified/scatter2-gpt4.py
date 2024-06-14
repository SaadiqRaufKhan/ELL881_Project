# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the data
# file_path = 'iowa-electricity-extended.csv'
# data = pd.read_csv(file_path)

# # Convert 'year' column to datetime format
# data['year'] = pd.to_datetime(data['year'])

# # Extract year as an integer for plotting
# data['year_int'] = data['year'].dt.year

# # Create the scatterplot
# plt.figure(figsize=(8, 5))
# scatter = sns.scatterplot(
#     data=data, 
#     x='year_int', 
#     y='net_generation', 
#     hue='source', 
#     size='consumption', 
#     alpha=1, 
#     sizes=(20, 200),
#     palette='viridis'
# )

# # Improve the plot's appearance
# scatter.set_title('Net Generation vs. Year by Source with Consumption Encoding')
# scatter.set_xlabel('Year')
# scatter.set_ylabel('Net Generation (MWh)')
# scatter.legend(title='Source', bbox_to_anchor=(1.05, 1), loc='upper left')

# # Display the plot
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'iowa-electricity-extended.csv'
data = pd.read_csv(file_path)

# Convert the 'year' column to datetime format
data['year'] = pd.to_datetime(data['year'], format='%d/%m/%y')

# Create a scatter plot
fig, ax = plt.subplots()

# Scatter plot with 'year' on the x-axis and 'net_generation' on the y-axis
# The opacity (alpha) encodes the 'consumption' values
sc = ax.scatter(data['year'], data['net_generation'], c='blue', alpha=data['consumption']/data['consumption'].max())

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Net Generation')
ax.set_title('Net Generation vs Year with Consumption Opacity Encoding')

# Show the plot
plt.show()
