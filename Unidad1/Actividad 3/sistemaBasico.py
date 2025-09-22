def agregar_tarea(tareas):
    """Permite al usuario agregar una nueva tarea a la lista."""
    tarea = input("Ingresa la nueva tarea: ")
    tareas.append({"tarea": tarea, "completada": False})
    print("Tarea agregada exitosamente.")

def listar_tareas(tareas):
    """Muestra todas las tareas pendientes y completadas."""
    if not tareas:
        print("No hay tareas en la lista.")
        return

    print("\n--- Tareas actuales ---")
    for i, t in enumerate(tareas):
        estado = "✅" if t["completada"] else "❌"
        print(f"{i + 1}. [{estado}] {t['tarea']}")
    print("---------------------\n")

def marcar_completada(tareas):
    """Permite al usuario marcar una tarea como completada."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea = int(input("Ingresa el número de la tarea a marcar como completada: "))
        if 1 <= num_tarea <= len(tareas):
            tareas[num_tarea - 1]["completada"] = True
            print(f"La tarea '{tareas[num_tarea - 1]['tarea']}' ha sido marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

def eliminar_tarea(tareas):
    """Permite al usuario eliminar una tarea de la lista."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        num_tarea = int(input("Ingresa el número de la tarea a eliminar: "))
        if 1 <= num_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(num_tarea - 1)
            print(f"La tarea '{tarea_eliminada['tarea']}' ha sido eliminada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Gestor de Tareas Personales ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del programa")
    print("-----------------------------------")

def main():
    """Función principal que ejecuta el gestor de tareas."""
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()