# Modelos de datos y estructura base
from functools import reduce
import numpy as np

class PolizaCliente:
    """Clase principal de poliza de cliente"""
    def __init__(self, id_poliza, edad_cliente, tipo_vehiculo, num_siniestros, prima_base):
        self.id_poliza = id_poliza
        self.edad_cliente = edad_cliente
        self.tipo_vehiculo = tipo_vehiculo
        self.num_siniestros = num_siniestros
        self.prima_base = prima_base
    
    def __str__(self):
        """formato de poliza en texto"""
        return f"[{self.id_poliza}] | Edad: {self.edad_cliente} | Vehículo: {self.tipo_vehiculo} | Siniestro: {self.num_siniestros} | Prima: {self.prima_base}]"

def simular_impacto_siniestros():

    # generación del conjunto de 5,000 accidentes aleatorios entre $5,000 y $250,000
    rng = np.random.default_rng(seed=42) #seed es para reproducir los datos
    # print(rng)
    costos_originales = rng.uniform(5000, 250000, size=5000) #size es el total de siniestros
    print(costos_originales)
    pagos_preliminares = costos_originales - 3000 # resta del deducible fijo

    pagos_reales = np.where(pagos_preliminares < 0, 0, pagos_preliminares)

    costo_promedio = np.mean(pagos_reales)

    pago_maximo = np.max(pagos_reales)

    return costo_promedio, pago_maximo

def valor_total_cartera(polizas_clientes):
    """acumulación de las primas base en un solo gran total"""
    solo_gran_total = reduce(lambda acc, p: acc + p.prima_base, polizas_clientes, 0)
    
    return solo_gran_total

def deteccion_conductores_riesgosos(cartera_proyectada):
    """detecta conductores riesgosos menores de 25 años y con 2 o mas siniestros"""
    detectados = list(filter(lambda p: p.edad_cliente < 25 and p.num_siniestros >= 2, cartera_proyectada))

    return detectados

def ajuste_inflacionario_primas(polizas_clientes):
    """ajuste de primas debido a la inflación"""    
    ajuste_inflacionario = 1.08

    nuevas_primas = list(map(lambda p: PolizaCliente(p.id_poliza, p.edad_cliente, p.tipo_vehiculo, p.num_siniestros, p.prima_base * ajuste_inflacionario), polizas_clientes))

    return nuevas_primas

def main():
    polizas_clientes = [
        PolizaCliente("POL-101", 35, "Sedán", 0, 8500),
        PolizaCliente("POL-102", 22, "Deportivo", 2, 14200),
        PolizaCliente("POL-103", 58, "SUV", 1, 9800),
        PolizaCliente("POL-104", 40, "Pick-up", 0, 11000)
    ]

    cartera_proyectada = ajuste_inflacionario_primas(polizas_clientes)

    clientes_riesgosos = deteccion_conductores_riesgosos(cartera_proyectada)

    valor_total = valor_total_cartera(polizas_clientes)

    promedio_siniestro, maximo_siniestro = simular_impacto_siniestros()
    
    print("\n Cartera original")
    for poliza in polizas_clientes:
        print(poliza)
    
    print("\n Cartera al próximo año con el 8%")
    for proyeccion in cartera_proyectada:
        print(proyeccion)
    
    print("\n Clientes riesgosos")
    for riesgosos in clientes_riesgosos:
        print(riesgosos)
    
    print("\n Gran Total de la Cartera")
    print(f"${valor_total:,.2f}")

    print("\n Simulación de Siniestralidad y Deducibles")
    print(f"Costo promedio pagado: ${promedio_siniestro:,.2f}")
    print(f"Pago máximo realizado: ${maximo_siniestro:,.2f}")

if __name__ == '__main__':
    main()