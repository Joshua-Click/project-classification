import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

def clean_telco(telco_df):
    '''USE THIS FOR INITIAL CLEAN - Cleans the telco dataset for exploring
    leaving the booleans and cleaning null values and dropping dup columns
    
    arguments: telco_df
    
    return: a clean dataframe ready to explore'''

    # drop duplicate columns and customer_id for view
    telco_df = telco_df.drop(columns =['payment_type_id','internet_service_type_id','contract_type_id', 'customer_id'])
    # fill nulls and change total_charges to float
    telco_df.total_charges = telco_df.total_charges.str.replace(' ', '0').astype(float)
    # drops (automatic) from the payment_type
    telco_df['payment_type'] = telco_df['payment_type'].str.replace(' (automatic)', '')

    return telco_df

def prep_telco(telco_df):
    '''USE THIS BEFORE MODELING - Preps the telco dataset for machine learning modeling by dropping unnessesary columns
    creating dummy values, and replacing null values in total_charges, keeps customer_id
    
    arguments: telco_df
    
    return: a dataframe ready for machine learning'''


    #drop duplicate columns
    telco_df = telco_df.drop(columns =['payment_type_id','internet_service_type_id','contract_type_id'])
    #create dummies
    dummy_list = ['gender','partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
    dummy_df = pd.get_dummies(telco_df[dummy_list], dtype=int, drop_first=True)
    # join dummy & telco_df
    telco_df = pd.concat([telco_df, dummy_df], axis=1)
    # drop str column categories
    cols_to_drop = ['gender','partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']
    telco_df = telco_df.drop(columns= cols_to_drop)
    #total_charges.str.replace(' ', '0').astype(float)
    telco_df.total_charges = telco_df.total_charges.str.replace(' ', '0').astype(float)

    return telco_df


def split_telco_data(df, target):
    '''
    split telco data into train, validate, test

    argument: df, target variable

    return: train, validate, test
    '''

    train_val, test = train_test_split(df,
                                   train_size=0.8,
                                   random_state=1108,
                                   stratify=df[target])
    train, validate = train_test_split(train_val,
                                   train_size=0.7,
                                   random_state=1108,
                                   stratify=train_val[target])
    
    print(f'Train: {len(train)/len(df)}')
    print(f'Validate: {len(validate)/len(df)}')
    print(f'Test: {len(test)/len(df)}')

    return train, validate, test


