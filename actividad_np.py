import numpy as np

print("=== SISTEMA DE ANÁLISIS: BARRA DE ESPRESSO ===")

# --------------------------------------------------------
# RETO 1: Vectorización y Matemáticas Elementales
# Tenemos las ventas de 4 bebidas: Espresso, Americano, Latte, Flat White
# --------------------------------------------------------
lista_tazas_vendidas = [18, 45, 30, 12]
lista_precios_mxn = [35.0, 40.0, 65.0, 70.0]

# todo 1: Convierte las dos listas estándar a Arrays de NumPy
tazas_array = np.array(lista_tazas_vendidas)
precios_array = np.array(lista_precios_mxn)

# todo 2: Calcula el subtotal generado por cada tipo de bebida e imprimelo
subtotal = tazas_array*precios_array
print(f'Subtotal: {subtotal}')

# --------------------------------------------------------
# RETO 2: Estadística Instantánea
# El gerente necesita el corte de caja con 4 métricas clave.
# --------------------------------------------------------

# todo 3: Utiliza las funciones estadísticas de NumPy para calcular e imprimelo:
ingreso_total = np.sum(subtotal) # TU CÓDIGO AQUÍ (Suma total)
print(ingreso_total)

venta_maxima = np.max(subtotal) # TU CÓDIGO AQUÍ (El subtotal más alto)
print(venta_maxima)

venta_promedio = np.mean(subtotal) # TU CÓDIGO AQUÍ (Promedio de los subtotales)
print(venta_promedio)

venta_mediana = np.median(subtotal) # TU CÓDIGO AQUÍ (La mediana)
print(venta_mediana)

# --------------------------------------------------------
# RETO 3: Lógica Condicional
# --------------------------------------------------------

# todo 4: Usa np.where para clasificar las bebidas. 
# Si el subtotal de la bebida superó los $1,000, etiquétala como "Top Ventas". 
# Si no, etiquétala como "Venta Regular".

clasificacion = np.where(subtotal > 1000.0, 'Top Ventas', 'Venta Regular')
print(subtotal)
print(clasificacion)

# --------------------------------------------------------
# RETO 4: Anatomía de Matrices y Generadores
# --------------------------------------------------------

# Matriz de inventario actual [Kilos de Café, Litros de Leche] en 3 sucursales
tabla_inventario = np.array([
    [5.5, 12.0],
    [2.0, 18.5],
    [8.2, 5.0]
])

# todo 5: Extrae y muestra las dimensiones de la tabla_inventario usando .shape
dimensiones = tabla_inventario.shape
print(f'dimensiones: {dimensiones}')

# todo 6: Genera los IDs para los 4 baristas del turno usando np.arange (Tienen que ser: 1001, 1002, 1003, 1004)

# todo 7: Crea una matriz de 2x2 llena de ceros (np.zeros) para inicializar el contador de mermas del día