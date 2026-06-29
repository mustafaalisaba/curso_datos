import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Fase 2: Extracción de insights (correlaciones)
# def alertasCadenaFrio(dataset):
    # Alertas de Cadena de Frío: Evaluar si las variaciones en iot_temperature tienen
    # una relación directa con el estado final de la carga (cargo_condition_status).


def fuel_consumption(dataset):
    # Rendimiento de Operadores: Cruzar el score de fatiga (fatigue_monitoring_score) 
    # con el comportamiento del conductor (driver_behavior_score) para ver si impactan 
    # el consumo de combustible (fuel_consumption_rate)

    print("\n----- Correlaciones -----\n fatigue_monitoring_score \n driver_behavior_score \n fuel_consumption_rate")

    variables = [
        "fatigue_monitoring_score",
        "driver_behavior_score",
        "fuel_consumption_rate"
    ]

    corr = dataset[variables].corr(method="pearson")

    print(corr.round(3))

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        data=dataset,
        x="fatigue_monitoring_score",
        y="driver_behavior_score",
        hue="fuel_consumption_rate",
        palette="viridis",
        alpha=0.6
    )

    plt.title("Fatiga vs Comportamiento del conductor")
    plt.xlabel("Fatigue Monitoring Score")
    plt.ylabel("Driver Behavior Score")

    plt.show()

def impactoExternoTiempos(dataset):
    # Impacto Externo en Tiempos: Analizar la correlación directa entre 
    # delivery_time_deviation y factores exógenos como weather_condition_severity y port_congestion_level

    print("\n----- Correlaciones -----")

    corr = dataset[
    [
        "delivery_time_deviation",
        "weather_condition_severity",
        "port_congestion_level"
    ]
    ].corr()

    print(corr.round(3))


# Fase 1: Data Cleaning & Transformación

def manejoBalanceo(dataset):
    # (2) Manejo de Desbalanceo: Aislar y documentar la distribución 
    # de risk_classification, ya que la gran mayoría (23,944 registros) 
    # está catalogada como "High Risk".
    riesgos = dataset.risk_classification
    
    # Risk Classification: A categorical classification indicating the level of risk (Low Risk, Moderate Risk, High Risk).

    riesgo_bajo = dataset.loc[riesgos == 'Low Risk']
    
    riesgo_moderado = dataset.loc[riesgos == 'Moderate Risk']

    riesgo_alto = dataset.loc[riesgos == 'High Risk']

    print("\n----- RIESGO BAJO -----")
    print(riesgo_bajo)
    
    print("\n----- RIESGO MODERADO -----")
    print(riesgo_moderado)
    
    print("\n----- RIESGO ALTO -----")
    print(riesgo_alto)

    frecuencia = dataset["risk_classification"].value_counts() # absoluta

    porcentaje = dataset["risk_classification"].value_counts(normalize=True) * 100 # relativa

    distribucion = pd.DataFrame({
        "Frecuencia": frecuencia,
        "Porcentaje": porcentaje.round(2)
    })

    print("\n----- FRECUENCIAS ABSOLUTAS Y REALTIVAS -----")
    print(distribucion)

    print("\n----- Generando gráfico de barras -----")

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(6, 4))

    sns.countplot(
        data=dataset,
        x="risk_classification",
        order=dataset["risk_classification"].value_counts().index
    )

    plt.title("Distribución de Risk Classification")
    plt.xlabel("Clase")
    plt.ylabel("Número de registros")

    plt.tight_layout()
    plt.show()

    # plt.figure(figsize=(6,4))
    # frecuencia.plot(kind="bar")

    # plt.title("Distribución de Risk Classification")
    # plt.xlabel("Clase")
    # plt.ylabel("Número de registros")

    # plt.show()

    mayor = frecuencia.max()
    menor = frecuencia.min()

    print(f"Relación Mayor/Menor: {mayor/menor:.2f}:1")

