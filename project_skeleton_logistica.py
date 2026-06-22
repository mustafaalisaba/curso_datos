from functools import reduce
import numpy as np

class CamionReparto:
    def __init__(self, id_camion, distancia_km, km_por_litro, num_paquetes):
        self.id_camion = id_camion
        self.distancia_km = distancia_km
        self.km_por_litro = km_por_litro
        self.num_paquetes = num_paquetes

    def __str__(self):
        return f"[Camión {self.id_camion}] | {self.distancia_km} km | Rendimiento: {self.km_por_litro} km/l"

def main_logistica():
    print("=== SISTEMA DE GESTIÓN DE FLOTILLAS ===")
    PRECIO_GASOLINA = 24.50  # Precio por litro en pesos

    flotilla = [
        CamionReparto("CAM-01", 120, 10.5, 45),
        CamionReparto("CAM-02", 350, 7.2, 120),
        CamionReparto("CAM-03", 85, 12.0, 30),
        CamionReparto("CAM-04", 410, 6.5, 150),
        CamionReparto("CAM-05", 200, 9.8, 80)
    ]

    print("\n1. Costos de combustible por camión:")
    # TODO 1: MAP + LAMBDA
    # Requerimiento: Crea una lista que contenga el costo de combustible estimado para cada camión en pesos.
    # Imprime la lista resultante.
    
    
    print("\n2. Camiones que requieren mantenimiento urgente:")
    # TODO 2: FILTER + LAMBDA
    # Requerimiento: Filtra la flotilla para obtener y mostrar SOLO los objetos CamionReparto 
    # que tengan un rendimiento inferior a 8 km por litro.
    
    
    print("\n3. Costo operativo total de la flotilla:")
    # TODO 3: REDUCE + LAMBDA
    # Requerimiento: Utilizando la lista de costos generada en el TODO 1, calcula e imprime 
    # el costo total de combustible de toda la flotilla.
    
    
    print("\n4. Simulación masiva de peso de paquetes (Numpy):")
    # TODO 4: NUMPY
    # Requerimiento:
    # A) Simula el peso en kg de 10,000 paquetes utilizando un arreglo de números enteros aleatorios (entre 1 y 100).
    # B) Encuentra cuántos de estos paquetes se consideran "pesados" (peso estrictamente mayor a 50 kg).
    # C) Imprime la cantidad de paquetes pesados y la desviación estándar de la simulación completa.
    
    

if __name__ == "__main__":
    main_logistica()