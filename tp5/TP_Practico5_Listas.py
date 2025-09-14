# TP 5 - Brian Switach
import random

def print_lista(titulo, lst):
    print(titulo)
    for i, v in enumerate(lst):
        print(f"  [{i}] -> {v}")

def pedir_lista_numeros(n, texto="Ingrese número"):
    nums = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"{texto} #{i+1}: ").strip())
                nums.append(x)
                break
            except ValueError:
                print("  Valor inválido. Intente de nuevo.")
    return nums

def pedir_lista_enteros(n, texto="Ingrese entero"):
    nums = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"{texto} #{i+1}: ").strip())
                nums.append(x)
                break
            except ValueError:
                print("  Valor inválido. Intente de nuevo.")
    return nums

def pedir_lista_textos(n, texto="Ingrese texto"):
    items = []
    for i in range(n):
        s = ""
        while s == "":
            s = input(f"{texto} #{i+1}: ").strip()
            if s == "":
                print("  No puede estar vacío.")
        items.append(s)
    return items

# =======================
# Ejercicio 1
# =======================
print("Ejercicio 1:")
notas = pedir_lista_numeros(10, "Ingrese nota del estudiante")
print_lista("  Lista completa de notas:", notas)
prom = sum(notas)/len(notas)
print(f"  Promedio: {prom:.2f}")
nota_max = max(notas)
nota_min = min(notas)
print(f"  Nota más alta: {nota_max}")
print(f"  Nota más baja: {nota_min}")
print("-"*50)

# =======================
# Ejercicio 2
# =======================
print("Ejercicio 2:")
productos = pedir_lista_textos(5, "Ingrese producto")
print("  Lista ordenada alfabéticamente (usando sorted()):")
ordenada = sorted(productos, key=lambda s: s.lower())
for i, p in enumerate(ordenada):
    print(f"  [{i}] -> {p}")
a_eliminar = input("  ¿Qué producto desea eliminar? Escriba el nombre exacto: ").strip()
if a_eliminar in productos:
    productos.remove(a_eliminar)
    print("  Producto eliminado. Lista actualizada:")
else:
    print("  No se encontró el producto. Lista sin cambios:")
for i, p in enumerate(productos):
    print(f"  [{i}] -> {p}")
print("-"*50)

# =======================
# Ejercicio 3
# =======================
print("Ejercicio 3:")
nums = [random.randint(1, 100) for _ in range(15)]
print_lista("  Lista de 15 enteros al azar (1..100):", nums)
pares = []
impares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print_lista("  Pares:", pares)
print_lista("  Impares:", impares)
print(f"  Cantidad en lista de pares: {len(pares)}")
print(f"  Cantidad en lista de impares: {len(impares)}")
print("-"*50)

# =======================
# Ejercicio 4
# =======================
print("Ejercicio 4:")
print("  Ingrese una lista con valores (separados por espacios). Ej: 1 2 2 3 4 4 5")
entrada = input("  -> ").strip()
valores = entrada.split() if entrada else []
print_lista("  Lista original:", valores)
sin_repetidos = []
vistos = set()
for v in valores:
    if v not in vistos:
        sin_repetidos.append(v)
        vistos.add(v)
print_lista("  Nueva lista sin repetidos:", sin_repetidos)
print("-"*50)

# =======================
# Ejercicio 5
# =======================
print("Ejercicio 5:")
alumnos = pedir_lista_textos(8, "Ingrese nombre de estudiante presente")
accion = ""
while accion.lower() not in ("agregar", "eliminar", "ninguna"):
    accion = input("  ¿Desea 'agregar', 'eliminar' o 'ninguna'?: ").strip().lower()
if accion == "agregar":
    nuevo = input("  Nombre a agregar: ").strip()
    if nuevo:
        alumnos.append(nuevo)
        print("  Agregado.")
elif accion == "eliminar":
    borrar = input("  Nombre a eliminar: ").strip()
    if borrar in alumnos:
        alumnos.remove(borrar)
        print("  Eliminado.")
    else:
        print("  No se encontró el nombre.")
print_lista("  Lista final actualizada:", alumnos)
print("-"*50)

# =======================
# Ejercicio 6
# =======================
print("Ejercicio 6:")
lista7 = pedir_lista_enteros(7, "Ingrese número de la lista (7 en total)")
print_lista("  Lista original:", lista7)
# rotar a derecha: último pasa a ser primero
if len(lista7) > 0:
    rotada = [lista7[-1]] + lista7[:-1]
else:
    rotada = []
print_lista("  Lista rotada a la derecha (1 posición):", rotada)
print("-"*50)

