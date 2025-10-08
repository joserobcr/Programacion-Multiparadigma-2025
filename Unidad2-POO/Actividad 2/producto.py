class Producto:
    
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        
        self.nombre = nombre  
        self._precio = 0.0    
        self.__stock = 0      
        
        self.precio = precio
        self.stock = stock

    @property
    def stock(self) -> int:
        """Getter para el atributo privado __stock."""
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        """Setter para __stock, no permite valores negativos."""
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        self.__stock = nuevo_stock

    @property
    def precio(self) -> float:
        """Getter para el atributo protegido _precio."""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        """Setter para _precio, requiere un valor mayor a 0."""
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio <= 0:
            raise ValueError("El precio debe ser un número mayor que cero.")
        self._precio = nuevo_precio

    # --- Métodos Especiales ---
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Producto):
            return self.nombre.lower() == other.nombre.lower()
        return False