import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("iowa-electricity.csv")

# Convert 'year' column to datetime type
df['year'] = pd.to_datetime(df['year'])

# Group by 'year' and 'source' and sum 'net_generation'
grouped_df = df.groupby(['year', 'source'])['net_generation'].sum().unstack()

# Plotting
plt.figure(figsize=(10, 6))

# Plot each source as a separate line
for column in grouped_df.columns:
    plt.plot(grouped_df.index, grouped_df[column], label=column)

plt.title('Net Generation of Electricity in Iowa by Source')
plt.xlabel('Year')
plt.ylabel('Net Generation (MWh)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
