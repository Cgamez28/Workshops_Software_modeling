"""
This module has simple CLI for Catalog Arcade Machine manipulation.

This file is part of CatalogArcadeMachine.

CatalogArcadeMachine is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

CatalogArcadeMachine is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Foobar. If not, see <https://www.gnu.org/licenses/>. 
"""
from datetime import datetime
from arcade_machine_shop import Game, ArcadeMachine, Customer, Admin, GamesCatalog, PurchaseManager

message = """
Welcome to Catalog Arcade Machines! 
1. Buy an arcade machine
2. Login as administrator
3. Exit
"""

def choose_games():
    """
    Prompts the user to choose games for the arcade machine.
    Returns:
        list: A list of Game objects representing the chosen games.
    """
    ...
    print("\nPlease, choose the games for the arcade machine:")
    games_catalog.show_games()
    
    print("Number of games: ")
    
    try:
        num_games = int(input())
    except ValueError:
        print("The number of games must be an integer.\n")
        return choose_games()
    
    if num_games < 1 or num_games > len(games_catalog.games):
        print("The number of games must be greater than 0.\n")
        return choose_games()
    
    
    for i in range(num_games):  
        
        print("Please, choose the game for the arcade machine (Enter the name of the game): ")  
        game_name = input()
        games = [] 

        for j in range(len(games_catalog.games)):
            if game_name.lower() == games_catalog.games[j].name.lower():
                category = games_catalog.games[j].category
                price = games_catalog.games[j].price
                game = Game(game_name, category, price)
                games.append(game) 


        if not games:
            print("The game is not available.")
            return choose_games()
    return games
            

def calculate_price(material: str, games: list[Game]) -> int:
    """
    Calculate the total price of a product based on the material and the list of games.

    Args:
        material (str): The material of the product. Valid options are "wood", "aluminium", or "carbon fiber".
        games (list[Game]): A list of Game objects representing the games included in the product.

    Returns:
        int: The total price of the product.
    """
    total_price = 0
    if material == "wood":
        total_price += 500
    elif material == "aluminium":
        total_price += 1000
    else: 
        material == "carbon fiber"
        total_price += 2000  
    for game in games:
        total_price += game.price
    return total_price
        

games_catalog = GamesCatalog()
option =int(input(message))

while option != 3:
    if option == 1:
        print("Please, enter the following information to buy an arcade machine:")
        print("""
            Choose the material of the arcade machine:
            1. Wood
            2. Aluminium
            3. Carbon fiber
              """)
        material = ""
        material_option = int(input("Material: "))

        while material_option not in [1, 2, 3]:
            print("Invalid option.")
            material_option = int(input("Material: "))
            
        if material_option == 1:
            material = "wood"
        elif material_option == 2:
            material = "aluminium"
        elif material_option == 3:
            material = "carbon fiber"

        print(f"The material of the arcade machine is {material}.")
        games = choose_games()
                
        price = calculate_price(material, games)
        arcade_machine = ArcadeMachine(material, games, price)
        
        print("\nNow, please enter the following personal information to buy the arcade machine:")
        name = input("Name: ")
        address = input("Address: ")
        phone = input("Phone: ")
        email = input("Email: ")
        customer = Customer(name, address, phone, email)
        
        print("The purchase details are as follows:")
        print(f"Name: {customer.name}")
        print(f"Address: {customer.adress}")
        print(f"Phone: {customer.phone}")
        print(f"Email: {customer.email}")
        print(f"Arcade machine material: {arcade_machine.material}")
        print("Games:")
        for game in arcade_machine.games:
            print(f" - Name: {game.name}, Category: {game.category}, Price: {game.price}")
        print(f"Total price: {arcade_machine.price}")
        
        print("Do you want to finalize the purchase?")
        finalize_purchase = int(input("Yes or No(Enter 1 for yes or 2 for no): "))
        if finalize_purchase == 1:
            print("Thank you for buying an arcade machine!")
            purchase_manager = PurchaseManager(customer, arcade_machine)
            purchase_manager.finalize_purchase()
        else:
            print("The purchase has been cancelled.")
            break
        
    elif option == 2:
        
        print("Please, enter the following information to login as administrator:")
        
        while True:
            username = input("Username: ")
            password = input("Password: ")
            admin = Admin("admin", "admin")
            if admin.login(username, password):
                print("The administrator has logged in successfully!")
                
                print("Please, enter the following information to add a game:")
                name = input("Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                game = Game(name, category, price)
                games_catalog.games.append(game)
                
                print("The game has been added successfully!")
                
                break
            else:
                print("The username or password is incorrect.")
    else:
        print("Invalid option.")
    option = int(input(message))
    

