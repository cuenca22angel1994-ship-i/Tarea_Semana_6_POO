class Cliente:
    """Clase que representa a un cliente registrado en el sistema"""

    def __init__(self, id_cliente: str, nombre: str, telefono: str, correo: str = ""):
        self.id_cliente: str = id_cliente
        self.nombre: str = nombre
        self.telefono: str = telefono
        self.correo: str = correo
        self.activo: bool = True  # Indica si el cliente sigue activo

    def __str__(self) -> str:
        """Representación en texto del cliente"""
        estado = "Activo" if self.activo else "Inactivo"
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Correo: {self.correo} | Estado: {estado}"