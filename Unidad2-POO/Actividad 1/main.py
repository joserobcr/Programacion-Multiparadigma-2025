# Jose Roberto Carrizales
# 21100177

# Importar la clase Libro desde el archivo libro.py
from libro import Libro

def main():
    """
    Funcion principal para instanciar y manipular objetos de la clase Libro.
    """

    print(" INICIO DE LA GESTION DE LA BIBLIOTECA ")

    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("1984", "George Orwell", 1949)  
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)

    print("\n Estado inicial de los libros: ")
    libro1.mostrar_estado()
    libro2.mostrar_estado() 
    libro3.mostrar_estado()

    print("\n MANIPULACION DE ESTADOS DE LOS LIBROS ")
    # Prestamos libro1
    libro1.prestar()

    # Intentamos prestar libro1 nuevamente
    libro1.prestar()

    # Prestamos libro3
    libro3.prestar() 

    # Devolvemos el libro2 (que no estaba prestado)
    libro2.devolver()

    # Devolvemos el libro1
    libro1.devolver()

    print("\n Estado final de los libros: ")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()

    # Muestra la ubicacion de la biblioteca
    print(f"\n Todos los libros pertenecen a la: {Libro.biblioteca}")

if __name__ == "__main__":
    main()