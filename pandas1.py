import pandas as pd
import numpy as np
import io

def pandas_seguros():
    csv_sucio = """ID_Poliza,Edad_Asegurado,Vehiculo,Monto_Reclamo,Estado_Reclamo
    POL-001,35,VW Jetta,15000.50,Aprobado
    POL-002,,Chevrolet Spark,,Pendiente
    POL-003,19,VW Jetta,8500.00,Rechazado
    POL-004,42,Camioneta,45000.00,Aprobado
    POL-005,999,Chevrolet Spark,12000.00,Aprobado
    POL-006,28,Camioneta,,Rechazado
    """

    dataframe_siniestros = pd.read_csv(io.StringIO(csv_sucio))
    print(type(dataframe_siniestros))
    print("Visualizacion de dataframe:")
    print(dataframe_siniestros)

    dataframe_siniestros.info()

    # print(dataframe_siniestros['ID_Poliza'][2])

    # print(dataframe_siniestros['Vehiculo']['VW Jetta'])
    print()
    # todos los valores donde los vehiculos son jetta
    jetta = dataframe_siniestros[dataframe_siniestros['Vehiculo'] == 'VW Jetta']
    print(jetta)

    # otra forma de hacerlo
    jetta2 = dataframe_siniestros.loc[dataframe_siniestros['Vehiculo'] == 'VW Jetta']
    print(jetta2)

    # dropna borra datos nulos
    df_limpio = dataframe_siniestros.dropna(subset=['Monto_Reclamo']).copy()

    df_limpio.loc[df_limpio['Edad_Asegurado'] > 100, 'Edad_Asegurado'] = np.nan

    edad_promedio = df_limpio['Edad_Asegurado'].mean()

    df_limpio['Edad_Asegurado'] = df_limpio['Edad_Asegurado'].fillna(edad_promedio)

    print(df_limpio)

if __name__=='__main__':
    pandas_seguros()