# EJERCICIO 1
for i in range(101):
    print(i)

# EJERCICIO 2
num = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

# EJERCICIO 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma es:", suma)

# EJERCICIO 4
suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print("La suma total es:", suma)

# EJERCICIO 5
import random
numero = random.randint(0, 9)
intentos = 0
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero:
        adivinado = True
print("¡Correcto! Lo lograste en", intentos, "intentos.")

# EJERCICIO 6
for i in range(100, -1, -2):
    print(i)

# EJERCICIO 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

# EJERCICIO 8
pares = impares = positivos = negativos = 0
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# EJERCICIO 9
suma = 0
for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num
media = suma / 100
print("La media es:", media)

# EJERCICIO 10
num = int(input("Ingrese un número: "))
invertido = int(str(num)[::-1])
print("Número invertido:", invertido)
