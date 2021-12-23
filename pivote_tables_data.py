import os
import pandas as pd
import numpy as np

def pivote_table():
    os.chdir('detalles')
    cwd = os.path.abspath('')
    print(cwd)
    files = os.listdir(cwd)
    print(files)

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xlsx') and not file.startswith('~'):
            df = df.append(pd.read_excel(file), ignore_index=True)
    #detail_file = 'detalle_'+activo_name+'.xlsx'

    print( df.shape)
    print(df.head())
    print('pivoting table')
    df_pivoted = pd.pivot_table(df, index=['fecha'], values=['Precio Cierre'], columns='Nemotecnico')
    print(df_pivoted.head())
    print(df_pivoted.shape)
    os.chdir('..')
    df_pivoted.to_excel('detalle_consolidado.xlsx')
    

def main():
    pivote_table()

if __name__ == "__main__":
    main()