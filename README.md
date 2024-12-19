# One Billion Row: Processing Challenge Using Python

## Introdution

The goal of this project is to demonstrate how to efficiently process a massive data file containing up to 1 billion rows (~14 GB), specifically to calculate statistics (including aggregation and ordering, which are heavy operations) using Python.

This challenge was inspired by [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originally proposed for Java.

The data file consists of temperature measurements from several weather stations. Each record follows the format `<string: station name>;<double: measurement>`, with the temperature being presented to one decimal place accuracy.

Below is an example of ten lines from the file:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

The challenge is to develop a Python program capable of reading this file and calculating the min, mean (rouned to one decimal place) and max for each station, displaying the results in a table sorted by station name.

| station      | min_temperature | mean_temperature | max_temperature |
|--------------|-----------------|------------------|-----------------|
| Abha         | -31.1           | 18.0             | 66.5            |
| Abidjan      | -25.9           | 26.0             | 74.6            |
| Abéché       | -19.8           | 29.4             | 79.9            |
| Accra        | -24.8           | 26.4             | 76.3            |
| Addis Ababa  | -31.8           | 16.0             | 63.9            |
| ...          | ...             | ...              | ...             |
| Zagreb       | -39.2           | 10.7             | 58.1            |
| Zanzibar City| -26.5           | 26.0             | 75.2            |
| Zürich       | -42.0           | 9.3              | 63.6            |
| Ürümqi       | -42.1           | 7.4              | 56.7            |
| İzmir        | -34.4           | 17.9             | 67.9            |

## Dependencies

In order to run the scripts from this project, you will need the following libraries:

* Polars: `0.20.3`
* DuckDB: `0.10.0`
* Dask[complete]: `^2024.2.0`

## Results

Tests were performed on a desktop equipped with an AMD Ryzen 7 5700X 3.4GHz procesor and 32GB of RAM. The implementations used purely Python, Pandas, Dask, Polars and DuckDB approaches. The table below presents the runtime results for processing 1M, 10M, 100M and 1B rows:

| Method | 1M rows | 10M rows | 100M rows | 1B rows (15.7GB) |
| --- | --- | --- | --- | --- |
| Python | 1.49 sec | 15.00 sec | 151.66 sec | 1484.89 sec |
| Python + Pandas | 1.07 sec | 3.42 sec | 27.99 sec | 300.72 sec |
| Python + Dask | 0.57 sec | 2.55 sec | 19.73 sec | 195.27 sec |
| Python + Polars | 0.08 sec | 0.25 sec | 1.70 sec | 16.43 sec |
| Python + Duckdb | 0.05 sec | 0.16 sec | 1.33 sec | 12.57 sec |

Thank you [Koen Vossen](https://github.com/koenvo) for Polars implementation, [Arthur Julião](https://github.com/ArthurJ) for the Python and Bash implementation and, finally, [Luciano Vasconcelos](https://github.com/lvgalvao) for the other implementations.

## Conclusion

This challenge clearly highlighted the effectiveness of several Python libraries in handling large volumes of data. Traditional methods such as pure Python and even Pandas required a series of tactics to implement the "batch" processing, while libraries like Dask, Polars and DuckDB proved to be exceptionally effective, requiring fewer lines of code due to their inherent ability to distribute data in "streaming batches" more efficiently. DuckDB came out on top, achieving the fastest execution time thanks to its data processing strategy.

These results emphasize the importance of selecting the right tool to large-scale data analysis, demonstrating that, with the right libraries, Python is a powerful choice to face big data challenges.q

## How to execute

In order to execute this project and reproduce the results:

1. Clone this repository
2. Set the Python version using `pyenv local 3.12.1`
2. Configure Poetry with `poetry env use 3.12.1`, `poetry install --no-root` and `poetry lock --no-update`
3. Run `python src/create_measurements.py` to generate the test file
4. Be pattient and go for a walk, it may take a while to generate the file
5. Make sure to install the specified versions of Dask, Polars and DuckDB libraries
6. Run the scripts `python src/using_python.py`, `python src/using_pandas.py`, `python src/using_dask.py`, `python src/using_polars.py` and `python src/using_duckdb.py` through a terminal or an IDE that supports Python

Este projeto destaca a versatilidade do ecossistema Python para tarefas de processamento de dados, oferecendo valiosas lições sobre escolha de ferramentas para análises em grande escala.

<br>
<br>

---
<br>
This projects is part of *Jornada de Dados*

Our mission is to provide the best education in data engineering.