from functools import reduce
import numpy as np

class PolizaCliente:
    def __init__(self, id_poliza, edad_conductor, tipo_vehiculo, siniestros_anio, prima_base):
        self.id_poliza = id_poliza
        self.edad_conductor = edad_conductor
        self.tipo_vehiculo = tipo_vehiculo
        self.siniestros_anio = siniestros_anio
        self.prima_base = prima_base

    def __str__(self):
        return f"[Póliza {self.id_poliza}] | Edad: {self.edad_conductor} | Siniestros: {self.siniestros_anio} | Prima: ${self.prima_base:,.2f}"

def main_seguros():
    print("=== SISTEMA DE EVALUACIÓN DE RIESGO DE SEGUROS ===")
    
    cartera = [
        PolizaCliente("POL-101", 35, "Sedan", 0, 8500000),
        PolizaCliente("POL-102", 22, "Deportivo", 2, 14000), 
        PolizaCliente("POL-103", 45, "SUV", 1, 11000),
        PolizaCliente("POL-104", 19, "Moto", 3, 9500),      
        PolizaCliente("POL-105", 50, "Sedan", 0, 7200)
    ]

    print("\n1. Primas ajustadas por inflación (8%):")
    # TODO 1: MAP + LAMBDA
    # Requerimiento: A partir de la cartera, genera una colección con los valores de las 
    # primas base actualizadas aplicando un aumento por inflación del 8%.
    # Imprime los nuevos valores.
    ajuste_inflacion = 1.08

    nuevas_primas = list(map(lambda p: PolizaCliente(p.id_poliza, p.edad_conductor, p.tipo_vehiculo, p.siniestros_anio, p.prima_base * ajuste_inflacion), cartera))

#     nuevas_primas = list(map(lambda p: (
#     print(f"Valor: {p} | Tipo: {type(p)}"), # <-- Esto imprime en cada iteración
#     PolizaCliente(p.id_poliza, p.edad_conductor, p.tipo_vehiculo, p.siniestros_anio, p.prima_base * ajuste_inflacion)
# )[1], cartera))
    print(nuevas_primas[0])
    for proyeccion in nuevas_primas:
        print(proyeccion)

    print("\n2. Conductores de Alto Riesgo:")
    # TODO 2: FILTER + LAMBDA
    # Requerimiento: Aísla y muestra SOLO los objetos PolizaCliente de conductores clasificados 
    # como "Alto Riesgo" (menores de 25 años que además tengan 2 o más siniestros en el año).
    detectados = list(filter(lambda p: p.edad_conductor < 25 and p.siniestros_anio >= 2, nuevas_primas))

    for riesgosos in detectados:
        print(riesgosos)

    print("\n3. Valor total asegurado de la cartera base:")
    # TODO 3: REDUCE + LAMBDA
    # Requerimiento: Calcula e imprime la suma de todas las primas BASE originales 
    # de toda la cartera de clientes.
    solo_gran_total = reduce(lambda acc, p: acc + p.prima_base, cartera, 0)
    print(f"${solo_gran_total:,.2f}")


    print("\n4. Análisis masivo de siniestros históricos (Numpy):")
    # TODO 4: NUMPY
    # Requerimiento:
    # A) Simula 5,000 costos de siniestros históricos usando un arreglo de números enteros aleatorios (entre $5,000 y $250,000).
    # B) Mediante operaciones vectorizadas, resta un deducible fijo de $3,000 a todos los siniestros generados.
    # C) Si tras aplicar el deducible el valor resultante es negativo, ajusta ese valor a 0 (la aseguradora no paga negativo).
    # D) Calcula e imprime el costo promedio pagado por la aseguradora y el pago máximo realizado.
    # generación del conjunto de 5,000 accidentes aleatorios entre $5,000 y $250,000
    rng = np.random.default_rng(seed=42) #seed es para reproducir los datos
    # print(rng)
    costos_originales = rng.uniform(5000, 250000, size=5000) #size es el total de siniestros
    print(costos_originales)
    pagos_preliminares = costos_originales - 3000 # resta del deducible fijo

    pagos_reales = np.where(pagos_preliminares < 0, 0, pagos_preliminares)

    costo_promedio = np.mean(pagos_reales)

    pago_maximo = np.max(pagos_reales)

    print(f"Costo promedio pagado: ${costo_promedio:,.2f}")
    print(f"Pago máximo realizado: ${pago_maximo:,.2f}")

if __name__ == "__main__":
    main_seguros()