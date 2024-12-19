from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # progress bar
import time
from pathlib import Path

NUMBER_OF_ROWS: int = 1_000_000_000

def process_temperatures(txt_path: Path) -> dict:
    # utilizando infinito positivo e negativo para comparar
    minimum: defaultdict = defaultdict(lambda: float('inf'))
    maxims: defaultdict = defaultdict(lambda: float('-inf'))
    sums: defaultdict = defaultdict(float)
    measures: Counter = Counter()

    with open(txt_path, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # Iterating with tqdm to visualize the progress bar
        for row in tqdm(_reader, total=NUMBER_OF_ROWS, desc="Processing"):
            station_name: str = str(row[0])
            temperature: float = float(row[1])
            measures.update([station_name])
            minimum[station_name] = min(minimum[station_name], temperature)
            maxims[station_name] = max(maxims[station_name], temperature)
            sums[station_name] += temperature

    print("Data loaded. Calculating statistics...")

    # Calculating min, mean and max for each station
    results: dict = {}
    for station, qty_measures in measures.items():
        mean_temp: float = sums[station] / qty_measures
        results[station] = (minimum[station], mean_temp, maxims[station])

    print("Statistics calculated. Ordering...")
    # Ordering the results by station name
    sorted_results: dict = dict(sorted(results.items()))

    # Formatting results for better displaying
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    txt_path: Path = Path("data/measurements.txt")

    print("Initializing file processing.")
    start_time: float = time.time()

    results: dict = process_temperatures(txt_path)

    end_time: float = time.time()

    for station, metrics in results.items():
        print(station, metrics, sep=': ')

    print(f"\nPython process took: {end_time - start_time:.2f} sec.")