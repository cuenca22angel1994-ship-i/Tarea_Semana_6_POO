from .producto import Producto

class Platillo(Producto):
    """Clase especializada para platillos, hereda de Producto"""
    def __init__(self, codigo: str, nombre: str, precio: float, tiempo_preparacion: int, disponible: bool = True):
        # Reutilizamos constructor de la clase padre
        super().__init__(codigo, nombre, categoria="Plato Principal", precio=precio, disponible=disponible)
        # Atributo propio
        self._tiempo_preparacion = tiempo_preparacion

    # Polimorfismo: sobrescribimos la representación
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Tiempo de preparación: {self._tiempo_preparacion} min"