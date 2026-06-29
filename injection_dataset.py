import pandas as pd
import os
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv

def pipeline():

    print("1. Cargando variables de entonro...")

    load_dotenv()

    usuario = "root"
    password = os.getenv("DB_ROOT_PASSWORD")
    base_datos = os.getenv("DB_NAME")
    puerto = os.getenv("DB_PORT_LOCAL")

    print("2. Conectando a MySQL...")

    cadena_conexion = f"mysql+pymysql://{usuario}:{password}@localhost:{puerto}/{base_datos}"
    
    engine = create_engine(cadena_conexion)

    archivos_config = {
        'master_fraud_data.csv':('polizas_maestro','PolicyNumber'),
        'master_motor_data.csv':('clientes_detalle','OBJECT_ID'),
        'resultados_macro_tendencias.csv':('resumen_tendencia','Make_Normalizado')
    }