def validacionIntegridad(dataset):
    # (1) Validación de Integridad: Aunque el dataset reporta 32,065 registros sin nulos, 
    # se deben revisar los valores atípicos (outliers). Por ejemplo, delivery_time_deviation 
    # tiene valores negativos (mínimo -1.99); verificar si representan entregas 
    # anticipadas o errores de captura.

    registro_entregas = dataset.delivery_time_deviation

    print(f"-----Resumen estadístico para 'delivery_time_deviation'----- \n {registro_entregas.describe()}")

    # Cuantos registros tienene 10hrs
    # registro_mayores_10 = (dataset["delivery_time_deviation"] == 10).sum()

    # print(registro_mayores_10)

    registros_negativos = dataset[dataset["delivery_time_deviation"] < 0]

    print(f"-----Registros negativos de 'delivery_time_deviation'----- \n {registros_negativos['delivery_time_deviation']}")

    total_registros_negativos = (dataset["delivery_time_deviation"] < 0).sum()

    print(f"-----Total de registros negativos de 'delivery_time_deviation'----- \n {total_registros_negativos}")

    columnas = [
        "delivery_time_deviation", # The deviation in hours from the expected delivery time
        "traffic_congestion_level", # The level of traffic congestion affecting the logistics route (scale 0-10).
        "weather_condition_severity", # The severity of weather conditions affecting operations (scale 0-1).
        "delay_probability", # The probability of a shipment being delayed (scale 0-1)
        "route_risk_level", # The risk level associated with a particular logistics route (scale 0-10)
        "eta_variation_hours" # The difference between the estimated and actual arrival times.
    ]

    registros_negativos_df = dataset.loc[dataset["delivery_time_deviation"] < 0, columnas]

    print("\n----- REGISTROS NEGATIVOS -----")

    print(registros_negativos_df[columnas].head(20))

    registros_negativos_sort_df = (dataset.loc[dataset["delivery_time_deviation"] < 0, columnas]).sort_values("delivery_time_deviation")

    print(registros_negativos_sort_df[columnas].head(10))

    print("\n----- REGISTROS POSITIVOS -----")

    registros_positivos = dataset.loc[dataset["delivery_time_deviation"] >= 0, columnas]

    print(registros_positivos[columnas].head(10))

    print("\n----- ESTADISTICAS -----")

    print("Negativos")

    print(registros_negativos_df[columnas].describe())

    print("\nPositivos")

    print(registros_positivos[columnas].describe())

    print("\n----- CORRELACIÓN ESTADÍSTICA -----")

    print(dataset[columnas].corr())

    sns.set_theme(style="whitegrid")

    print("\n----- Generando histograma -----")

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=dataset,
        x="delivery_time_deviation",
        bins=30,
        kde=False
    )

    plt.axvline(0, color="red", linestyle="--", linewidth=2, label="0 horas")

    plt.title("Distribución de Delivery Time Deviation")
    plt.xlabel("Delivery Time Deviation (horas)")
    plt.ylabel("Frecuencia")
    plt.legend()

    plt.tight_layout()
    plt.show()


    print("\n----- Generando gráfica de dispersión -----")

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=dataset,
        x="eta_variation_hours",
        y="delivery_time_deviation",
        alpha=0.5,
        s=20
    )

    plt.title("ETA Variation vs Delivery Time Deviation")
    plt.xlabel("ETA Variation (horas)")
    plt.ylabel("Delivery Time Deviation (horas)")

    plt.tight_layout()
    plt.show()
    # print("\n----- Generando histograma -----")

    # plt.hist(dataset["delivery_time_deviation"], bins=30)
    # plt.axvline(0, color="red")
    # plt.xlabel("Delivery Time Deviation")
    # plt.ylabel("Frecuencia")
    # plt.show()
    
    # print("\n----- Generando gráfica de dispersión -----")

    # plt.figure(figsize=(7,5))
    # plt.scatter(dataset["eta_variation_hours"],
    #             dataset["delivery_time_deviation"],
    #             alpha=0.5)

    # plt.xlabel("ETA Variation")
    # plt.ylabel("Delivery Time Deviation")
    # plt.grid(True)
    # plt.show()

    print("\n----- Correlaciones -----")

    corr = dataset[
    [
    "delivery_time_deviation",
    "eta_variation_hours",
    "delay_probability",
    "traffic_congestion_level",
    "route_risk_level"
    ]
    ].corr()

    print(corr.round(3))
    # # Order Fulfillment Status: Status indicating whether the order was fulfilled on time (0 = not fulfilled, 1 = fulfilled).
    # estado_completado_orden = [dataset.order_fulfillment_status > 1.0]

    # print(estado_completado_orden)

    # print("\nHistograma")
    # desv_tiempo_entrega.plot(kind='hist')
    # plt.show()

def datasetGenerator():
    
    print("(1. Cargando el dataset...)")

    try:
        
        transporte_df = pd.read_csv('datos_crudos/dynamic_supply_chain_logistics_dataset.csv')
        
        return transporte_df
    
    except FileNotFoundError:
        
        print('Error al cargar datos')

        return

def datasetInformation(df):

    print(df.info())

    print(f"\n--- Estadísticas descriptivas ---\n{df.describe().T}")

    print(f"\n--- Total de datos nulos ---\n{df.isnull().sum()}")

    print(f"\n--- Datos duplicados ---\n{df.duplicated().sum()}")

