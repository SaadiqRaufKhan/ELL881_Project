# import matplotlib.pyplot as plt
# import pandas as pd

# def generate_pyramid_chart(csv_file):
#     # Read the data from the CSV file
#     data = pd.read_csv(csv_file)

#     # Ensure the required columns exist
#     required_columns = ['Age Range', 'Male', 'Female']
#     if not all(col in data.columns for col in required_columns):
#         print("Error: The CSV file does not contain the required columns.")
#         return

#     # Create a figure and axis
#     fig, ax = plt.subplots(figsize=(8, 6))

#     # Sort the data by 'Age Range'
#     data = data.sort_values(by='Age Range')

#     # Get the age ranges
#     age_ranges = data['Age Range'].tolist()

#     # Plot the bars for females
#     ax.barh(age_ranges, data['Female'], color='pink', label='Female')

#     # Plot the bars for males
#     ax.barh(-data['Male'], age_ranges, color='skyblue', label='Male')

#     # Set the axis labels and title
#     ax.set_xlabel('Population')
#     ax.set_ylabel('Age Range')
#     ax.set_title('Population Pyramid')

#     # Adjust the x-axis limits
#     max_population = max(data['Male'].max(), data['Female'].max())
#     ax.set_xlim(-max_population * 1.1, max_population * 1.1)

#     # Add a legend
#     ax.legend()

#     # Adjust the spacing between subplots
#     plt.tight_layout()

#     # Display the chart
#     plt.show()

# # Replace 'pyramiddata.csv' with the actual name of your CSV file
# generate_pyramid_chart('pyramiddata.csv')

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('pyramiddata.csv')

# Sort the data by 'Age Range' column
data = data.sort_values(by='Age Range')

# Create a figure and axis objects
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the bars for Male and Female columns
ax.barh(data['Age Range'], data['Male'], color='blue', label='Male')
ax.barh(data['Age Range'], -data['Female'], color='red', label='Female')

# Set the x-axis limits
max_value = max(data['Male'].max(), data['Female'].max())
ax.set_xlim(-max_value * 1.1, max_value * 1.1)

# Set the title and axis labels
ax.set_title('Pyramid Chart')
ax.set_xlabel('Population')
ax.set_ylabel('Age Range')

# Add a legend
ax.legend()

# Adjust the spacing between subplots
plt.tight_layout()

# Display the chart
plt.show()