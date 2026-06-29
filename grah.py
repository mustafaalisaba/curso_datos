import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exec_macro_analysis():

    print("1. Cargando datasets...")

    try:
        df_fraud = pd.read_csv('master_fraud_data.csv')
        df_motor = pd.read_csv('master_motor_data.csv')
    except FileNotFoundError:
        print('Error al cargar datos')
        return
    
    print('2. Estandarizando dimensiones en común...')

    df_fraud['Make_Normalizado'] = df_fraud['Make'].astype(str).str.upper().str.strip()
    df_motor['Make_Normalizado'] = df_motor['MAKE'].astype(str).str.upper().str.strip()

    # print(df_fraud['Make_Normalizado'])
    # print(df_motor['Make_Normalizado'])

    print("3. Calculando tendencias del dataset Fraude...")
    # Nombre de tu nueva columna = ('col original', 'operacion')
    
    tendencia_fraud = df_fraud.groupby('Make_Normalizado').agg(
        Tasa_Fraude_Porcentaje=('FraudFound_P', lambda x: x.mean() * 100), #agrega las cols a la nueva tabla tendencia_fraud
        Total_Polizas_Fraude=('PolicyNumber', 'count')
    ).reset_index()

    tendencia_motor = df_motor.groupby('Make_Normalizado').agg(
        Promedio_Reclamo_Pagado=('CLAIM_PAID', 'mean'),
        Promedio_Prima_Cobrada=('PREMIUM', 'mean'),
        Total_Polizas_Motor=('OBJECT_ID', 'count')
    ).reset_index()

    # print("5. Cruzando los universos (inner-join por macro-tendencias)...")

    # macro_analisis = pd.merge(tendencia_fraud, tendencia_motor, on='Make_Normalizado', how='inner')

    # macro_analisis = macro_analisis[macro_analisis['Total_Polizas_Fraude'] > 30]

    # macro_analisis = macro_analisis.sort_values(by='Tasa_Fraude_Porcentaje', ascending=False)

    # macro_analisis.to_csv('resultados_macro_tendencias.csv', index=False)
    # print("Archivo creado con éxito")

    # print("7. Generando visualización de datos...")
    # generar_graficas(macro_analisis)

def generar_graficas(df):
    
    sns.set_theme(style='whitegrid')

    fig, axes = plt.subplots(1,2,figsize=(16,6))
    
    sns.barplot(
        data=df.head(10),
        x='Tasa_Fraude_Porcentaje',
        y='Make_Normalizado',
        ax = axes[0],
        palette='Reds_r'
    )

    axes[0].set_title('Top 10: Tasa de fraude por marca (%)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Tasa de Fraude (%)')
    axes[0].set_ylabel('Marca del vehículo')

    sns.barplot(
        data=df.head(10),
        x='Promedio_Reclamo_Pagado',
        y='Make_Normalizado',
        ax = axes[1],
        palette='Blues_r'
    )

    axes[0].set_title('Costo promedio del reclamo para estas marcas (%)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Promedio pagado por reclamo')
    axes[0].set_ylabel('')

    plt.show()

if __name__=='__main__':
    exec_macro_analysis()