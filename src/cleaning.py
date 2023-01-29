import pandas as pd
import warnings
from pandas.core.common import SettingWithCopyWarning   #I import this library and setting to be able to hide warnings that show me information I do not need.

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

def compare_columns (df, columns):
    """
    This function takes a data frame and a list. For the columns of the dataframe specified in the list, it will return descriptive information comparing those columns.
    """

    #First it determines the lenght of every column specified
    lengths_list = []
    for i in columns:
        lengths_list.append(len(df[i]))
    
    #Then it determines the amount of non-null values in every column
    non_null_list = []
    for i in columns:
        non_null_list.append(df[i].notnull().sum())

    #Now it builds a data frame with this information
    results = pd.DataFrame({
        "Columns" : columns,
        "Lengths" : lengths_list,
        "Non - null values" : non_null_list
    })
    results = results.set_index("Columns")


    #Builds a data frame with information about the types of data in every column
    data_types_list = []
    for i in columns:
        data_types_list.append(df[i].map(type).value_counts())
    data_types = pd.DataFrame(data_types_list)


    warnings.simplefilter(action="ignore", category=SettingWithCopyWarning) # I turned this setting off because it was warning me about storing a value in a copy of a DataFrame which is exactly what I wanted to do in the next step.
    
    #Builds a DataFrame comparing the number of rows in which each column is exactly the same as the other columns.
    value_comparisons = []
    for x in range(len(columns)):
        dict_x={}
        for y in range(len(columns)):
            comp = df[[columns[x],columns[y]]]
            comp.fillna(" ",inplace = True)
            comp["test"] = comp.apply(lambda row: row[0] == row[1], axis=1)
            dict_x[columns[y]] = comp.test.sum()
        value_comparisons.append(dict_x)

    value_comparisons_df = pd.DataFrame(value_comparisons)
    value_comparisons_df.index = columns


    #Creates a sample DataFrame where at least one of the values is different in one of the columns
    samples = df[columns]
    """
    def comparison (df, columns):
        tracker = df[0]
        size = len(columns)
        for i in size:
            tracker = tracker and df[i]

    samples["test"] = samples.apply(lambda row: row)

    """

    #Displays all the information collected
    print("Column information:")
    display(results.transpose())
    print("Data type comparison:")
    display(data_types.transpose())
    print("Value comparisons:")
    display(value_comparisons_df)
    print("The above matrix shows the amount of rows that each column shares with other columns. E.g. how many cells store the same information in both columns")
    print("Sample of columns with differences:")
    display(df[columns].sample(5))

    pass