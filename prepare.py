import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats



def prep_telco(telco_df):
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


def split_telco_data(df, target='survived'):
    '''
    split telco data will split data based on 
    the values present in a cleaned version of titanic
    that is from clean_titanic
    
    '''
    train_val, test = train_test_split(df,
                                   train_size=0.8,
                                   random_state=1108,
                                   stratify=df[target])
    train, validate = train_test_split(train_val,
                                   train_size=0.7,
                                   random_state=1108,
                                   stratify=train_val[target])
    return train, validate, test


def clean_telco(df):
    '''
    clean telco will take in a single pandas dataframe
    and will proceed to drop redundant columns
    and nonuseful information
    in addition to addressing null values
    and encoding categorical variables
    '''
    #drop out any redundant, excessively empty, or bad columns
    df = df.drop(columns=['passenger_id','embarked','deck','class'])
    # impute average age and most common embark_town:
    train, validate, test = split_titanic_data(df)
    # impute missing values for our fields using sklearn's simpleimputer
    #create age imputer, with strategry mean
    my_age_imputer = SimpleImputer(strategy='mean')
    # use imputer object to fit to train ages
    my_age_imputer.fit(train[['age']])
    # tranform values in train, validate, and test based on mean fit from the last step
    train.loc[:,'age'] = my_age_imputer.transform(train[['age']])
    validate.loc[:,'age'] = my_age_imputer.transform(validate[['age']])
    test.loc[:,'age'] = my_age_imputer.transform(test[['age']])     
    # go through the same process with embark_town
    my_embark_imputer = SimpleImputer(strategy='most_frequent')
    my_embark_imputer.fit(train[['embark_town']])
    train.loc[:,'embark_town'] = my_embark_imputer.transform(train[['embark_town']])
    validate.loc[:,'embark_town'] = my_embark_imputer.transform(validate[['embark_town']])
    test.loc[:,'embark_town'] = my_embark_imputer.transform(test[['embark_town']])
    # encode categorical values: 
    train = pd.concat(
    [train, pd.get_dummies(train[['sex', 'embark_town']],
                        drop_first=True, dtype=int)], axis=1)
    validate = pd.concat(
    [validate, pd.get_dummies(validate[['sex', 'embark_town']],
                        drop_first=True, dtype=int)], axis=1)
    test = pd.concat(
    [test, pd.get_dummies(test[['sex', 'embark_town']],
                        drop_first=True, dtype=int)], axis=1)        
                                                                  
    return train, validate, test