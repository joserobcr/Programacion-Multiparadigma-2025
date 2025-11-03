"""
Módulo de Operaciones.

Define la clase Biblioteca, que maneja toda la lógica de gestión,
incluyendo la persistencia de datos en JSON.
"""

import json
from typing import List, Optional
from modelos import Libro, Usuario

class Biblioteca:
    """
    Clase que gestiona las operaciones de la biblioteca.
    Administra listas de libros y usuarios, y maneja la persistencia de datos.
    """

    def __init__(self, archivo_datos: str = "biblioteca.json"):
        """
        Inicializa la Biblioteca.

        Args:
            archivo_datos (str): Nombre del archivo JSON para guardar/cargar datos.
        """
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []
        self.archivo_datos = archivo_datos
        self.cargar_datos()

    def agregar_libro(self, libro: Libro):
        """Agrega un nuevo libro al catálogo de la biblioteca."""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado con éxito.")
        self.guardar_datos()

    def agregar_usuario(self, usuario: Usuario):
        """Registra un nuevo usuario en el sistema."""
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' agregado con éxito.")
        self.guardar_datos()

    def buscar_libro(self, titulo: str) -> Optional[Libro]:
        """Busca un libro por título."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, nombre: str) -> Optional[Usuario]:
        """Busca un usuario por nombre."""
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    def mostrar_libros_disponibles(self):
        """Muestra todos los libros con estado 'disponible'."""
        disponibles = [libro for libro in self.libros if libro.estado == "disponible"]
        if not disponibles:
            print("No hay libros disponibles en este momento.")
            return

        print("\n--- Libros Disponibles ---")
        for libro in disponibles:
            libro.mostrar_detalles()
        print("-" * 26)

    def prestar_libro(self, titulo_libro: str, nombre_usuario: str):
        """Presta un libro a un usuario, cambiando su estado."""
        libro = self.buscar_libro(titulo_libro)
        usuario = self.buscar_usuario(nombre_usuario)

        if not libro:
            print(f"Error: No se encontró el libro '{titulo_libro}'.")
            return
        if not usuario:
            print(f"Error: No se encontró el usuario '{nombre_usuario}'.")
            return
        
        if libro.estado == "disponible":
            libro.estado = "prestado"
            usuario.libros_prestados.append(libro.titulo)
            self.guardar_datos()
            print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
        else:
            print(f"Error: El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, titulo_libro: str, nombre_usuario: str):
        """Devuelve un libro a la biblioteca, cambiando su estado."""
        libro = self.buscar_libro(titulo_libro)
        usuario = self.buscar_usuario(nombre_usuario)

        if not libro:
            print(f"Error: No se encontró el libro '{titulo_libro}'.")
            return
        if not usuario:
            print(f"Error: No se encontró el usuario '{nombre_usuario}'.")
            return

        if libro.estado == "prestado" and libro.titulo in usuario.libros_prestados:
            libro.estado = "disponible"
            usuario.libros_prestados.remove(libro.titulo)
            self.guardar_datos()
            print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
        else:
            print(f"Error: El libro '{libro.titulo}' no estaba prestado a {usuario.nombre}.")

    def guardar_datos(self):
        """Guarda el estado actual de libros y usuarios en un archivo JSON."""
        try:
            datos = {
                "libros": [libro.__dict__ for libro in self.libros],
                "usuarios": [usuario.__dict__ for usuario in self.usuarios]
            }
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self):
        """Carga el estado de libros y usuarios desde un archivo JSON."""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                
                self.libros = []
                for l_data in datos.get("libros", []):
                    libro = Libro(l_data['titulo'], l_data['autor'], l_data['año'])
                    libro.estado = l_data.get('estado', 'disponible')
                    self.libros.append(libro)
                
                self.usuarios = []
                for u_data in datos.get("usuarios", []):
                    usuario = Usuario(u_data['nombre'])
                    usuario.libros_prestados = u_data.get('libros_prestados', []) 
                    self.usuarios.append(usuario)
                    
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo de datos no encontrado. Se iniciará con una biblioteca vacía.")
        except Exception as e:
            print(f"Error al cargar datos: {e}. Se iniciará con biblioteca vacía.")
            self.libros = []
            self.usuarios = []