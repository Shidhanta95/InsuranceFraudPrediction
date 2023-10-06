import pandas as pd

def load_data() :
    df = pd.read_csv(r'insurance_claims.csv')
    return df
