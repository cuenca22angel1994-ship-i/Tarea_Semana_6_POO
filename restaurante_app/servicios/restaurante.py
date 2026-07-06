from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio que gestiona productos y clientes del restaurante"""
    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.lista_productos: List[Producto] = []
        self.lista_clientes: List[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def mostrar_productos(self) -> None:
        print("\n--- Menú de Productos ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        # Polimorfismo: mismo método __str__, comportamiento distinto
        for prod in self.lista_productos:
            print(prod)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_clientes(self) -> None:
        print("\n--- Lista de Clientes ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        for cli in self.lista_clientes:
            print(cli)