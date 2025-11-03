"""
Módulo de Modelos.

Define las clases de entidad para el sistema de gestión de la biblioteca,
incluyendo Persona, Usuario y Libro.
"""

class Persona:
    """Clase base que representa a una persona."""
    
    def __init__(self, nombre: str):
        """
        Inicializa una nueva Persona.

        Args:
            nombre (str): El nombre de la persona.
        """
        self.nombre = nombre

    def mostrar_detalles(self):
        """Muestra los detalles básicos de la persona."""
        print(f"Nombre: {self.nombre}")


class Usuario(Persona):
    """
    Clase que representa a un usuario de la biblioteca.
    Hereda de Persona.
    """
    
    def __init__(self, nombre: str):
        """
        Inicializa un nuevo Usuario.

        Args:
            nombre (str): El nombre del usuario.
        """
        super().__init__(nombre)  
        self.libros_prestados = [] 

    def mostrar_detalles(self):
        """
        Muestra los detalles del usuario, incluyendo los libros prestados.
        En este punto, el método es sobreescrito, aplicando polimorfismo.
        """
        print(f"--- Usuario: {self.nombre} ---")
        if self.libros_prestados:
            print("Libros Prestados:")
            for libro in self.libros_prestados:
                print(f"  - {libro}")
        else:
            print("No tiene libros prestados.")
        print("-" * (17 + len(self.nombre)))


class Libro:
    """Clase que representa un libro en la biblioteca."""
    
    def __init__(self, titulo: str, autor: str, año: int):
        """
        Inicializa un nuevo Libro.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            año (int): El año de publicación.
        """
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.estado = "disponible"  

    def mostrar_detalles(self):
        """Muestra los detalles completos del libro."""
        print(f"'{self.titulo}' por {self.autor} ({self.año}) - Estado: {self.estado}")

    def __str__(self):
        """Representación en string simple del libro."""
        return f"'{self.titulo}' ({self.autor})"