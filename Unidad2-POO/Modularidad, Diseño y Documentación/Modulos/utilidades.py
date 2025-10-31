"""
Módulo de Utilidades

Este módulo proporciona funciones auxiliares y de validación
para ser usadas en todo el proyecto.
"""

def validar_entero_positivo(prompt: str) -> int:
    """
    Solicita al usuario un número entero positivo y lo valida.

    Args:
        prompt (str): El mensaje que se mostrará al usuario
                      para solicitar el dato.

    Returns:
        int: El número entero positivo ingresado por el usuario.
    """
    while True:
        try:
            valor_str = input(prompt)
            valor_int = int(valor_str)
            if valor_int > 0:
                return valor_int
            else:
                print("Error: El número debe ser positivo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")