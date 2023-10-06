import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from feature_engineering import featureEngineering

def dataVisualisation():
    df = featureEngineering()

    # distinguishing features between numerical and categorical values
    cat_types = df.select_dtypes("object").columns
    num_types = df.select_dtypes("number").columns
    df_num = df[num_types]

    #correlation heatmap
    corr = df_num.corr()
    plt.figure(figsize = (18,14))
    mp = sns.heatmap(corr, linewidth = 1 ,  annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()

    # #missing no visualisation
    # msno.bar(df)
    # plt.show()

    #boxplot
    for col in num_types:
        plt.figure(figsize=(5, 5)) 
        sns.boxplot(data=df, x=col)
        plt.xlabel(col)
    plt.show()

    #data balance
    x = df['fraud_reported'].value_counts()
    # df['temp'].plot(kind='bar', figsize=(10, 6))
    p = x.plot(kind = 'bar')
    p.set_xlabel("Reported Fraud Value")
    p.set_ylabel("Counts")
    p.set_title("Distribution of Reported Insurance Fraud Cases")
    plt.show()

    return df



dataVisualisation()
