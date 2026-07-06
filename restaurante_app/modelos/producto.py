class Producto:
    """Clase base que representa cualquier producto del restaurante"""
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Atributos encapsulados (protegidos/privados)
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self.__precio = self._validar_precio(precio)  # Privado
        self._disponible = disponible

    # Método para validar precio
    def _validar_precio(self, valor: float) -> float:
        if valor > 0:
            return round(valor, 2)
        print("⚠️ Precio inválido, se asigna $1.00 por defecto")
        return 1.00

    # Métodos de acceso y modificación
    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        self.__precio = self._validar_precio(nuevo_precio)

    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._codigo}] {self._nombre} | Categoría: {self._categoria} | Precio: ${self.__precio:.2f} | Estado: {estado}"