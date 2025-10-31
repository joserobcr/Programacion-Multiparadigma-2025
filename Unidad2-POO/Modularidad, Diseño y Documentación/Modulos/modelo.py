"""
Módulo de Modelo 

Contiene las clases principales y la lógica de negocio
del sistema de inventario.
"""

class Producto:
    """
    Representa un producto en el inventario.

    Attributes:
        nombre (str): El nombre del producto.
        precio (float): El precio unitario del producto.
        cantidad (int): La cantidad en stock del producto.
    """

    def __init__(self, nombre: str, precio: float, cantidad: int):
        """
        Inicializa una nueva instancia de Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto (debe ser > 0).
            cantidad (int): La cantidad en stock (debe ser >= 0).
        """
        if precio <= 0:
            raise ValueError("El precio debe ser positivo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
            
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del producto.

        Returns:
            str: Descripción textual del producto.
        """
        return f"Producto: {self.nombre} | Precio: ${self.precio:,.2f} | Stock: {self.cantidad}"

    def calcular_valor_total(self) -> float:
        """
        Calcula el valor total del stock de este producto.

        Returns:
            float: El valor total (precio * cantidad).
        """
        return self.precio * self.cantidad