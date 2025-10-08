from producto import Producto

class Inventario:

    def __init__(self):
        # Atributo privado: {nombre_minusculas: objeto_Producto}
        self.__productos: dict[str, Producto] = {}

    def agregar_producto(self, producto: Producto):
        """
        Agrega un producto o actualiza su stock si ya existe.
        
        Usa el setter de stock del objeto Producto.
        """
        nombre_clave = producto.nombre.lower()
        if nombre_clave in self.__productos:
            # Producto ya existe, actualiza su stock sumando el stock del nuevo objeto
            producto_existente = self.__productos[nombre_clave]
            nuevo_stock = producto_existente.stock + producto.stock
            producto_existente.stock = nuevo_stock  
            print(f"Stock de '{producto.nombre}' actualizado a {nuevo_stock}.")
        else:
            # Producto nuevo
            self.__productos[nombre_clave] = producto
            print(f"Producto '{producto.nombre}' agregado con éxito.")

    def buscar_producto(self, nombre: str) -> Producto or None:
        """
        Retorna el Producto o None.
        """
        return self.__productos.get(nombre.lower())

    def total_valor_inventario(self) -> float:
        """Suma el valor total de todos los productos."""
        valor_total = 0.0
        for producto in self.__productos.values():
            valor_total += producto.stock * producto.precio
        return valor_total

    def __len__(self) -> int:
        """Retorna el número de productos únicos en el inventario."""
        return len(self.__productos)

    def __str__(self) -> str:
        """Lista todos los productos en formato legible (usa __str__ de Producto)."""
        if not self.__productos:
            return "El inventario está vacío."
        
        info = ["\n--- Reporte de Inventario ---"]
        for producto in self.__productos.values():
            info.append(str(producto))
        info.append(f"\nTotal de productos únicos: {len(self)}")
        return "\n".join(info)