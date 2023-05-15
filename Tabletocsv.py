import numpy as np
import csv

# Datenextractfunktion aus CSV Input file

import csv

def extract_data(file_name):
    data = []
    year = None
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # skip first header
        next(csv_reader)  # skip second header
        for row in csv_reader:
            if not row:  # if row is an empty list
                continue  # skip to next iteration of loop
            if row[0] != '':
                year = int(row[0])  # get year from row
            id_cl = int(row[1])  # get id_cl from row
            et_value = float(row[2])  # get et value from row
            data.append([year, id_cl, et_value])
    return data


# Die Daten aus der ersten Tabelle
data = extract_data('input_cluster.csv')

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
with open("ergebnis_tabelle2.csv", "w", newline="", encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Jahr", "Cluster", "Fernwärme"] + list(lastenprofil.keys()))
    writer.writerows(tabelle)

print("Die Tabelle wurde als ergebnis_tabelle2.csv gespeichert.")
