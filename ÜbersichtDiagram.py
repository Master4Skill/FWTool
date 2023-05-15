import numpy as np
import matplotlib.pyplot as plt
import csv

# Lese die Daten aus der CSV-Datei
data = []
with open('ergebnis_tabelle2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Überspringe die Header-Zeile
    for row in reader:
        data.append(row)

# Extrahiere die erforderlichen Informationen aus den Daten
years = np.array([int(row[0]) for row in data])
clusters = np.array([int(row[1]) for row in data])
heat_demand = np.array([float(row[2]) for row in data])
months = np.array(['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'])
demand_per_month = np.array([row[3:] for row in data], dtype=float)

while True:
    # Frage den Benutzer nach dem gewünschten Jahr
    selected_year = int(input("Geben Sie das gewünschte Jahr ein (oder '0' zum Beenden): "))

    # Überprüfe, ob das Programm beendet werden soll
    if selected_year == 0:
        print("Programm beendet.")
        break

    # Überprüfe, ob das ausgewählte Jahr in den Daten vorhanden ist
    if selected_year not in years:
        print("Das eingegebene Jahr ist nicht in den Daten vorhanden.")
        continue

    # Erstelle den Plot für das ausgewählte Jahr
    fig, ax = plt.subplots()
    for cluster in np.unique(clusters):
        mask = (years == selected_year) & (clusters == cluster)
        color = plt.cm.get_cmap('tab10')(cluster - 1)  # Verwende unterschiedliche Farben für jeden Cluster
        ax.plot(months, demand_per_month[mask].flatten(), marker='o', color=color, label=f'Cluster {cluster}')
    ax.set_xticks(np.arange(len(months)))
    ax.set_xticklabels(months, rotation=45)
    ax.set_xlabel('Monat')
    ax.set_ylabel('Wärmebedarf')
    ax.set_title(f'Wärmebedarf pro Monat (Jahr {selected_year})')
    ax.legend()
    plt.tight_layout()
    plt.show()
