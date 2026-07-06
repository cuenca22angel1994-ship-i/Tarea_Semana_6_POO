from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def main():
    mi_restaurante = Restaurante(nombre="Sazón Manaba")

    # Crear objetos: 2 Platillos + 2 Bebidas
    plato1 = Platillo(codigo="P001", nombre="Arroz Marinero", precio=5.00, tiempo_preparacion=40)
    plato2 = Platillo(codigo="P002", nombre="Camarones Apanados", precio=4.50, tiempo_preparacion=15)
    bebida1 = Bebida(codigo="B001", nombre="Jugo de Maracuyá", precio=2.00, volumen_ml=500)
    bebida2 = Bebida(codigo="B002", nombre="Jugo de Coco", precio=1.50, volumen_ml=600)

    # Ejemplo de encapsulación: modificar precio con validación
    print("--- Actualizando precio ---")
    plato1.cambiar_precio(5.50)
    print(f"Nuevo precio {plato1._nombre}: ${plato1.obtener_precio():.2f}\n")

    # Crear clientes
    cliente1 = Cliente(id_cliente="C001", nombre="Marixa López", telefono="0975654390", correo="marix@manaba.com")
    cliente2 = Cliente(id_cliente="C002", nombre="Jhon Velez", telefono="0999433428")

    # Agregar todo
    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)
    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)

    # Mostrar información
    print(f"=== Sistema de Gestión: {mi_restaurante.nombre} ===")
    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()