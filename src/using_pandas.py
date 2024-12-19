import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  # for the progress bar

CONCURRENCY = cpu_count()

total_rows = 1_000_000_000  # Total number of rows known
chunksize = 100_000_000  # Chunk size
filename = "data/measurements.txt"  # Make sure that this is the right path for the file 

def process_chunk(chunk):
    # Aggregate data inside the chunk using Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated

def create_df_with_pandas(filename, total_rows, chunksize=chunksize):
    total_chunks = total_rows // chunksize + (1 if total_rows % chunksize else 0)
    results = []

    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # Iterating with tqdm to visualize the progress bar
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processando"):
                # Process each chunk in parallel
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Initializing file processing.")
    start_time = time.time()
    df = create_df_with_pandas(filename, total_rows, chunksize)
    took = time.time() - start_time

    print(df.head())
    print(f"Python + Pandas process took: {took:.2f} sec")
