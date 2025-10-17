# Fichero: main.py
from gestor import GestorTareas
from tarea import Tarea, TareaPrioritaria

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Agregar nueva tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("------------------------------------")

def main():
    """Función principal que ejecuta el programa."""
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            texto = input("Introduce el título de la tarea: ")
            descripcion = input("Introduce la descripción: ")
            es_prioritaria = input("¿Es una tarea prioritaria? (s/n): ").lower()
            
            if es_prioritaria == 's':
                prioridad = input("Introduce el nivel de prioridad (Ej: Alta, Media, Baja): ")
                nueva_tarea = TareaPrioritaria(texto, descripcion, prioridad)
            else:
                nueva_tarea = Tarea(texto, descripcion)
            
            gestor.agregar_tarea(nueva_tarea)

        elif opcion == '2':
            gestor.listar_tareas()

        elif opcion == '3':
            gestor.listar_tareas()
            try:
                indice = int(input("Introduce el número de la tarea a completar: ")) - 1
                gestor.marcar_tarea_completada(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")

        elif opcion == '4':
            gestor.listar_tareas()
            try:
                indice = int(input("Introduce el número de la tarea a eliminar: ")) - 1
                gestor.eliminar_tarea(indice)
            except ValueError:
                print("Por favor, introduce un número válido.")

        elif opcion == '5':
            gestor.guardar_tareas()
            print("¡Saliendo del sistema!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()