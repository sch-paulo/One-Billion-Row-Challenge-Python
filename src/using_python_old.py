from csv import reader
from collections import defaultdict
import time

from pathlib import Path

def process_temperatures(txt_path: Path):
    print("Initializing file procesing.")
    start_time = time.time()

    station_temperature = defaultdict(list)

    """
        'station_temperature' example:
        station_temperature = {
            'Hamburg': [12.0],
            'Bulawayo': [8.9],
            'Palembang': [38.8],
            'St. John\'s': [15.2],
            'Cracow': [12.6],
            'Bridgetown': [26.9],
            'Istanbul': [6.2, 23.0], # Note that Istambul has two entries
            'Roseau': [34.4],
            'Conakry': [31.2],
        }
        Using 'defaultdict' from the 'collections' module is a convenient choice
        Without 'defaultdict', the code to add a temperature would be more complicated:
        if station_name not in station_temperature:
            station_temperature[station_name] = []
        station_temperature[station_name].append(temperature)
        With 'defaultdict':
        station_temperature[station_name].append(temperature)
    """

    with open(txt_path, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            station_name, temperature = str(row[0]), float(row[1])
            station_temperature[station_name].append(temperature)

    print("Data loaded. Calculating statistics...")

    # Dictionary to store the calculated results
    results = {}

    # Calculating min, mean and max for each station
    for station, temperatures in station_temperature.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Statistics calculated. Ordering...")
    # Ordering the results by station name
    sorted_results = dict(sorted(results.items()))

    # Formatting results for better displaying
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()
    print(f"Python process took: {end_time - start_time:.2f} sec.")

    return formatted_results

# Change 'data/measurements.txt' for the correct path of your file
if __name__ == "__main__":

    txt_path: Path = Path("data/measurements.txt")
    results = process_temperatures(txt_path)