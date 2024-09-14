# Taller: Tienda de Máquinas Arcade

## Descripción

Este taller consiste en la creación de un programa en consola para gestionar la compra de máquinas arcade personalizadas. Los clientes pueden elegir el material de la máquina, agregar juegos disponibles en el catálogo a su compra y finalizar la transacción proporcionando su información para la entrega. Además, el programa incluye la funcionalidad para que un administrador pueda añadir nuevos juegos al catálogo, manteniéndolo actualizado con las últimas opciones disponibles.

## Funcionalidades Principales

1. **Selección de Materiales:** Permite al cliente elegir el tipo de material de la máquina arcade entre opciones como madera, aluminio y fibra de carbono.
2. **Catálogo de Juegos:** Muestra la lista de juegos disponibles que pueden ser añadidos a la máquina arcade.
3. **Añadir Juegos:** Los clientes pueden añadir juegos a su máquina arcade usando un código único para cada juego.
4. **Finalizar Compra:** Los clientes completan la compra de su máquina arcade y proporcionan la información necesaria para la entrega.
6. **Gestión del Catálogo por el Administrador:** Permite al administrador añadir nuevos juegos al catálogo para mantenerlo actualizado.

## Historias de Usuario

- **Cliente:** 
  - Elegir el tipo de material para la máquina arcade.
  - Ver la lista de juegos disponibles y añadirlos a la máquina utilizando un código.
  - Completar la compra y proporcionar la información de entrega.
  - Buscar juegos en el catálogo por categorías.
- **Administrador:**
  - Añadir nuevos juegos al catálogo para mantenerlo actualizado.

## Diseño Orientado a Objetos

El programa sigue los principios de la Programación Orientada a Objetos (POO) para lograr una arquitectura modular y escalable. Se han aplicado los principios SOLID para asegurar la mantenibilidad y extensibilidad del sistema. 

### Clases Principales

- **ArcadeMachine:** Gestiona la configuración de la máquina arcade, permitiendo elegir materiales y agregar juegos.
- **Game:** Representa un juego individual, con detalles como el nombre, categoría, y código único.
- **GameCatalog:** Gestiona la lista de juegos disponibles, permitiendo buscar por código o categoría.
- **Customer:** Almacena y gestiona la información del cliente.
- **PurchaseManager:** Controla el proceso de compra, incluyendo la finalización y resumen de la transacción.
- **Administrator:** Permite añadir nuevos juegos al catálogo.