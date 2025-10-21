
# 1) Factorial y lista hasta el número indicado
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


# 2) Serie de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Posición de Fibonacci: "))
serie = [fibonacci(i) for i in range(n)]
print("Serie:", serie)


# 3) Potencia recursiva
def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

print("2^5 =", potencia(2, 5))


# 4) Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

print("10 en binario =", decimal_a_binario(10))


# 5) Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print("¿'reconocer' es palíndromo?", es_palindromo("reconocer"))


# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

print("Suma de dígitos de 1234:", suma_digitos(1234))


# 7) Pirámide de bloques
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print("Bloques para nivel 4:", contar_bloques(4))


# 8) Contar dígitos
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

print("Cantidad de 2 en 12233421:", contar_digito(12233421, 2))
