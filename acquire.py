from env import get_db_url
import os
import pandas as pd


def get_telco_data():
    """
    Gets all data from the telco_churn db in sql. To make it work, use 'df = get_telco_data()'

    arguments: none

    return: a pandas dataframe
    """
    filename = "telco.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT *
        FROM customers
        JOIN contract_types
        USING (contract_type_id)
        JOIN internet_service_types
        USING (internet_service_type_id)
        JOIN payment_types
        USING (payment_type_id);"""
        connection = get_db_url("telco_churn")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df


def get_summary(df):
    '''
    get_summary will take in one positional argument, a single pandas DF, 
    and will output info to the console regarding the following info:
    - print the first 3 rows
    - print the # of rows and columns
    - print the columns
    - print the dtypes of each col
    - print summary statistics
    
    return:none
    '''

    print('First 3 rows of the dataframe:')
    print(df.head(3))
    print('~~~~~~~~~~~~~~')
    print('Number of Rows and Cols in DF:')
    print(f'Rows: {df.shape[0]}, Cols: {df.shape[1]}')
    print('~~~~~~~~~~~~~~')
    print('Column Names:')
    [print(col) for col in df.columns]
    print('~~~~~~~~~~~~~~')
    [print(col,'- datatype:', df[col].dtype) for col in df.columns]
    print('~~~~~~~~~~~~~~')
    print(df.describe().T)
    print('~~~~~~~~~~~~~~')
    print('Descriptive stats for Object Variables: ')
    print(df.loc[:, df.dtypes=='O'].describe().T)
    print('~~~~~~~~~~~~~~')
    for col in df.loc[:, df.dtypes=='O']:
        if df[col].nunique() > 10:
            print(f'Column {col} has too many uniques ({df[col].nunique()}) to display')
        else:
            print(f' {col}: ', df[col].unique())