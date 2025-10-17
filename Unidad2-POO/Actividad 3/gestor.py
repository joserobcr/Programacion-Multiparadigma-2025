# Fichero: gestor.py
import json
from tarea import Tarea, TareaPrioritaria

class GestorTareas:
    """
    Gestiona la lista de tareas, incluyendo la carga y guardado en JSON.
    """
    def __init__(self, archivo_json='tareas.json'):
        self.archivo_json = archivo_json
        self.tareas = self.cargar_tareas()

    def agregar_tarea(self, tarea):
        """Añade una nueva tarea a la lista."""
        self.tareas.append(tarea)
        print("¡Tarea agregada con éxito!")

    def listar_tareas(self):
        """Muestra todas las tareas registradas."""
        if not self.tareas:
            print("\nNo hay tareas registradas. ¡Añade una!")
            return
        
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(self.tareas):
            # Usamos el método polimórfico mostrar_info()
            print(f"{i + 1}. {tarea.mostrar_info()}")
        print("-----------------------")

    def marcar_tarea_completada(self, indice):
        """Marca una tarea como completada según su índice en la lista."""
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_como_completada()
            print(f"Tarea {indice + 1} marcada como completada.")
        else:
            print("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista según su índice."""
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.texto}' eliminada.")
        else:
            print("Índice de tarea no válido.")

    def guardar_tareas(self):
        """Guarda la lista de tareas en un archivo JSON."""
        lista_para_guardar = []
        for tarea in self.tareas:
            datos_tarea = {
                'texto': tarea.texto,
                'descripcion': tarea.descripcion,
                'completada': tarea.completada,
                'tipo': type(tarea).__name__ # Guardamos el nombre de la clase
            }
            if isinstance(tarea, TareaPrioritaria):
                datos_tarea['prioridad'] = tarea.prioridad
            lista_para_guardar.append(datos_tarea)
            
        with open(self.archivo_json, 'w', encoding='utf-8') as f:
            json.dump(lista_para_guardar, f, indent=4, ensure_ascii=False)
        print("Tareas guardadas en el archivo.")

    def cargar_tareas(self):
        """Carga las tareas desde un archivo JSON al iniciar."""
        try:
            with open(self.archivo_json, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            tareas_cargadas = []
            for item in datos:
                if item['tipo'] == 'TareaPrioritaria':
                    tarea = TareaPrioritaria(item['texto'], item['descripcion'], item['prioridad'])
                else:
                    tarea = Tarea(item['texto'], item['descripcion'])
                
                if item['completada']:
                    tarea.marcar_como_completada()
                tareas_cargadas.append(tarea)
            
            print("Tareas cargadas desde el archivo.")
            return tareas_cargadas
        except FileNotFoundError:
            # Si el archivo no existe, empezamos con una lista vacía.
            return []
        except json.JSONDecodeError:
            print("El archivo de tareas está corrupto o vacío. Empezando de cero.")
            return []