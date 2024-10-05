"""
This module has a class to define a general arcade videogames machine.

Author: Cristian Andres Gamez Nuñez <cagamezn@udistrital.edu.co>

This file is part of Workshop-SM-UD.

Workshop-SM-UD is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop-SM-UD is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop-SM-UD. If not, see <https://www.gnu.org/licenses/>. 

"""
import sys
from videogames import VideoGame
from users import User, Address, Manager, Client
from machines import Machine, ClasicArcadeFactory, DanceRevolutionFactory, ShootingArcadeFactory, RacingArcadeFactory, VirtualRealityFactory
from purchasemanager import PurchaseManager
from videogamescatalog import VideoGamesCatalog


class Main:
    """This class represents the main behavior of the application."""

    MENU_ADMIN = "1.Add Videogame\n2.Remove Videogame\n3.Exit"
    MENU_CLIENT = "1. Choose a Machine\n 2. Exit"
    MENU_CHOOSE_MACHINE = "1. Clasic Arcade Machine\n2. Dance Revolution Machine\n3. Shooting Arcade Machine\n4. Racing Arcade Machine\n5. Virtual Reality Machine\n6. Exit"  
    
    def __init__ (self, user: User):
        self.__catalog = VideoGamesCatalog()
        self.__temp_machine = None
        self.__user: User = user
    
    def show_menu(self):
        """This method shows the menu according to the user type."""
        if isinstance(self.__user, Manager):
            print(Main.MENU_ADMIN)
        elif isinstance(self.__user, Client):
            print(Main.MENU_CLIENT)
    
    def choose_machine(self):
        """This method allows to choose a machine."""
        print(self.MENU_CHOOSE_MACHINE)
        option = int(input("Choose an option: "))
        if option == 1:
            self.__temp_machine = ClasicArcadeFactory()
        elif option == 2:
            self.__temp_machine = DanceRevolutionFactory()
        elif option == 3:
            self.__temp_machine = ShootingArcadeFactory()
        elif option == 4:
            self.__temp_machine = RacingArcadeFactory()
        elif option == 5:
            self.__temp_machine = VirtualRealityFactory()
        else:
            print("Invalid option")
        return self.__temp_machine
    
    def choose_material(self):
        """This method allows to choose the material of the machine."""
        
        if self.__user._grants['buy_machine']:
            material = input(
                "Insert the material of the machine (wood, aluminum or carbon fiber):"
            )
        else:
            print("You do not have permission to choose a material.")
        return material
    
    def show_videogames(self):
        """This method shows the videogames in the catalog."""
        options = [
            [isinstance(self.__temp_machine, ClasicArcadeFactory), "Classic"], 
            [isinstance(self.__temp_machine, DanceRevolutionFactory), "Dance"],
            [isinstance(self.__temp_machine, ShootingArcadeFactory), "Shooting"],
            [isinstance(self.__temp_machine, RacingArcadeFactory), "Racing"],
            [isinstance(self.__temp_machine, VirtualRealityFactory), "Virtual"]
        ]
        for option in options:
            if option[0]:
                category = option[1]
                videogames = self.__catalog.search_by_category(category)
                for vg in videogames:
                    print(vg)
                break
        else:
            print("No machine selected.")
    
    
    def choose_videogames(self):
        """
        Prompts the user to choose videogame for the arcade machine.
        Returns:
            videogame :videogame objects representing the choose videogame.
        """ 
        print("Please, choose the videogame for the arcade machine (Enter the code of videogame): ")  
        videogame_code = int(input())

        for i in range(len(self.__catalog.videogames)):
            if videogame_code == self.__catalog.videogames[i].code:
                videogame = self.__catalog.videogames[i]
                return videogame
        else:
            print("The videogame is not available.")
            return None
    
    def change_user(self, user: User):
        """This method changes the current user."""
        self.__user = user
    
    def create_machine(self):
        """This method creates a machine."""
        if self.__user._grants['buy_machine']:
            material = self.choose_material()
            option_machine = self.choose_machine()
            videogame = self.choose_videogames()
            machine = option_machine.create_machine(material, videogame)
            print("Machine created successfully.")
            return machine
        else:
            print("You do not have permission to create a machine.")
           
            
    def add_videogame(self):
        """This method adds a videogame to the catalog."""
        if self.__user._grants['add_videogame']:
            code = int(input("Insert the code of the videogame:"))
            name = input("Insert the name of the videogame:")
            category = input("Insert the category of the videogame:")
            price = float(input("Insert the price of the videogame:"))
            self.__catalog.add_videogame(VideoGame(code, name, category, price))
        else:
            print("You do not have permission to add videogames.")
    
    def remove_videogame(self):
        """This method removes a videogame from the catalog."""
        if self.__user._grants['remove_videogame']:
            code = int(input("Insert the code of the videogame:"))
            response = self.__catalog.search_by_code(code)
            if response is not None:
                self.__catalog.remove_videogame(response[0])
                print("Videogame removed successfully.")
            else:
                print(f"Videogame with code {code} is not in the catalog.")
        else:
            print("You do not have permission to remove videogames.")
    
    def buy_machine(self):
        """This method buys a machine."""
        if self.__user._grants['buy_machine']:
            purchase_manager = PurchaseManager(self.__user, self. __temp_machine)
            purchase_manager.finalize_purchase()
        else:
            print("You do not have permission to buy a machine.")
            
            
    def __handle_admin(self, option: int):
        exit_ = False
        if option == 1:  # add videogame
            self.add_videogame()
        elif option == 2:  # remove videogame
            self.remove_videogame()
        elif option == 3:  # exit
            print("Manager view is closing!")
            exit_ = True

        return exit_

    def __handle_client(self, option: int) -> bool:
        exit_ = False
        if option == 1:  # choose machine
            self.create_machine()
        elif option == 2:  # buy machine
            self.buy_machine()
        elif option == 3:  # exit
            print("Client view is closing!")
            exit_ = True

        return exit_

    def handle_option(self, option: int) -> bool:
        """This method handles the option selected by the user.

        Args:
            option (int): Option selected by the user.
        """
        if isinstance(self.__user, Manager):
            exit_ = self.__handle_admin(option)
        elif isinstance(self.__user, Client):
            exit_ = self.__handle_client(option)
        return exit_
    
    

def get_user() -> User:
    """This function gets the user type."""
    options = "1.Manager/n2.Client/n3.Exit"
    type_user = int(input(options))

    while type_user not in [1, 2, 3]:
        print("Invalid option. Please try again.")
        type_user = int(input(options))

    user = None
    if type_user == 1:
        user = Manager(1, "admin", "admin@udistrital.edu.co")
    elif type_user == 2:
        address = Address("St. Evergreen 123", 110783, "Springfield", "USA")
        user = Client("Homer Simpson", "dsadas@udistrital.edu.co", "1234567", address)
    elif type_user == 3:
        print("Thanks for using the application. Goodbye!")
        sys.exit()

    return user   

def run():
    """This function runs the application."""
    user = get_user()
    main = Main(user)

    while True:
        while True:
            main.show_menu()
            option = int(input("Enter the option:"))
            if main.handle_option(option):
                break

        user = get_user()
        main.change_user(user)


if __name__ == "__main__":
    run()