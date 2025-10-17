# Fichero: tarea.py

class Tarea:
    """
    Clase base que representa una tarea genérica.
    Aplica encapsulación para proteger los atributos.
    """
    def __init__(self, texto, descripcion):
        # Encapsulación: Atributos "protegidos" con un guion bajo.
        self._texto = texto
        self._descripcion = descripcion
        self._completada = False

    # Propiedades para acceder a los atributos de forma controlada (getter)
    @property
    def texto(self):
        return self._texto

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    def marcar_como_completada(self):
        """Marca la tarea como completada."""
        self._completada = True

    def mostrar_info(self):
        """
        Muestra la información de la tarea.
        Este es el método que será redefinido (Polimorfismo).
        """
        estado = "Completada" if self._completada else "Pendiente"
        return f"[{estado}] {self._texto}: {self._descripcion}"

# Herencia 
class TareaPrioritaria(Tarea):
    """
    Clase que hereda de Tarea y añade un nivel de prioridad.
    """
    def __init__(self, texto, descripcion, prioridad):
        # Llama al constructor de la clase padre (Tarea)
        super().__init__(texto, descripcion)
        self._prioridad = prioridad

    @property
    def prioridad(self):
        return self._prioridad
    
    # Polimorfismo
    def mostrar_info(self):
        """
        Redefine el método de la clase padre para mostrar también la prioridad.
        """
        # Llama al método original de la clase padre para no repetir código
        info_base = super().mostrar_info()
        return f"{info_base} - Prioridad: {self._prioridad}"