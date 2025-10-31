"""
Módulo Principal (main.py)

Punto de entrada del programa. Controla el menú principal
y coordina las operaciones del sistema de inventario,
utilizando 'modelo' para los datos y 'utilidades' para la validación.
"""

# Importamos las clases y funciones de nuestros propios módulos
# Nota cómo usamos 'modulos.' como prefijo del paquete
from Modulos.modelo import Producto
from Modulos.utilidades import validar_entero_positivo

# Esta lista simula nuestra base de datos en memoria
inventario = []


def agregar_producto():
    """
    Solicita al usuario los datos de un nuevo producto
    y lo añade al inventario.
    """
    print("\n--- Agregar Nuevo Producto ---")
    try:
        # Usamos la función del módulo de utilidades
        nombre = input("Nombre del producto: ")
        precio = validar_entero_positivo("Precio del producto: ")
        cantidad = validar_entero_positivo("Cantidad en stock: ")
        
        # Creamos la instancia de la clase del módulo modelo
        nuevo_producto = Producto(nombre, float(precio), cantidad)
        inventario.append(nuevo_producto)
        print(f"\n¡Producto '{nombre}' agregado con éxito!")

    except ValueError as e:
        print(f"Error al crear producto: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def ver_inventario():
    """
    Muestra todos los productos actualmente en el inventario.
    """
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    valor_total_inventario = 0.0
    for producto in inventario:
        # Usa el método __str__ de la clase Producto
        print(f"- {producto}")
        valor_total_inventario += producto.calcular_valor_total()
    
    print("---------------------------------")
    print(f"Valor total del inventario: ${valor_total_inventario:,.2f}")


def main_menu():
    """
    Muestra el menú principal y gestiona la selección del usuario.
    """
    while True:
        print("\n===== GESTOR DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_inventario()
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Esta construcción estándar de Python asegura que main_menu()
# solo se ejecute cuando el script es el archivo principal.
if __name__ == "__main__":
    main_menu()