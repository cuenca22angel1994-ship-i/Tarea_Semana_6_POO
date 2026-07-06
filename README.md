# Tarea_Semana_6_POO
Aplicación de herencia, encapsulación y polimorfismo en un proyecto Python modular.
Alumno: Angel Rafael Cuenca Tamayo

Proyecto: Restaurante App
 
Aplicación de principios de Programación Orientada a Objetos
  
*- Descripción del sistema -*
 
Este proyecto consiste en un sistema básico de gestión para un restaurante, desarrollado en Python. Permite registrar, almacenar y visualizar productos (platillos y bebidas) y clientes, organizando el código bajo el paradigma de Programación Orientada a Objetos. El objetivo es demostrar el uso correcto de herencia, encapsulación y polimorfismo, manteniendo una estructura modular clara y fácil de mantener.
 
*- Estructura del proyecto -*
 
El código se organiza por responsabilidades:
 
plaintext
  
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       → Clase base de todos los productos
│   ├── platillo.py       → Clase especializada para comidas
│   ├── bebida.py         → Clase especializada para bebidas
│   └── cliente.py        → Clase para registrar clientes
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    → Clase de gestión general
├── main.py               → Punto de ejecución del programa
└── README.md             → Documentación del proyecto 
 
*-Relación de herencia aplicada-*
 
Se establece una jerarquía lógica:
 
- Clase padre:  Producto  → Define los atributos comunes a todos los productos:  código ,  nombre ,  categoría ,  precio  y  disponibilidad .
- Clases hijas:
-  Platillo : Hereda de  Producto  y agrega su propio atributo:  tiempo_preparacion .
-  Bebida : Hereda de  Producto  y agrega su propio atributo:  volumen_ml .
  
Se usa la función  super()  en los constructores de las clases hijas para reutilizar el código de la clase padre, evitando duplicaciones.

*- Atributo encapsulado -*
 
El atributo  __precio  está definido como privado (mediante doble guion bajo  __ ), lo que impide su modificación directa desde fuera de la clase. Para acceder y actualizar su valor se utilizan métodos controlados:
 
-  obtener_precio() : Devuelve el valor actual.
-  cambiar_precio() : Modifica el valor solo si es mayor a 0, incluyendo una validación automática para evitar valores incorrectos.
 
*-Método que demuestra el polimorfismo-*
 
Se utiliza el método especial  __str__() :
 
- En la clase  Producto  muestra la información general.
- En  Platillo  se sobrescribe para agregar el tiempo de preparación.
- En  Bebida  se sobrescribe para agregar el volumen.
 
Al recorrer la lista de productos, el mismo método  print()  ejecuta una versión diferente según el tipo de objeto, mostrando información específica en cada caso.
  
* Reflexión sobre la importancia de la POO
 
Aplicar principios de POO en proyectos modulares permite:
 
- Reutilizar código: La herencia evita escribir las mismas propiedades y métodos varias veces.
- Proteger la información: La encapsulación garantiza que los datos solo se modifiquen bajo reglas establecidas.
- Flexibilidad: El polimorfismo permite ampliar el sistema sin alterar la estructura base.
- Mantenimiento: Al separar responsabilidades, el código es más legible, organizado y fácil de corregir o ampliar a futuro.
 
