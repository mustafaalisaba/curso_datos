import pandas as pd
import numpy as np

def extraer_datos():
    df_fraud = pd.read_csv('datos_crudos/fraud_oracle.csv')
    df_motor1 = pd.read_csv('datos_crudos/motor_data11-14lats.csv')
    df_motor2 = pd.read_csv('datos_crudos/motor_data14-2018.csv')

    return df_fraud, df_motor1, df_motor2

def transformar_datos(df_fraud, df_motor1, df_motor2):
    df_motor = pd.concat([df_motor1, df_motor2], ignore_index=True)
    df_motor = df_motor.drop_duplicates()

    df_fraud['Age'] = df_fraud['Age'].replace(0, np.nan) #sustituye nan por 0
    edad_promedio = df_fraud['Age'].mean() # calcula su promedio
    df_fraud['Age'] = df_fraud['Age'].fillna(edad_promedio) #llenalo con el promedio

    df_motor['CLAIM_PAID'] = df_motor['CLAIM_PAID'].fillna(0.0)

    df_motor = df_motor.loc[df_motor['PREMIUM'] > 0]

    df_motor['CARRYING_CAPACITY'] = df_motor['CARRYING_CAPACITY'].fillna(df_motor['CARRYING_CAPACITY'].median())
    df_motor['SEATS_NUM'] = df_motor['SEATS_NUM'].fillna(df_motor['SEATS_NUM'].median())

    moda_anio = df_motor['PROD_YEAR'].mode()[0]
    df_motor['PROD_YEAR'] = df_motor['PROD_YEAR'].fillna(moda_anio)

    df_motor = df_motor.dropna()

    return df_fraud, df_motor

def cargar_datos(df_fraud, df_motor):
    print('Exportando datasets maestros')
    df_fraud.to_csv('master_fraud_data.csv', index=False)
    df_motor.to_csv('master_motor_data.csv', index=False)
    print('Pipeline ejecutado correctamente.')

if __name__=='__main__':
    fraud, motor1, motor2 = extraer_datos()
    df_fraud_clean, df_motor_clean = transformar_datos(fraud, motor1, motor2)
    cargar_datos(df_fraud_clean, df_motor_clean)
