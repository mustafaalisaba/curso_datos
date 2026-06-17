lis=['1','2','3']

ints = map(int, lis)

# print(ints)

# 1. Dada una lista en mayusculas, convertir a minúsculas
mayusculas = ['A','B','C']
minusculas = list(map(lambda x: x.lower(), mayusculas))
print(minusculas)

nombres_mayusculas = ['Pedro Paramo', 'Norma', 'Juan']
minus = list(map(str.lower, nombres_mayusculas))
print(minus)

# 2) aplicar el método capitalize a una lista de texto
caps = list(map(lambda x: x.capitalize(), minusculas))
print(caps)

# 3) quitar espacios en blanco a una lista de correos
emails= ['juan@gmail .com', 'em ma@yahh o.com', 'musta fa ali sa ba@hotmail.com']
new_emails = list(map(lambda x: x.replace(" ", ""), emails))
print(new_emails)

# 4) aplicar una función lambda a una lista de dias, tal que solo obtengo la primera letra de cda dia
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
letras= list(map(lambda x: x[0], dias))
print(letras)

l1 = [1, 2, 3]
l2 = [10, 20, 30]
suma = list(map(lambda x,y: x+y, l1, l2))
print(suma)

lista_potencias = [2, 2, 2]
potencias=list(map(lambda x,y: pow(x,y), l1, lista_potencias))
print(potencias)

maximo = list(map(lambda x,y: max(x,y), l1,l2))
print(maximo)

coordenadas = [(10,20), (5,8), (3,1)]
ejey = list(map(lambda t: t[1], coordenadas))

empleados = [{'id':1, 'nombre':'Mustafa'}, {'id':2, 'nombre':'Ilse'}]
nombres = list(map(lambda e: e['nombre'], empleados))
print(nombres)

inventario = [
    {'sku':'A1', 'producto':'LAPTOP gamer', 'precio_str':'$1200.50', 'moneda':'USD'},
    {'sku':'B2', 'producto':'ratón Inalámbrico', 'precio_str':'€45.00', 'moneda':'EURO'},
    {'sku':'C3', 'producto':'TECLADO MECÁNICO', 'precio_str':'$85.99', 'moneda':'USD'}
]

TASA_EURO_A_USD = 1.08

def normalizar(item: dict) -> dict:
    precio_limpio = float(item['precio_str'].replace('$', '').replace('€',''))

    if item['moneda'] == 'EURO':
        precio_limpio = round(precio_limpio*TASA_EURO_A_USD, 2)

    return {
        'sku': item['sku'],
        'producto': item['producto'].title(),
        'precio_usd': precio_limpio
    }

inv_limp=list(map(normalizar, inventario))
print(inv_limp)