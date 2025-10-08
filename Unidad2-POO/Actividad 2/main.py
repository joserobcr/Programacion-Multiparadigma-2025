# main.py

from producto import Producto
from inventario import Inventario

if __name__ == "__main__":
    
    # --- Inicialización ---
    mi_inventario = Inventario()
    print("Inventario creado.\n")

    # --- 1. Agregar Productos ---
    laptop = Producto("Laptop", 1200.50, 10)
    mouse = Producto("Mouse", 25.00, 50)
    teclado = Producto("Teclado Mecánico", 75.99, 20)
    monitor = Producto("Monitor 4K", 350.00, 5)

    mi_inventario.agregar_producto(laptop)
    mi_inventario.agregar_producto(mouse)
    mi_inventario.agregar_producto(teclado)
    mi_inventario.agregar_producto(monitor)

    # 1.1. Agrega un producto existente (debe usar el setter de stock en Inventario)
    mouse_extra = Producto("Mouse", 25.00, 5) 
    mi_inventario.agregar_producto(mouse_extra)
    
    print("\n" + "="*50 + "\n")

    # --- 2. Modificar stock/precios usando setters ---
    print("Modificando stock y precio (a través de los setters):")
    
    # Modificar stock de Laptop (usa el setter de Producto)
    try:
        mi_inventario.buscar_producto("Laptop").stock = 8
        print(f"Stock de Laptop ajustado a {mi_inventario.buscar_producto('Laptop').stock}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Modificar precio de Monitor (usa el setter de Producto)
    try:
        mi_inventario.buscar_producto("Monitor 4K").precio = 345.99
        print(f"Precio de Monitor ajustado a ${mi_inventario.buscar_producto('Monitor 4K').precio:.2f}")
    except Exception as e:
        print(f"Error: {e}")

    # Intento de stock negativo (debe fallar y mostrar el mensaje del setter)
    print("\nIntentando asignar stock no válido:")
    try:
        mi_inventario.buscar_producto("Teclado Mecánico").stock = -5
    except ValueError as e:
        print(f"Error capturado (Validación de Stock): {e}")

    # --- 3. Muestra total valor (Uso de total_valor_inventario) ---
    valor_total = mi_inventario.total_valor_inventario()
    print("\n" + "="*50)
    print(f"Valor Total del Inventario (Método especial: total_valor_inventario): ${valor_total:.2f}")

    # --- 4. Muestra la lista y el número de productos (Uso de __str__ y __len__) ---
    print(mi_inventario) # Usa __str__
    print(f"Total de tipos de productos (Método especial: len()): {len(mi_inventario)}") # Usa __len__

    # --- 5. Busca un producto ---
    nombre_buscado = "Mouse"
    producto_encontrado = mi_inventario.buscar_producto(nombre_buscado)
    if producto_encontrado:
        print(f"\nProducto buscado: {producto_encontrado}") # Usa __str__ de Producto
    else:
        print(f"\nProducto '{nombre_buscado}' no encontrado.")
        
    # --- 6. Compara dos productos iguales (Uso de __eq__) ---
    print("\n" + "="*50)
    print("Comparación de Productos (Método especial: __eq__):")
    producto_a = Producto("Auriculares", 50.0)
    producto_b = Producto("auriculares", 75.0) 
    producto_c = Producto("Impresora", 200.0)

    print(f"'{producto_a.nombre}' == '{producto_b.nombre}' (solo por nombre): {producto_a == producto_b}")
    print(f"'{producto_a.nombre}' == '{producto_c.nombre}': {producto_a == producto_c}")