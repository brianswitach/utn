import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return math.pi * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = None
    if b != 0:
        div = a / b
    return (suma, resta, mult, div)

def calcular_imc(peso, altura):
    if altura == 0:
        return None
    imc = peso / (altura * altura)
    return imc

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == '__main__':
    imprimir_hola_mundo()
    nombre = input()
    print(saludar_usuario(nombre))
    nombre = input()
    apellido = input()
    edad = input()
    residencia = input()
    informacion_personal(nombre, apellido, edad, residencia)
    radio = float(input())
    print(f"{calcular_area_circulo(radio)}")
    print(f"{calcular_perimetro_circulo(radio)}")
    segundos = float(input())
    print(f"{segundos_a_horas(segundos)}")
    numero = int(input())
    tabla_multiplicar(numero)
    a = float(input())
    b = float(input())
    s, r, m, d = operaciones_basicas(a, b)
    print(s)
    print(r)
    print(m)
    print(d)
    peso = float(input())
    altura = float(input())
    imc = calcular_imc(peso, altura)
    if imc is None:
        print(None)
    else:
        print(f"{imc:.2f}")
    c = float(input())
    print(celsius_a_fahrenheit(c))
    x = float(input())
    y = float(input())
    z = float(input())
    print(calcular_promedio(x, y, z))
