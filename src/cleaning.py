import pandas as pd

def delete_columns (df, columns):
    df.drop(columns = columns, inplace=True)
    print("Deleted columns: ", list(columns))
    return
