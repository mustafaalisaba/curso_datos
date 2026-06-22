import numpy as np

lista_cantidades = [5, 77, 10, 50, 48]

lista_precios = [6.95, 6.75, 6.5, 2.10, 1.25]

array_cantidades = np.array(lista_cantidades)

array_precios = np.array(lista_precios)

subtotal = array_cantidades*array_precios

print(subtotal)

ingreso_total = np.sum(subtotal)
venta_max = np.max(subtotal)
venta_promedio = np.mean(subtotal)
venta_mediana = np.median(subtotal)

print('\n=== REPORTE ===')
print(f'ventas : {subtotal}')
print(f'ingreso total: {ingreso_total}')
print(f'venta mas alta registrada : {venta_max:.2f}')
print(f'promedio : {venta_promedio:.2f}')
print(f'mediana : {venta_mediana:.2f}')
print(f'=='*30)

ventas = np.array([15.5, 85.00, 5.00, 120.00, 8.95, 50.0])

etiquetas = np.where(ventas > 50.0, 'venta alta', 'venta baja')

print('analisis con where')
print(f'ventas crudas: {ventas}')
print(f'clasificación: {etiquetas}\n')

transaccione = np.array([
    [10, 2.5],
    [5, 1.25],
    [24, 7.9],
    [1, 0.99]
])

dim = transaccione.shape

print(f'escaner de dim con .shape')
print(f'la matriz es \n {transaccione}')
print(f'\n reporte: {dim}')
print(f'{dim[0]} filas (transacc)')
print(f'{dim[1]} columnas (variables)')

ids = np.arange(-1, 0, 0.5) #rango generalizado, objeto de numpy
print(ids)

pts_grafica = np.linspace(0, 10, 5) # crea pts para un segmento de linea
print(pts_grafica)

mat_zeros = np.zeros((3,3))
mat_unos = np.ones((2,2))

print(mat_unos)

arr_num = np.array([1,2,'3'])
print(arr_num)
# instrucciones
# completa los TODO en el siguiente script de python usando las herramientas de numpy.
# (np.array, *, np.sum, np.mean, np.where, .shape, np.arange, np.zeros)