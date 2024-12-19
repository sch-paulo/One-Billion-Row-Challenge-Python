import dask
import dask.dataframe as dd

def create_dask_df():
    dask.config.set({'dataframe.query-planning': True})
    # Configuring Dask Dataframe to read the CSV file
    # Since the file does not have a header, we specify the column names manually
    df = dd.read_csv("data/measurements.txt", sep=";", header=None, names=["station", "measure"])
    
    # Grouping by "station" and calculating max, min and mean of "measure"
    # Dask does operations in a "lazy" way, so this part just defines the calculus
    grouped_df = df.groupby("station")['measure'].agg(['max', 'min', 'mean']).reset_index()

    # Dask does not support direct ordering of grouped/resulting Dataframes in an efficient way
    # But you can compute the result and than order it if the resulting dataset is not very large
    # Or, if it is an essential thing for the next step of processing, the ordering can be done after 
    # the ".compute()" call

    return grouped_df

if __name__ == "__main__":
    import time

    start_time = time.time()
    df = create_dask_df()
    
    # The real calculus and the ordering are done here
    result_df = df.compute().sort_values("station")
    took = time.time() - start_time

    print(result_df)
    print(f"Python + Dask process took: {took:.2f} sec")
