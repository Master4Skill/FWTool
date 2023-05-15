import numpy as np
import matplotlib.pyplot as plt
import csv

# Read the data from the CSV file
data = []
with open("ergebnis_tabelle.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        data.append(row)

# Extract the required information from the data
years = np.array([int(row[0]) for row in data])
clusters = np.array([int(row[1]) for row in data])
heat_demand = np.array([float(row[2]) for row in data])
months = np.array(
    [
        "Januar",
        "Februar",
        "März",
        "April",
        "Mai",
        "Juni",
        "Juli",
        "August",
        "September",
        "Oktober",
        "November",
        "Dezember",
    ]
)
demand_per_month = np.array([row[3:] for row in data], dtype=float)

# Ask the user for the desired year and cluster
selected_year = int(input("Enter the year: "))
selected_cluster = int(input("Enter the cluster: "))

# Check if the program should be terminated
if selected_year == 0 or selected_cluster == 0:
    print("Program terminated.")
    exit()

# Check if the selected year and cluster are present in the data
if (selected_year, selected_cluster) not in zip(years, clusters):
    print("The entered year and cluster combination is not present in the data.")
    exit()

# Filter the data for the selected year and cluster
mask = (years == selected_year) & (clusters == selected_cluster)
selected_demand = demand_per_month[mask].flatten()

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(months, selected_demand)
ax.set_xlabel("Month")
ax.set_ylabel("Heat Demand")
ax.set_title(
    f"Heat Demand per Month - Year {selected_year}, Cluster {selected_cluster}"
)
plt.tight_layout()
plt.show()
