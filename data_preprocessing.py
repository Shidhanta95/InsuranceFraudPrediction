import pandas as pd
import numpy as np

from loading_data import load_data
'''
PREPROCESSING :cls

    1. EDA 
    2. Data Imputation and Deletion

        1. Check and fill nulls
        2. Check Unique and Duplicates
        3. Check for heuristically impossible value
        4. Store cat and num types seperately 
        5. Check and treat for outliers
        6. Check for balanced and unbalanced dataset 
        7. Check for Correlation

'''


def outlierTreatment(df):
    # Outlier Treatment 
    # IQR
    df.reset_index(drop=True)

    # Create arrays of Boolean values indicating the outlier rows
    # upper_array = np.where(df[col]>=upper)[0]
    # lower_array = np.where(df[col]<=lower)[0]
    
    # # Removing the outliers
    # df.drop(index=upper_array, inplace=True)
    # df.drop(index=lower_array, inplace=True)
    num_types = df.select_dtypes("number").columns
    # Calculate the upper and lower limits
    for col in num_types:    
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1
        lower = Q1 - 1.5*IQR
        upper = Q3 + 1.5*IQR
    
  
    
    df[col] = np.where(df[col] > upper, upper,df[col])
    df[col] = np.where(df[col]<lower, lower, df[col])
    return df

def preprocessing():
    df = load_data()
    df.replace('?',np.nan , inplace = True)
    # filling null values 
    names = df[df.columns[df.isna().any()]].columns
    for name in names:
        df[name].fillna(df[name].mode(), inplace = True)
    
    #columsn to drop 
    to_drop = ['policy_number','policy_bind_date','policy_state','insured_zip','incident_location','incident_date',
           'incident_state','incident_city','insured_hobbies','auto_make','auto_model','auto_year', '_c39']
    df.drop(to_drop, inplace = True, axis = 1)

    #Rows to drop
    #drop duplicate rows
    df.drop_duplicates(keep = 'first', inplace= True)


    #high correlation between ->
    # 1. age - months_as_customer
    # 2. total_claim_ammount - injury_claim - property_claim - vehicle_claim
    # drop -> age , injury_claim, property_claim, vehicle_claim
    df= df.drop('age', axis = 1)
    df = df.drop(['injury_claim','property_claim','vehicle_claim'] , axis = 1)  
    df = outlierTreatment(df)
    return df

preprocessing()
