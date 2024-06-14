# # Import libraries
# import pandas as pd
# import plotly.graph_objects as go

# # Read the CSV file
# data = pd.read_csv("myfile.csv")

# # Get the values from columns A and B
# labels = data["A"]
# values = data["B"]

# # Create the donut chart
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

# # Update layout for better visualization
# fig.update_layout(title_text="Donut Chart from myfile.csv")

# # Show the plot
# fig.show()
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("myfile.csv")

# Extract data from desired columns
categories = data["A"].tolist()
values = data["B"].tolist()

# Create the donut chart
plt.figure(figsize=(8, 8))  # Customize the figure size as desired
plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=140)  # Adjust startangle for better readability

# Create a circle for the donut hole
center_circle = plt.Circle((0, 0), 0.7, color="white")
plt.gca().add_artist(center_circle)

# Set chart title and labels
plt.title("Distribution of Values")
plt.axis("equal")  # Equal aspect ratio for a circular chart

# Display the chart
plt.show()
