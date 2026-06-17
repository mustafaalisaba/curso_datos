def calcular(x):
    y = x * 0.05
    return y

calcular_lam = lambda x: x * 0.05

print(calcular(10))
print(calcular_lam(10))

linea_recta = lambda a, b, x: a*x+b

print(linea_recta(2,2,5))

cuadrado = lambda x: x**2

cadena_str = lambda t: f"hey, {t}"

cadena2 = lambda cadena_str: cadena_str[:2]

minuscula = lambda t: t.lower()

mayor_que = lambda a,b: a if a>b else b

par = lambda x: "par" if x%2==0 else "impar"

edad = lambda x: True if x >= 18 else False

cuadrados = lambda: [x**2 for x in range(0,100)]

texto = lambda: "textoloco"

print(texto())

print(len(cuadrados()))

cuadrados2 = [x**2 for x in range(0, 100)]

print(len(cuadrados2))

diccionario_lamb = lambda a,b,c: {a:"A",b:"B",c:"C"}

print(diccionario_lamb(1,2,3))

last = lambda lis:lis[:]

print(last([0,2,3,4,5]))