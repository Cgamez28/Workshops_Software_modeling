"""
This module contains the CatalogArcadeMachine class.

Author: Cristian Andres Gamez Nuñez <cagamezn@udistrital.edu.co>

This file is part of CatalogArcadeMachines.

CatalogArcadeMachines is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

CatalogArcadeMachines is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with CatalogArcadeMachines. If not, see <https://www.gnu.org/licenses/>. 
"""
from datetime import datetime

class Game:
    """
    This class represents a game for the arcade machine.
    """
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

class ArcadeMachine:
    """
    This class represents an arcade machine.
    """
    def __init__(self, material: str, games: list[Game], price: float):
        self.material = material
        self.games = games
        self.price = price
    
    def choose_material(self, material: str):
        """
        This method allows to choose the material of the arcade machine.
        
        Args: 
            material (str): The material of the arcade machine.
        """
        self.material = material
    
    def calculate_price(self):
        """
        This method allows to calculate the price of the arcade machine.
        """
        total_price = 0
        if self.material == "wood":
            total_price += 500
        elif self.material == "aluminium":
            total_price += 1000
        elif self.material == "carbon fiber":
            total_price += 2000  
        else:
            raise ValueError("The material is not available.")
        for game in self.games:
            total_price += game.price
        return total_price
        
    def add_game(self, game: Game):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            game (Game): The game to add.
        """
        self.games.append(game)
    

class Admin:
    """
    This class represents the admin of the arcade machine shop.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
    
    def login(self, username: str, password: str) -> bool:  
        """
        This method allows to login.
        
        Args:
            username (str): The username.
            password (str): The password.
        """
        if self.username == username and self.password == password:
            return True
        else:
            return False
    
    def add_game(self, game: Game):
        """
        This method allows to add a game to the catalog.
        
        Args:
            game (Game): The game to add.
        """
        GamesCatalog.games.append(game)
        
# ================== Example of Games ================== #
mario_bros = Game("Mario Bros", "Adventure", 200)
pacman = Game("Pacman", "Arcade", 100)
space_invaders = Game("Space Invaders", "Arcade", 150)
street_fighter = Game("Street Fighter", "Fighting", 250)


class GamesCatalog:
    """
    This class represents the catalog of games.
    """
    def __init__(self):
        self.games = [mario_bros, pacman, space_invaders, street_fighter]
    
    def search_by_category(self, category: str) -> list[Game]:
        """
        This method allows to search a game by category.
        
        Args:
            category (str): The category of the game.
        """
        games_by_category = []
        for game in self.games:
            if game.category == category:
                games_by_category.append(game)
        return games_by_category
    
    def show_games(self):
        """
        This method allows to show the games.
        """
        for game in self.games:
            print(f"Name: {game.name}, Category: {game.category}, Price: {game.price}")
    

class Customer:
    """
    This class represents a customer.
    """
    def __init__(self, name: str, adress: str, phone: str, email: str):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.email = email

class PurchaseManager:
    """
    This class represents the purchase manager.
    """
    def __init__(self, customer: Customer, arcade_machine: ArcadeMachine):
        self.customer = customer
        self.arcade_machine = arcade_machine

    def finalize_purchase(self):
        """
        This method allows to finalize the purchase.
        """
        with open("purchase.txt", "a") as file:
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"Customer: {self.customer.name}\n")
            file.write(f"Adress: {self.customer.adress}\n")
            file.write(f"Phone: {self.customer.phone}\n")
            file.write(f"Email: {self.customer.email}\n")
            file.write(f"Arcade machine material: {self.arcade_machine.material}\n")
            file.write("Games:\n")
            for game in self.arcade_machine.games:
                file.write(f"Name: {game.name}, Category: {game.category}, Price: {game.price}\n")
            file.write(f"Total price: {self.arcade_machine.price}\n")
        
        print("The purchase has been finalized.")
