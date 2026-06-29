import numpy as np
import time

def demo():
    cantidad_siniestros = 1_000_000
    print(cantidad_siniestros)
    print(type(cantidad_siniestros))

    costos = np.random.randint(2000, 350000, size=cantidad_siniestros)
    print(type(costos))
    lista_costo = costos.tolist()

    print(lista_costo[1])

    inicio_py = time.time() 
    deducible_py = []
    for costo in lista_costo:
        deducible_py.append(costo*0.1)

    fin_py = time.time()
    tiempo_py = fin_py - inicio_py
    
    inicio_np = time.time()
    deducible_np = costos*0.1
    fin_np = time.time()
    tiempo_np = fin_np - inicio_np

    print(f"tiempo calculando 1M de deducibles con for y listas: {tiempo_py:.5f} segundos")
    print(f"tiempo calculando 1M de deducibles con numpy: {tiempo_np:.5f} segundos")
    print(f"numpy fue {(tiempo_py / tiempo_np):.2f} mas rápido. ")

    mascara_casos_graves = costos > 200000
    print(mascara_casos_graves)
    print(len(mascara_casos_graves))

    siniestros_graves = costos[mascara_casos_graves]
    print(siniestros_graves)
    print(len(siniestros_graves))

    print(f"de 1M de choques, {len(siniestros_graves)} costaron mas de 200k")
    print(f"probabilidad de sinistros graves mayor a 200k: {(len(siniestros_graves)/len(mascara_casos_graves))*100:.2f}")

    promedio= np.mean(costos)
    costo_maximo = np.max(costos)
    desviacion = np.std(costos)

    print("Promedio de cotos, máximo y desviación estándar")
    print(promedio)
    print(costo_maximo)
    print(desviacion)

if __name__ == '__main__':
    demo()