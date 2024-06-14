import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV with column names
data = pd.read_csv("myfile.csv", names=["A", "B"])

# Get categories and values
categories = data["A"].tolist()
values = data["B"].tolist()

# Set bar width to 10 pixels
bar_width = 10

# Create the bar chart
plt.figure(dpi=200)  # Adjust DPI for desired image size
plt.bar(categories, values, width=bar_width)

# Set labels and title
plt.xlabel("Category (Column A)")
plt.ylabel("Value (Column B)")
plt.title("Bar Chart from myfile.csv")

# Rotate x-axis labels for better readability with many categories
plt.xticks(rotation=45, ha="right")

# Show the chart
plt.tight_layout()
plt.show()
