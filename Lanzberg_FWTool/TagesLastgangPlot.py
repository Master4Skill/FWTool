import matplotlib.pyplot as plt
import pandas as pd


def read_data(filename, scenario, year):
    df = pd.read_csv(filename, delimiter=';', header=1)  # We specify that the decimal point is comma
    df = df.dropna(subset=['Monat'])

    if scenario == "Status Quo":
        index = 3 + ((year - 2023) // 5)
    elif scenario == "1":
        index = 4 + ((year - 2025) // 5)
    elif scenario == "2":
        index = 10 + ((year - 2025) // 5)
    else:
        raise ValueError("Ungültiges Szenario")


    # convert columns to proper types
    df['Monat'] = df['Monat'].astype(int)
    df['Tag'] = df['Tag'].astype(int)
    df['Stunde'] = df['Stunde'].astype(int)
    df[df.columns[index]] = df[df.columns[index]].astype(float)

    data = list(zip(df['Monat'], df['Tag'], df['Stunde'], df[df.columns[index]]))
    
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
