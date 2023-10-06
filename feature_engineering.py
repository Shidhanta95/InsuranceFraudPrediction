import pandas as pd
from data_preprocessing import preprocessing
from imblearn.over_sampling import RandomOverSampler

def SMOTEUpsampling(df):
    #smote based upsampling 
    # transform the dataset
    oversample = RandomOverSampler(sampling_strategy='minority')
    column = df.columns
    y = df[column[-1]]
    x = df.drop('fraud_reported', axis = 1)
    # x = np.nan_to_num(x)
    # y = np.nan_to_num(y)
    x,y = oversample.fit_resample(x,y)
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)

    df_concat = pd.concat([x,y], axis=1) 
    return df_concat

def featureEngineering():
    df = preprocessing()
    df = SMOTEUpsampling(df)
    df.to_csv("insurance_claims_final.csv", index = False)
    return df

featureEngineering()
