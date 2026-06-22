from functools import reduce

numeros = [1,2,3,4,5]

suma = reduce(lambda actual, acumulador: acumulador + actual, numeros) # reduce(func, iter, [value])

print(suma)

numeros = [2,3,4]
product = reduce(lambda acc, x: acc * x, numeros)

numeros = [100,2,5,4]
div = reduce(lambda acc, x: acc / x, numeros)

numeros = [2,3,4]
squares = reduce(lambda acc, x: acc + (x**2), numeros,0)


numeros = [15,8,42,4,23]
mayor = reduce(lambda acc, x: acc if acc > x else x, numeros)

valores = [True, True, False, True]
verdaderos = reduce(lambda acc, x: acc and acc, valores)

print(verdaderos)

palabras = ['python', 'es', 'muy', 'poderoso']
frase = reduce(lambda acc, x: acc + ' ' + x, palabras)

letras=['a','b','a','c','a']
conteo = reduce(lambda acc, x: acc + 1 if x == "a" else acc, letras, 0)

texto='hola'
invertido= reduce(lambda acc, x: x + acc, texto)

listas = [[1,2], [3,4], [5,6]]
aplanada = reduce(lambda acc, x: acc + x, listas)

conjuntos = [{1,2,3},{2,3,4},{3,5}]
comunes = reduce(lambda acc, x: acc & x, conjuntos)

# TAREA
elementos = ['manzana', 'pera', 'manzana', 'uva', 'pera']
frecuencias = reduce(lambda acc, x: {**acc, x: acc.get(x, 0) + 1}, elementos, {})
# Resultado: {'manzana': 2, 'pera': 2, 'uva': 1}
# acc= {'manzana':2}, x = 'pera'
# acc={'pera':2}

numeros = [1, 2, 3, 4, 5, 6]
agrupados = reduce(
    lambda acc, x: {**acc, 'pares': acc['pares'] + [x]} if x % 2 == 0 else {**acc, 'impares': acc['impares'] + [x]}, 
    numeros, 
    {'pares': [], 'impares': []}
)
# Resultado: {'pares': [2, 4, 6], 'impares': [1, 3, 5]}

ventas_sucursales = [
    {'a': 10, 'b': 3, 'c': 4},
    {'a': 13, 'b': 13, 'c': 14},
    {'a': 6, 'b': 22}
]

def cons(acumulador: dict, reporte_actual: dict) -> dict:
    '''Toma el reporte maestro acumulado y le suma las ventas de la siguiente sucursal.
    Si la categoría no existe en el maestro, la crea'''

    nuevo_dic = acumulador.copy()

    for key,value in reporte_actual.items():

        if key in nuevo_dic:
            nuevo_dic[key] = nuevo_dic[key] + value
        else:
            nuevo_dic[key] = value
    
    return nuevo_dic

reporte = reduce(cons, ventas_sucursales, {})

print(reporte)