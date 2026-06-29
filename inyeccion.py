import pandas as pd
import os
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv

def ejecutar_pipeline_inyeccion():

    print("1. Cargando variables de entonro...")
    load_dotenv()

    usuario = "root"
    password = os.getenv("DB_ROOT_PASSWORD")
    base_datos = os.getenv("DB_NAME")
    puerto = os.getenv("DB_PORT_LOCAL")

    # Cadena de conexion:
    # dialecto+driver://usuario:contraseña@servidor:puerto/base_de_datos

    print("2. Conectando a MySQL...")
    cadena_conexion = f"mysql+pymysql://{usuario}:{password}@localhost:{puerto}/{base_datos}"
    engine = create_engine(cadena_conexion)

    archivos_config = {
        'master_fraud_data.csv':('polizas_maestro','PolicyNumber'),
        'master_motor_data.csv':('clientes_detalle','OBJECT_ID'),
        'resultados_macro_tendencias.csv':('resumen_tendencia','Make_Normalizado')
    }

    for archivo, config in archivos_config.items():

        tabla_destino = config[0]
        llave_primaria = config[1]

        print(f"\n--- Procesando: {archivo} -> Destino: Tabla '{tabla_destino}' ---")

        try:
            df = pd.read_csv(archivo)
        except FileNotFoundError:
            print(f"[!] Error: El archivo {archivo} no existe. Saltando al siguiente...")
            continue

        if 'INSR_BEGIN' in df.columns and 'INSR_END' in df.columns:
            df['INSR_BEGIN'] = pd.to_datetime(df['INSR_BEGIN'], format='%d-%b-%y')
            df['INSR_END'] = pd.to_datetime(df['INSR_END'], format='%d-%b-%y')
            print("[*] Fechas formateadas correctamente.")

        if llave_primaria not in df.columns:
            print(f"[!] ALERTA CRÍTICA: El archivo {archivo} no tiene la columna '{llave_primaria}'. Inyección abortada.")
            continue

        inspector = inspect(engine)

        if inspector.has_table(tabla_destino):
            with engine.connect() as conn:
                query = f"SELECT {llave_primaria} FROM {tabla_destino}"
                ids_existentes = pd.read_sql(query,conn)

            lista_ids_bd = ids_existentes[llave_primaria].tolist()
            df_nuevo = df[~df[llave_primaria].isin(lista_ids_bd)]
            print(f"[*] Registros en Archivo: {len(df)} | Nuevos a inyectar: {len(df_nuevo)}")    
        else:
            df_nuevo = df
            print(f"[*] Tabla nueva. Se inyectarán los {len(df_nuevo)} registros.")

        if not df_nuevo.empty:
            df_nuevo.to_sql(
                name=tabla_destino, 
                con=engine, 
                if_exists='append', 
                index=False
            )
            print(f"[OK] {len(df_nuevo)} registros inyectados con éxito en '{tabla_destino}'.")
        else:
            print("[!] No hay registros nuevos. Prevención de duplicados activada.")

if __name__ == "__main__":
    ejecutar_pipeline_inyeccion()