# =======================
# Ejercicio 7
# =======================
print("Ejercicio 7:")
print("  Ingrese mínimas y máximas de 7 días (semana).")
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
temps = []  # 7x2: [ [min, max], ... ]
for i in range(7):
    while True:
        try:
            tmin = float(input(f"    {dias[i]} - Mínima: ").strip())
            tmax = float(input(f"    {dias[i]} - Máxima: ").strip())
            if tmax < tmin:
                print("    Máxima no puede ser menor que mínima. Reingresar.")
                continue
            temps.append([tmin, tmax])
            break
        except ValueError:
            print("    Valor inválido. Intente de nuevo.")
# promedio mínimas y máximas
suma_min = 0.0
suma_max = 0.0
for par in temps:
    suma_min += par[0]
    suma_max += par[1]
prom_min = suma_min / 7
prom_max = suma_max / 7
print(f"  Promedio de mínimas: {prom_min:.2f}")
print(f"  Promedio de máximas: {prom_max:.2f}")
# mayor amplitud
mayor_amp = None
dia_mayor_amp = None
for i in range(7):
    amp = temps[i][1] - temps[i][0]
    if (mayor_amp is None) or (amp > mayor_amp):
        mayor_amp = amp
        dia_mayor_amp = i
print(f"  Mayor amplitud térmica: {mayor_amp:.2f} en {dias[dia_mayor_amp]}")
print("-"*50)

# =======================
# Ejercicio 8
# =======================
print("Ejercicio 8:")
print("  Ingrese las notas de 5 estudiantes en 3 materias (valores numéricos).")
notas = []  # 5x3
for i in range(5):
    fila = []
    for j in range(3):
        while True:
            try:
                x = float(input(f"    Estudiante {i+1}, Materia {j+1}: ").strip())
                fila.append(x)
                break
            except ValueError:
                print("    Valor inválido. Intente de nuevo.")
    notas.append(fila)
# Promedio de cada estudiante
for i in range(5):
    s = 0.0
    for j in range(3):
        s += notas[i][j]
    print(f"  Promedio Estudiante {i+1}: {s/3:.2f}")
# Promedio de cada materia
for j in range(3):
    s = 0.0
    for i in range(5):
        s += notas[i][j]
    print(f"  Promedio Materia {j+1}: {s/5:.2f}")
print("-"*50)

# =======================
# Ejercicio 9
# =======================
print("Ejercicio 9:")
print("  Tablero Ta-Te-Ti 3x3. Casillas vacías con '-'.")
tab = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        # imprimir fila con bucle
        linea = ""
        for c in fila:
            linea += c + " "
        print("  " + linea.strip())

def posicion_valida(r, c):
    return 0 <= r < 3 and 0 <= c < 3 and tab[r][c] == "-"

turno = "X"  # alterna entre X y O
for jugada in range(9):
    print(f"  Turno de {turno}. Ingrese fila y columna (0..2).")
    while True:
        try:
            r = int(input("    Fila (0,1,2): ").strip())
            c = int(input("    Columna (0,1,2): ").strip())
            if posicion_valida(r, c):
                tab[r][c] = turno
                break
            else:
                print("    Posición inválida u ocupada. Reintente.")
        except ValueError:
            print("    Entrada inválida. Reintente.")
    print("  Tablero luego de la jugada:")
    mostrar_tablero(tab)
    # alternar
    turno = "O" if turno == "X" else "X"
print("-"*50)

# =======================
# Ejercicio 10
# =======================
print("Ejercicio 10:")
print("  Matriz de ventas de 4 productos durante 7 días (4x7).")
ventas = []  # 4x7
for p in range(4):
    fila = []
    for d in range(7):
        while True:
            try:
                x = float(input(f"    Producto {p+1}, Día {d+1}: ").strip())
                fila.append(x)
                break
            except ValueError:
                print("    Valor inválido. Intente de nuevo.")
    ventas.append(fila)

# Total por producto
totales_producto = []
for p in range(4):
    s = 0.0
    for d in range(7):
        s += ventas[p][d]
    totales_producto.append(s)

for p, total in enumerate(totales_producto, start=1):
    print(f"  Total vendido por Producto {p}: {total:.2f}")

# Día con mayores ventas totales
totales_dia = []
for d in range(7):
    s = 0.0
    for p in range(4):
        s += ventas[p][d]
    totales_dia.append(s)

dia_max = max(range(7), key=lambda i: totales_dia[i])
print(f"  Día con mayores ventas totales: Día {dia_max+1} (Total {totales_dia[dia_max]:.2f})")

# Producto más vendido en la semana
prod_max = max(range(4), key=lambda i: totales_producto[i])
print(f"  Producto más vendido en la semana: Producto {prod_max+1} (Total {totales_producto[prod_max]:.2f})")


