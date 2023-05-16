import matplotlib.pyplot as plt
import csv

def read_data(filename, scenario, year):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        header = True
        for row in reader:
                        # Skip rows that don't have at least 3 columns or if the first 3 columns are not all digits
            if len(row) < 3 or not all(item.isdigit() for item in row[:3]):
                continue

            month, day, hour = map(int, row[:3])

            if scenario == "Status Quo":
                index = 4 + (year - 2023)
            elif scenario == "1":
                index = 13 + (year - 2025)
            elif scenario == "2":
                index = 21 + (year - 2025)
            else:
                raise ValueError("Ungültiges Szenario")

            try:
                value = float(row[index].replace(',', '.'))
            except ValueError:
                value = 0.0  # default value for cells that can't be converted to float

            data.append((month, day, hour, value))
    return data


def plot_data(data, month, day, scenario, year):
    x = []
    y = []

    for d in data:
        m, d, h, v = d
        if m == month and d == day:
            x.append(h)
            y.append(v)

    plt.plot(x, y)
    plt.xlabel("Stunde")
    plt.ylabel("Fernwärmebedarf")
    plt.title(f"Lastgang für {day}.{month} ({scenario}, {year})")
    plt.grid(True)
    plt.show()

def main():
    filename = "Versorgungskonzepte.csv"

    day = int(input("Bitte geben Sie einen Tag ein (z.B. 13): "))
    month = int(input("Bitte geben Sie einen Monat ein (z.B. 1): "))
    scenario = input("Bitte geben Sie ein Szena13io ein (Status Quo, 1, 2): ")
    year = int(input("Bitte geben Sie ein Jahr ein (2023, 2025, 2030, 2035, 2040, 2045, 2050): "))

    data = read_data(filename, scenario, year)
    plot_data(data, month, day, scenario, year)

if __name__ == "__main__":
    main()
