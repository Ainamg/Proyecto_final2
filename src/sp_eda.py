import pandas as pd
import numpy as np

def calcular_nulos(dataframe):
    """
    Calcula el número y el porcentaje de valores nulos en cada columna de un DataFrame.

    Parámetros
    ----------
    dataframe : pandas.DataFrame
        El DataFrame sobre el cual se desea calcular los valores nulos.

    Retorna
    -------
    tuple of pandas.Series
        Una tupla con dos Series:
        - numero_nulos : pandas.Series
            Número total de valores nulos por columna.
        - porcentaje_nulos : pandas.Series
            Porcentaje de valores nulos por columna, calculado como:
            (nulos / total_filas) * 100
    """
    numero_nulos = dataframe.isnull().sum()
    porcentaje_nulos = (dataframe.isnull().sum() / dataframe.shape[0]) * 100
    return numero_nulos, porcentaje_nulos

def analisis_general_cat(dataframe):

    col_cat=dataframe.select_dtypes(include=['object']).columns

    if len(col_cat) == 0:
        print("No hay columnas categóricas en el DataFrame.")
        
    else:
        for col in col_cat:
            print(f"La dsitribución de las columna {col.upper()}")
            print(f"Esta columna tiene {len(dataframe[col].unique())} valores únicos")
            display(dataframe[col].value_counts(normalize=True))
            print("-----------")
            display(dataframe[col].describe())
            print("-----------")
    
   

