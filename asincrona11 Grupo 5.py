#Bienvenida
print("bienvenido al programa")

#Variables n 
numeros = []
n = int(input("Ingrese la cantidad de números a evaluar: "))

#Numeros positivos,negativos y nulos y uso while 
while len(numeros) < n:
    try:
        num = int(input("Ingrese un número: "))
        numeros.append(num)
    except ValueError:
        print("El valor ingresado no es un número. Intente de nuevo.")

positivos = 0
negativos = 0
nulos = 0

for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        nulos += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números nulos:", nulos)

#Final del programa 
print("Fin")
