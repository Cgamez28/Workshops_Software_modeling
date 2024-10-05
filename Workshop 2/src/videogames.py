"""
This module has a class to define a simple videogame.

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

class VideoGame:
    """This class represents the behavior of a general videogame."""

    def __init__(self, code: int, name: str, description: str, price: float, category: str, definition: str, 
                 storytelling_creator: str, graphics_creator: str, year: int): 
        self.__code = code
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.definition = definition # HD or standard definition
        self.storytelling_creator = storytelling_creator
        self.graphics_creator = graphics_creator
        self.year = year
 
    def get_code(self) -> int:
        """This method returns the code of the videogame.
        
        Returns:
            An integer with the code of the videogame.
        """
        return self.__code

    def set_description(self, description: str):
        """This method changes the description of the videogame.
        
        Args:
            description (str): New description of the videogame.
        """
        self.description = description
            
    def add_definition(self):
        """
        This method adds a 10% to the price of the videogame if it is in HD.
        """
        if self.definition == "HD":
            self.price *= 1.1
            
    def __str__(self) -> str:
        return f"Code: {self.__code}, Name: {self.name}, Description: {self.description}"
