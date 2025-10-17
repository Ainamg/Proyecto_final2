import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def subplot_col_cat(dataframe):

    # Seleccionamos las columnas categoricas
    col_categoricas = dataframe.select_dtypes(include=['object']).columns

    if len(col_categoricas) == 0:
        print("No hay columnas categóricas en el DataFrame.")
        return
    
    # Configurar el tamaño de la figura
    num_cols = len(col_categoricas)
    rows = (num_cols + 2) // 3 # Número de filas necesarias
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten()  # Aplanar el array de ejes para facilitar el acceso

    # Generar gráficos para cada columna categórica
    for i, col in enumerate(col_categoricas):
        sns.countplot(data=dataframe, x=col, ax=axes[i], hue=col, palette="tab10", legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90)  # Rotar etiquetas del eje x para mejor legibilidad

    # Eliminar ejes no utilizados
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Ajustar el diseño
    plt.tight_layout()
    plt.show()

def subplot_col_num(dataframe, col):
    num_graph = len(col)

    num_rows = (num_graph + 2) // 2

    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows * 5))

    for i, col in enumerate(col):

        sns.histplot(data=dataframe, x=col, ax = axes[i,0])
        axes[i,0].set_title(f'Distribución de {col}')
        axes[i,0].set_xlabel(col)
        axes[i,0].set_ylabel('Frecuencia')

        sns.boxplot(data=dataframe, x=col, ax = axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')

    plt.tight_layout()
    plt.show()