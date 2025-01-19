"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():


    import pandas as pd

    # Cargar los archivos tbl0 1.tsv y tbl2.tsv en DataFrames
    df_tbl0 = pd.read_csv('./files/input/tbl0.tsv', sep='\t')
    df_tbl2 = pd.read_csv('./files/input/tbl2.tsv', sep='\t')

    # Asegurarse de que las columnas 'c0' estén presentes en ambos DataFrames
    if 'c0' in df_tbl0.columns and 'c0' in df_tbl2.columns:
        # Unir los dos DataFrames en la columna 'c0'
        merged_df = pd.merge(df_tbl0, df_tbl2, on='c0')

        # Agrupar por 'c1' y calcular la suma de 'c5b'
        result_df = merged_df.groupby('c1')['c5b'].sum()

        # Mostrar el DataFrame resultante
    return result_df


    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
