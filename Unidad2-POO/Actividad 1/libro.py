# Jose Roberto Carrizales
# 21100177
class Libro:
    """
    Clase que modela un libro en una biblioteca.
    """

    # Atributos de clase
    biblioteca = "Biblioteca Central"

    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        """
        Constructor de la clase Libro.

        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param año_publicacion: Año de publicación del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.prestado = False

    def prestar(self):
            """
            Método para prestar el libro.
            """
            if not self.prestado:
                self.prestado = True
                print(f"El libro '{self.titulo}' ha sido prestado.")
            else:
                print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
            """
            Método para devolver el libro a la biblioteca.
            """
            if self.prestado:
                self.prestado = False
                print(f"El libro '{self.titulo}' ha sido devuelto y esta disponible.")
            else:
                print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_estado(self):
            """
            Método para mostrar el estado del libro.
            """
            estado = "prestado" if self.prestado else "Disponible"
            print("-" * 30)
            print(f" INFORMACIÓN DEL LIBRO ")
            print(f" Título: {self.titulo}")
            print(f" Autor: {self.autor}")
            print(f" Año de Publicación: {self.año_publicacion}")
            print(f" Estado: {estado}")
            print(f" Ubicacion: {Libro.biblioteca}")
            print("-" * 30)