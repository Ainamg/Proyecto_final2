import pandas as pd

def eda_preliminar (df):
    display (df.sample(5))

    print('-----------------------')

    print('INFO')

    display(df.info())

    print('-----------------------')

    print('NULOS')

    display(round(df.isnull().sum()/df.shape[0] * 100,2))

    print('-----------------------')

    print('DUPLICADOS')

    display(df.duplicated().sum())

    print('-----------------------')

    print('VALUE COUNTS')

    for col in df.select_dtypes(include='object').columns:
        print(df[col].value_counts())
        print('-----------------------')

def valores_minus(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.lower()


