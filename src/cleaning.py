import pandas as pd

def delete_columns (df, columns):
    df.drop(columns = columns, inplace=True)
    print("Deleted columns: ", list(columns))
    return

def compare_columns (df, columns):
    lengths_list = []
    for i in columns:
        lengths_list.append(len(df[i]))
    max_len = max(lengths_list)
    return max_len
