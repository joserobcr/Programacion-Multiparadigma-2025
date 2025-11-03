"""
Módulo Principal.

Punto de entrada de la aplicación. Contiene el menú de la interfaz de 
consola y la lógica principal del programa.
"""

from operaciones import Biblioteca
from modelos import Libro, Usuario

def mostrar_menu():
    """Imprime el menú de opciones en la consola."""
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar detalles de usuario")
    print("7. Salir")
    print("-" * 20)

def main():
    """Función principal que ejecuta el bucle del programa."""
    mi_biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            try:
                año = int(input("Año de publicación: "))
                libro = Libro(titulo, autor, año)
                mi_biblioteca.agregar_libro(libro)
            except ValueError:
                print("Error: El año debe ser un número.")

        elif opcion == '2':
            nombre = input("Nombre del usuario: ")
            usuario = Usuario(nombre)
            mi_biblioteca.agregar_usuario(usuario)

        elif opcion == '3':
            mi_biblioteca.mostrar_libros_disponibles()

        elif opcion == '4':
            titulo_libro = input("Título del libro a prestar: ")
            nombre_usuario = input("Nombre del usuario: ")
            mi_biblioteca.prestar_libro(titulo_libro, nombre_usuario)

        elif opcion == '5':
            titulo_libro = input("Título del libro a devolver: ")
            nombre_usuario = input("Nombre del usuario: ")
            mi_biblioteca.devolver_libro(titulo_libro, nombre_usuario)

        elif opcion == '6':
            nombre_usuario = input("Nombre del usuario a consultar: ")
            usuario = mi_biblioteca.buscar_usuario(nombre_usuario)
            if usuario:
                usuario.mostrar_detalles() 
            else:
                print(f"Usuario '{nombre_usuario}' no encontrado.")

        elif opcion == '7':
            print("Datos guardados correctamente. Saliendo del programa.")
            mi_biblioteca.guardar_datos() 
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()