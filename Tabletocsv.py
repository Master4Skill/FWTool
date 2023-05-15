import numpy as np
import csv


# Die Daten aus der ersten Tabelle
data = [
    [2019, 1, 332.384657],
    [2019, 2, 5.192877],
    [2019, 3, 0],
    [2019, 4, 43.453898],
    [2019, 5, 2422.722115],
    [2019, 6, 1248.1333165],
    [2019, 7, 0],
    [2020, 1, 420.842087],
    [2020, 2, 5.183286],
    [2020, 3, 0],
    [2020, 4, 43.375647],
    [2020, 5, 2668.790623],
    [2020, 6, 1322.420172],
    [2020, 7, 0],
]

# Das Lastenprofil für den Fernwärmebedarf pro Monat
lastenprofil = {
    "Januar": 13,
    "Februar": 11,
    "März": 10,
    "April": 9,
    "Mai": 8,
    "Juni": 7,
    "Juli": 6,
    "August": 5,
    "September": 4,
    "Oktober": 4,
    "November": 6,
    "Dezember": 9,
}

# Erstelle eine leere Tabelle
tabelle = np.zeros((len(data), len(lastenprofil) + 3), dtype=object)

# Fülle die erste Zeile der Tabelle mit Monatsnamen
tabelle[0, 3:] = list(lastenprofil.keys())

# Fülle die Daten aus der ersten Tabelle in die entsprechenden Spalten der Tabelle
for i, row in enumerate(data):
    jahr, cluster, fernwaerme = row
    tabelle[i, 0] = jahr
    tabelle[i, 1] = cluster
    tabelle[i, 2] = fernwaerme

    # Berechne den Fernwärmebedarf pro Monat
    if fernwaerme > 0:
        for j, monat in enumerate(lastenprofil.keys()):
            bedarf = fernwaerme * (lastenprofil[monat] / sum(lastenprofil.values()))
            tabelle[i, j + 3] = round(bedarf, 2)

# Speichere die Tabelle als CSV-Datei
with open("ergebnis_tabelle.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Jahr", "Cluster", "Fernwärme"] + list(lastenprofil.keys()))
    writer.writerows(tabelle)

print("Die Tabelle wurde als ergebnis_tabelle.csv gespeichert.")
