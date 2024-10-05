"""
This module contains the machine class and its respective machine factory.

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
from abc import ABC, abstractmethod
from videogames import VideoGame

class Machine(ABC):
    """
    This class represents the behavior of a machine. 
    This act as an abstract class.
    """
    def __init__(self, material: str, videogames: list[VideoGame]):
        self.material = material
        self.__videogames = videogames
    
    @abstractmethod        
    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        pass
    
    @abstractmethod
    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        pass
    
    @abstractmethod        
    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        pass
    
    @abstractmethod
    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        pass
    

class DanceRevolutionMachine(Machine):
    """
    This class represents the behavior of a Dance Rebolution machine.
    """
    def __init__(self, material: str, videogames: list[VideoGame],):        
        super().__init__(material, videogames)
        self.dimensions = (150, 150, 250) # cm
        self.weight = 80 # kg
        self.energy_consumption = 1000 # watts
        self.memory = 64 # GB
        self.processor = "Intel Core i3"
        self.base_price = 7000
        self.dificulties = ['easy', 'medium', 'hard']  
        self.arrow_cardinalities = ['up', 'down', 'left', 'right']
        self.control_price = 1000
        
    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break
        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
            print(f"the videogame with code {code} was removed successfully")
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        if self.material == "wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.energy_consumption *= 1.15
        elif self.material == "aluminium":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "carbon fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.energy_consumption *= 0.90
        else:
            raise ValueError("The material is not available.")
        for videogame in self.__videogames:
            
            self.base_price += videogame.price
        return self.base_price

    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        self.__videogames.append(videogame)

    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.")
            
class ClasicArcadeMachine(Machine):
    """
    This class represents the behavior of a Dance Rebolution machine.
    """
    def __init__(self, material: str, videogames: list[VideoGame],):        
        super().__init__(material, videogames)
        self.dimensions = (180, 70, 60) # cm
        self.weight = 15 # kg
        self.energy_consumption = 200 # watts
        self.memory = 16 # GB
        self.processor = "Raspberry Pi 4"
        self.base_price = 3000 

    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break
        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        if self.material == "wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.energy_consumption *= 1.15
        elif self.material == "aluminium":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "carbon fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.energy_consumption *= 0.90
        else:
            raise ValueError("The material is not available.")
        for videogame in self.__videogames:
            self.base_price += videogame.price
        return self.base_price

    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        self.__videogames.append(videogame)

    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.")
            
class ShootingArcadeMachine(Machine):
    """
    This class represents the behavior of a Dance Rebolution machine.
    """
    def __init__(self, material: str, videogames: list[VideoGame]):        
        super().__init__(material, videogames)
        self.num_shots = 30
        self.objetives = ['human', 'zombie', 'animal']  
        self.dimensions = (200, 100, 70) # cm
        self.weight = 40 # kg
        self.energy_consumption = 450 # watts
        self.memory = 24 # GB
        self.processor = "Intel Core i5"
        self.base_price = 5000

    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break
        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        if self.material == "wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.energy_consumption *= 1.15
        elif self.material == "aluminium":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "carbon fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.energy_consumption *= 0.90
        else:
            raise ValueError("The material is not available.")
        for videogame in self.__videogames:
            self.base_price += videogame.price
        return self.base_price

    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        self.__videogames.append(videogame)
        
    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.")    
    
class RacingArcadeMachine(Machine):
    """
    This class represents the behavior of a racing arcade machine.
    """
    def __init__(self, material: str, videogames: list[VideoGame]):        
        super().__init__(material, videogames, )
        self.num_players = 1   
        self.dimensions = (200, 180, 110) # cm
        self.weight = 90 # kg
        self.energy_consumption = 700 # watts
        self.memory = 16 # GB
        self.processor = "Raspberry Pi 4"
        self.base_price = 7000
        
    def choose_num_players(self, num_players: int):
        """
        This method allows to choose the number of players of the arcade machine.
        
        Args: 
            num_players (int): The number of players of the arcade machine.
        """
        if num_players not in [1, 2]:
            raise ValueError("The number of players is not available.")
        
        self.num_players = num_players

    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break
        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        if self.material == "wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.energy_consumption *= 1.15
        elif self.material == "aluminium":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "carbon fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.energy_consumption *= 0.90
        else:
            raise ValueError("The material is not available.")
        for videogame in self.__videogames:
            self.base_price += videogame.price
        return self.base_price

    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        self.__videogames.append(videogame)
        
    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.")   
    
    def make_vibration(self):
        print("the machine is vibrating")

    def sound_record_alert(self):
        print("the machine is recording the sound") 
             
class VirtualRealityMachine(Machine):
    """
    This class represents the behavior of a virtual reality arcade machine.
    """
    def __init__(self, material: str, videogames: list[VideoGame], glasses_type: str, glasses_resolution: tuple, glasses_price: float):        
        super().__init__(material, videogames)
        self.dimensions = (15, 22, 10) # cm
        self.weight = 0.7 # kg
        self.energy_consumption = 80 # watts
        self.memory = 4 # GB
        self.processor = "Raspberry Pi 4"
        self.base_price = 3000
        self.glasses_type = glasses_type
        self.glasses_resolution = glasses_resolution
        self.glasses_price = glasses_price  

    def remove_videogame(self, code: int):
        """This method removes a videogame from the machine.

        In this method based on videogame code, if the videogame 
        exists it will be removed from current machine.

        Args:
            code (int): Code of the videogame to be removed.
        """
        index = -1 # logic mark
        for i, vg in enumerate(self.__videogames):
            if vg.get_code() == code:
                index = i
                break
        if index != -1: # videogame is in machine
            self.__videogames.pop(index)
        else:
            print(f"VideoGame with code {code} it not in the machine.")

    def calculate_price(self):
        """
        This method allows to calculate the price an weight of the machine.
        """
        if self.material == "wood":
            self.weight *= 1.1
            self.base_price *= 0.95
            self.energy_consumption *= 1.15
        elif self.material == "aluminium":
            self.weight *= 0.95
            self.base_price *= 1.1
        elif self.material == "carbon fiber":
            self.weight *= 0.85
            self.base_price *= 1.2
            self.energy_consumption *= 0.90
        else:
            raise ValueError("The material is not available.")
        for videogame in self.__videogames:
            self.base_price += videogame.price
        return self.base_price
    
    def add_videogame(self, videogame: VideoGame):
        """
        This method allows to add a game to the arcade machine.
        
        Args:
            videogame (Game): The videogame to add.
        """
        self.__videogames.append(videogame)
        
    def show_videogames(self):
        """This method show all videogames in the current machine.

        In this method the list of videogames is printed following
        a format of code and name.
        """
        if len(self.__videogames) > 0:
            print("Code\tName")
            for vg in self.__videogames:
                print(vg)
        else:
            print("No videogames have been added.") 
             
class MachineFactory:
    """
    This class represents the machine factory.
    """
    def __init__(self):
        self.__machines = []
    
    def create_machine(self, material: str, videogames: list[VideoGame]):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
        """
        machine = Machine(material, videogames)
        self.__machines.append(machine)
        return machine

    def show_machines(self):
        """
        This method shows all machines in the factory.
        """
        for machine in self.__machines:
            print(machine)

    def __str__(self) -> str:   
        temp_machines = ""
        for machine in self.__machines:
            
            temp_machines += str(machine)
        return temp_machines

