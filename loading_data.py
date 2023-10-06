import pandas as pd

df = pd.read_csv(r'insurance_claims.csv')

def load_data() :
    df = pd.read_csv(r'insurance_claims.csv')
    return df