# def data_cleaning(data_frame):
#     clean_dataframe = pd.DataFrame

#     # obtengo un valor del dataset
#     df_new_data = data_frame[data_frame['vehicle_gps_latitude'] == 32065]

#     return df_new_data

def datasetCleaning(df):
    clean_df = df.dropna()

    # print(clean_df.to_string())

    return clean_df

def timestampStats(df):

    print(f"\n------ Análisis Exploratorio de Datos ------\n")
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    fecha_minima = df["timestamp"].min()
    fecha_maxima = df["timestamp"].max()
    fecha_promedio = pd.to_datetime(df["timestamp"].astype("int64").mean())

    print(f"Fecha Mínima (Inicio): {fecha_minima}")
    print(f"Fecha Máxima (Fin):    {fecha_maxima}")
    print(f"Fecha Promedio (Media): {fecha_promedio}")

    # Cuantos días, horas o años cubre el dataset
    duracion_total = fecha_maxima - fecha_minima
    print(f"Duración total del dataset: {duracion_total}")

    # Si la mediana es muy diferente de la media, hay mas datos acumulados de una fecha que de otra.
    fecha_mediana = pd.to_datetime(df["timestamp"].astype("int64").median())
    print(f"Mediana de las fechas: {fecha_mediana}")

    # Calcular la diferencia entre registros consecutivos
    df["diferencia_tiempo"] = df["timestamp"].diff() #ayuda para ver si faltan datos
    
    # Ver cuál es el intervalo más común (Moda)
    intervalo_comun = df["diferencia_tiempo"].mode()[0]
    print(f"Intervalo más común entre registros: {intervalo_comun}")

    # Desviación estándar expresada en días
    desviacion_dias = pd.to_timedelta(df["timestamp"].astype("int64").std()).days
    print(f"Dispersión (Desviación estándar): {desviacion_dias} días")

def datasetEDA(df):
    # Ordena los datos de forma ascendente. Prepara las subtablas que van a graficarse
    print(f"\n------ Análisis Exploratorio de Datos ------\n")
    
    df["timestamp"] = pd.to_datetime(df["timestamp"]) #año, mes, día y hora

    # 2. Extraer los componentes temporales
    df['Año'] = df['timestamp'].dt.year
    df['Mes'] = df['timestamp'].dt.month
    df['Hora'] = df['timestamp'].dt.hour

    print(df['Año'])
    print(df['Mes'])
    print(df['Hora'])

    return

def datasetPlotter(df):

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 6))

    # sns.lineplot(
    #     data=df.head(10), 
    #     x='weather_condition_severity',
    #     y='route_risk_level',
    #     color='crimson',
    #     errorbar='ci' # Esto calcula automáticamente la sombra del intervalo de confianza
    # )

    # plt.title('¿Aumenta el riesgo al aumentar los costos de envío?', fontsize=14, fontweight='bold')
    # plt.xlabel('weather_condition_severity')
    # plt.ylabel('Nivel de Riesgo de la Ruta (route_risk_level)')

    sns.regplot(
    data=df,
    x='shipping_costs',
    y='route_risk_level',
    scatter_kws={'alpha': 0.1, 'color': 'gray'}, # Puntos semi-transparentes de fondo
    line_kws={'color': 'red', 'linewidth': 2}     # Línea de tendencia clara
    )

    plt.title('Tendencia de Riesgo vs Costo de Envío', fontsize=14, fontweight='bold')
    plt.xlabel('Costo de Envío')
    plt.ylabel('Nivel de Riesgo')

    plt.show()

if __name__=='__main__':
    transporte_df = datasetGenerator()
    
    # print("Información del dataframe:")
    # print(df_transporte.info())

    # print(df_transporte.T) # verifica todas las columnas
    
    # Calcula la información que concierne al dataset
    # dataset_info = datasetInformation(transporte_df)

    # print(dataset_info)

    # dataset_clean = datasetCleaning(transporte_df)

    # print(dataset_clean.T)

    # # time_stats = timestampStats(transporte_df)

    # dataset_stats = datasetEDA(transporte_df)

    # print(dataset_stats)

    # datasetPlotter(transporte_df)

    # dataset_clean = data_cleaning(df_transporte)
    # print("-"*100)
    # print(dataset_clean)

    # Proyecto semana 2

    # desv_tiempo_entrega = validacionIntegridad(transporte_df)

    # alto_riesgo = manejoBalanceo(transporte_df)

    # print(desv_tiempo_entrega)

    # print(alto_riesgo)

    # correlaciones_fase_2 = correlations(transporte_df)

    consumo_gasolina = fuel_consumption(transporte_df)