class DanceRevolutionFactory(MachineFactory):
    """
    This class represents the Dance Revolution machine factory.
    """
    def create_machine(self, material: str, videogames: list[VideoGame]):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
        """
        machine = DanceRevolutionMachine(material, videogames)
        self.__machines.append(machine)
        return machine

class ClasicArcadeFactory(MachineFactory):
    """
    This class represents the Clasic Arcade machine factory.
    """
    def create_machine(self, material: str, videogames: list[VideoGame]):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
        """
        machine = ClasicArcadeMachine(material, videogames)
        self.__machines.append(machine)
        return machine

class ShootingArcadeFactory(MachineFactory):
    """
    This class represents the Shooting Arcade machine factory.
    """
    def create_machine(self, material: str, videogames: list[VideoGame]):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
        """
        machine = ShootingArcadeMachine(material, videogames)
        self.__machines.append(machine)
        return machine

class RacingArcadeFactory(MachineFactory):
    """
    This class represents the Racing Arcade machine factory.
    """
    def create_machine(self, material: str, videogames: list[VideoGame]):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
        """
        machine = RacingArcadeMachine(material, videogames)
        self.__machines.append(machine)
        return machine

class VirtualRealityFactory(MachineFactory):
    """
    This class represents the Virtual Reality machine factory.
    """
    def create_machine(self, material: str, videogames: list[VideoGame], glasses_type: str, glasses_resolution: tuple, glasses_price: float):
        """
        This method allows to create a machine.
        
        Args:
            material (str): The material of the machine.
            videogames (list[VideoGame]): The videogames of the machine.
            glasses_type (str): The type of the glasses.
            glasses_resolution (tuple): The resolution of the glasses.
            glasses_price (float): The price of the glasses.
        """
        machine = VirtualRealityMachine(material, videogames, glasses_type, glasses_resolution, glasses_price)
        self.__machines.append(machine)
        return machine

