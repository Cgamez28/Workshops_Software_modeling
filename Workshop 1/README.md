# Workshop: Arcade Machine Shop

## Description

This workshop involves creating a console program to manage the purchase of custom arcade machines. Customers can choose the material of the machine, add available games in the catalog to their purchase, and finalize the transaction by providing their information for delivery. Additionally, the program includes the functionality for an administrator to add new games to the catalog, keeping it updated with the latest available options.

## Main Functionalities

1. **Material Selection:** Allows the customer to choose the type of material for the arcade machine from options such as wood, aluminum, and carbon fiber.
2. **Game Catalog:** Displays the list of available games that can be added to the arcade machine.
3. **Add Games:** Customers can add games to their arcade machine using a unique code for each game.
4. **Finalize Purchase:** Customers complete the purchase of their arcade machine and provide the necessary information for delivery.
6. **Administrator Catalog Management:** Allows the administrator to add new games to the catalog to keep it up to date.

## User Stories

- **Customer:**
- Choose the type of hardware for the arcade machine.
- View the list of available games and add them to the machine using a code.
- Complete the purchase and provide delivery information.
- Search for games in the catalog by category.
- **Administrator:**
- Add new games to the catalog to keep it up to date.

## Object Oriented Design

The program follows the principles of Object Oriented Programming (OOP) to achieve a modular and scalable architecture. SOLID principles have been applied to ensure the maintainability and extensibility of the system.

### Main Classes

- **ArcadeMachine:** Manages the configuration of the arcade machine, allowing you to choose hardware and add games.
- **Game:** Represents an individual game, with details such as name, category, and unique code.
- **GameCatalog:** Manages the list of available games, allowing you to search by code or category.
- **Customer:** Stores and manages customer information.
- **PurchaseManager:** Controls the purchasing process, including completion and summary of the transaction.
- **Administrator:** Allows you to add new games to the catalog.
