from .producto import Producto

class Bebida(Producto):
    """Clase especializada para bebidas, hereda de Producto"""
    def __init__(self, codigo: str, nombre: str, precio: float, volumen_ml: int, disponible: bool = True):
        super().__init__(codigo, nombre, categoria="Bebida", precio=precio, disponible=disponible)
        # Atributo propio
        self._volumen_ml = volumen_ml

    # Polimorfismo: sobrescribimos la representación
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Volumen: {self._volumen_ml} ml"