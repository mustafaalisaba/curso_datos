nums = [1,2,3,4,5,6]

pares= list(filter(lambda x: x%2==0, nums))

#hacer los impares 

# print(pares)

numeros=[-10,5,-3,8,0]
positivos=list(filter(lambda x: x>0,numeros))

edades = [5,12,25,45,60,8]
rango=list(filter(lambda x: 10 <= x <= 50, edades))

numeritos=[10,12,15,22,25]
multiplos=list(filter(lambda x: x%5==0, numeritos))

# Filtrar palabras largas (mas de 5 letras)
palabras = ['Perseo', 'Talos', 'Zeus', 'Andrómeda', 'Apropósito']

palabras_largas = list(filter(lambda w: len(w) > 5, palabras))

print(palabras_largas)

# Encontrar palabras que empiecen con una letra específica (A)
palabras_A = list(filter(lambda w: w[0] == 'A', palabras))

print(palabras_A)

# Filtrar palabras que contengan una subcadena (ej. pro)
palabras_pro = list(filter(lambda w: 'pro' in w, palabras))

print(palabras_pro)

# identif palindromos (ana, anita lava la tina, oso)
palabras_tontas = ['ana', 'Júpiter', 'anita lava la tina', 'oso', 'Marte']

palindromos = list(filter(lambda w: w == w[::-1], palabras_tontas))

# Conservar solo las palabras que esten completamente en mayúsculas

datos = [1, 0, 'Hola', '', None, False, 5]
limpios = list(filter(None, datos))
print(limpios)

elimina_nones = list(filter(lambda x: x is not None, datos))
print(elimina_nones)

mezcla = [1, 'dos',3.5,4,'cinco']
enteros= list(filter(lambda x: isinstance(x, int), mezcla))

usuarios = [{'nombre': 'luis', 'edad':16}, {'nombre': 'Ana', 'edad':22}]
mayores = list(filter(lambda x: x['edad'] >= 18, usuarios))

cuentas = [{'user': 'admin', 'activo':True}, {'user': 'invitado', 'activo':False}]
activos = list(filter(lambda x: x['activo'], cuentas))

productos = [('mouse', 25), ('monitor', 150), ('teclado', 45)]
baratos = list(filter(lambda x: x[1] < 50, productos))

inv = [{'item': 'A', 'stock':1}, {'item': 'B', 'stock':10}]
dispo = list(filter(lambda x: x['stock'] > 0, inv))

lis1 = [1,2,3,4,5,6]
lis2 = [4,5,6,7,8,9]
comunes = list(filter(lambda x: x in lis2, lis1))

text='murcielago'
sin_vocales= "".join(filter(lambda w: w.lower() not in 'aeiou', text))

logs = [
    {'ip':'192.168.1.10', 'endpoint':'/home', 'status':200, 'user_agent':'Chrome'},
    {'ip':'44.33.22.11', 'endpoint':'/wp-admin.php', 'status':403, 'user_agent':'Python-urllib'},
    {'ip':'10.0.0.5', 'endpoint':'/api/v1/users', 'status':200, 'user_agent':'Safari'},
    {'ip':'88.15.44.3', 'endpoint':'/.env', 'status':404, 'user_agent':'Curl/7.68.0'},
    {'ip':'192.168.1.12', 'endpoint':'/dashboard', 'status':200, 'user_agent':'Firefox'}
]

def es_amenaza(log: dict) -> bool:
    endpoints_peligrosos = ['.env','wp_admin','config.php']

    if any(peligro in log['endpoint'] for peligro in endpoints_peligrosos):
        return True
    
    if log['status'] == 403 and log['user_agent'] not in ['Chrome','Firefox','Safari']:
        return True
    
    return True

ataques_detectados = list(filter(es_amenaza, logs))
print(ataques_detectados)