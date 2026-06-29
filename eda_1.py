import pandas as pd
import matplotlib.pyplot as ptl
import seaborn as sns

def ejecutar_macro_analisis():
    try:
        df_fraud = pd.read_csv('datos_crudos/fraud_oracle.csv')
        df_motor1 = pd.read_csv('datos_crudos/motor_data11-14lats.csv')
        df_motor2 = pd.read_csv('datos_crudos/motor_data14-2018.csv')
        return df_fraud, df_motor1, df_motor2
    except FileNotFoundError:
        return

def informacion(data_frame):
    dimensiones = f"dimensiones del data frame:\n {data_frame.shape}"
    # datos = f"tipos de datos del data frame:\n {data_frame.dtypes}"

    print(dimensiones)
    print()
    print(f"resumen del data frame:\n {data_frame.info()}")
    print()
    print(data_frame.head(3))
    print()
    print(data_frame.head(3).T)

def info_complementaria(data_frame):
    print('info estadistica:')
    print(data_frame.describe())
    print('')
    print(f'total de datos nulos {data_frame.isnull().sum()}')
    print(f'datos duplicados: {data_frame.duplicated().sum()}')

if __name__=='__main__':
    df_fraud, df_motor1, df_motor2 = ejecutar_macro_analisis()

    print('primeros datos de df_fraud')
    info_complementaria(df_motor1)

## Proyecto: (al menos 5 años de analisis) logistica, ventas, seguros, marketing