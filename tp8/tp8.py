def leer_productos():
    productos = []
    try:
        with open("productos.txt", "r") as f:
            for linea in f:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
    return productos

def mostrar_productos(productos):
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")
    with open("productos.txt", "a") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")

def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print(f"Encontrado → {p}")
            return
    print("Producto no encontrado.")

def guardar_productos(productos):
    with open("productos.txt", "w") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

def main():
    productos = leer_productos()
    mostrar_productos(productos)
    agregar_producto()
    productos = leer_productos()
    buscar_producto(productos)
    guardar_productos(productos)

if __name__ == "__main__":
    main()
