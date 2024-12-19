from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # barra de progresso
import time
from pathlib import Path

NUMERO_DE_LINHAS: int = 10_000_000

def processar_temperaturas(path_do_txt: Path) -> dict:
    # utilizando infinito positivo e negativo para comparar
    minimas: defaultdict = defaultdict(lambda: float('inf'))
    maximas: defaultdict = defaultdict(lambda: float('-inf'))
    somas: defaultdict = defaultdict(float)
    medicoes: Counter = Counter()

    with open(path_do_txt, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # usando tqdm diretamente no iterador, isso mostrará a porcentagem de conclusão.
        for row in tqdm(_reader, total=NUMERO_DE_LINHAS, desc="Processando"):
            nome_da_station: str = str(row[0])
            temperatura: float = float(row[1])
            medicoes.update([nome_da_station])
            minimas[nome_da_station] = min(minimas[nome_da_station], temperatura)
            maximas[nome_da_station] = max(maximas[nome_da_station], temperatura)
            somas[nome_da_station] += temperatura

    print("Dados carregados. Calculando estatísticas...")

    # calculando min, média e max para cada estação
    results: dict = {}
    for station, qtd_medicoes in medicoes.items():
        mean_temp: float = somas[station] / qtd_medicoes
        results[station] = (minimas[station], mean_temp, maximas[station])

    print("Estatística calculada. Ordenando...")
    # ordenando os resultados pelo nome da estação
    sorted_results: dict = dict(sorted(results.items()))

    # formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    path_do_txt: Path = Path("data/measurements.txt")

    print("Iniciando o processamento do arquivo.")
    start_time: float = time.time()  # Tempo de início

    resultados: dict = processar_temperaturas(path_do_txt)

    end_time: float = time.time()  # Tempo de término

    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')

    print(f"\nProcessamento concluído em {end_time - start_time:.2f} segundos.")