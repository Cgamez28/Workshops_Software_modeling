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
from users import User, Manager, Client, Address
from machines import ClasicArcadeFactory, DanceRevolutionFactory, ShootingArcadeFactory, RacingArcadeFactory, VirtualRealityFactory
from purchasemanager import PurchaseManager
from videogamescatalog import VideoGamesCatalog


class Main:
    """This class represents the main behavior of the application."""

    MENU_ADMIN = "1. Add Videogame\n2. Remove Videogame\n3. Exit"
    MENU_CLIENT = "1. Choose a Machine\n2. Buy Machine\n3. Exit"
    MENU_CHOOSE_MACHINE = ("1. Clasic Arcade Machine\n2. Dance Revolution Machine\n3. "
                           "Shooting Arcade Machine\n4. Racing Arcade Machine\n5. Virtual Reality Machine\n6. Exit")

    def __init__(self, user: User):
        self.__catalog = VideoGamesCatalog()
        self.__temp_machine = None
        self.__user = user

    def show_menu(self):
        """Show menu based on user type."""
        if isinstance(self.__user, Manager):
            print(Main.MENU_ADMIN)
        elif isinstance(self.__user, Client):
            print(Main.MENU_CLIENT)

    def choose_machine(self):
        """Allows the client to choose a predefined machine."""
        print(self.MENU_CHOOSE_MACHINE)
        option = int(input("Choose a machine: "))
        if option == 1:
            return ClasicArcadeFactory()
        elif option == 2:
            return DanceRevolutionFactory()
        elif option == 3:
            return ShootingArcadeFactory()
        elif option == 4:
            return RacingArcadeFactory()
        elif option == 5:
            return VirtualRealityFactory()
        else:
            print("Invalid option.")
            return None

    def choose_material(self):
        """Allows the client to choose the material for the machine."""
        material = input("Choose the material of the machine (wood, aluminum, carbon fiber): ")
        return material

    def show_videogames(self):
        """Displays videogames based on the selected machine's category."""
        options = [
            (isinstance(self.__temp_machine, ClasicArcadeFactory), "Classic"),
            (isinstance(self.__temp_machine, DanceRevolutionFactory), "Dance"),
            (isinstance(self.__temp_machine, ShootingArcadeFactory), "Shooting"),
            (isinstance(self.__temp_machine, RacingArcadeFactory), "Racing"),
            (isinstance(self.__temp_machine, VirtualRealityFactory), "Virtual")
        ]
        for option, category in options:
            if option:
                videogames = self.__catalog.search_by_category(category)
                for vg in videogames:
                    print(vg)
                return
        print("No machine selected.")

    def choose_videogames(self):
        """Prompts the user to choose a videogame for the machine."""
        videogame_code = int(input("Enter the code of the videogame you want to add: "))
        videogame = self.__catalog.search_by_code(videogame_code)
        if videogame:
            return videogame
        else:
            print("Videogame not available.")
            return None

    def create_machine(self):
        """Creates a customized machine."""
        self.__temp_machine = self.choose_machine()
        if not self.__temp_machine:
            return None

        material = self.choose_material()
        videogame = self.choose_videogames()

        if videogame:
            machine = self.__temp_machine.create_machine(material, [videogame])
            print("Machine created successfully!")
            return machine
        else:
            print("Machine creation failed.")
            return None

    def add_videogame(self):
        """Allows the manager to add a videogame to the catalog."""
        code = int(input("Insert the code of the videogame: "))
        name = input("Insert the name of the videogame: ")
        category = input("Insert the category of the videogame: ")
        price = float(input("Insert the price of the videogame: "))
        new_game = VideoGame(code, name, "", price, category, "", "", "", 2024)
        self.__catalog.videogames.append(new_game)
        print("Videogame added successfully!")

    def remove_videogame(self):
        """Allows the manager to remove a videogame from the catalog."""
        code = int(input("Insert the code of the videogame: "))
        videogame = self.__catalog.search_by_code(code)
        if videogame:
            self.__catalog.videogames.remove(videogame)
            print("Videogame removed successfully!")
        else:
            print(f"Videogame with code {code} not found.")

    def buy_machine(self):
        """Allows the client to finalize the purchase of the machine."""
        if self.__temp_machine:
            purchase_manager = PurchaseManager(self.__user, self.__temp_machine)
            purchase_manager.finalize_purchase()
        else:
            print("No machine has been created yet.")

    def handle_option(self, option: int) -> bool:
        """Handles menu options for both Manager and Client."""
        if isinstance(self.__user, Manager):
            if option == 1:
                self.add_videogame()
            elif option == 2:
                self.remove_videogame()
            elif option == 3:
                print("Exiting manager view.")
                return True
        elif isinstance(self.__user, Client):
            if option == 1:
                self.create_machine()
            elif option == 2:
                self.buy_machine()
            elif option == 3:
                print("Exiting client view.")
                return True
        return False


def get_user() -> User:
    """Gets the user type (Manager or Client)."""
    options = "1. Manager\n2. Client\n3. Exit\n"
    type_user = int(input(options))

    if type_user == 1:
        return Manager(1, "admin", "admin@udistrital.edu.co")
    elif type_user == 2:
        address = Address("St. Evergreen 123", 110783, "Springfield", "USA")
        return Client("Homer Simpson", "homer@springfield.com", "1234567", address)
    elif type_user == 3:
        print("Thanks for using the application. Goodbye!")
        sys.exit()
    else:
        print("Invalid option.")
        return None


def run():
    """Runs the application."""
    user = get_user()
    main = Main(user)

    while True:
        main.show_menu()
        option = int(input("Enter your option: "))
        if main.handle_option(option):
            break

        user = get_user()
        main.__user = user


if __name__ == "__main__":
    run()
