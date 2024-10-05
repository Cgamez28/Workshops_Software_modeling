"""
This module has a class to define a videogame catalog.

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
from videogames import VideoGame

dance_revolution = VideoGame(1, "Dance Revolution", "Dance", 100.0, "Dance", "HD", "Sofia", "Liam", 2023)
super_mario = VideoGame(2, "Super Mario Bros", "Classic game", 50.0, "Classic", "Standard", "Sofia", "Liam", 1985)
legend_zelda = VideoGame(3, "The Legend of Zelda", "Classic game", 80.0, "Classic", "HD", "Sofia", "Liam", 1986)
street_fighter = VideoGame(4, "Street Fighter", "Classic game", 70.0, "Classic", "HD", "Sofia", "Liam", 1987) 
pacman = VideoGame(5, "PacMan", "Classic game", 40.0, "Classic", "Standard", "Sofia", "Liam", 1980)
gunfire = VideoGame(6, "Gunfire Assault", "shoot game", 60.0, "Shooter", "HD", "Sofia", "Liam", 2023)
nitrospeed = VideoGame(7, "Nitro Speed", "racing game", 70.0, "Racing", "HD", "Sofia", "Liam", 2023)
virtual_quest = VideoGame(8, "Virtual Quest", "virtual game", 70.0, "Virtual", "HD", "Sofia", "Liam", 2023)

class VideoGamesCatalog:
    """
    This class represents the catalog of games.
    """
    def __init__(self):
        self.videogames = [
            dance_revolution,
            super_mario,
            legend_zelda,
            street_fighter,
            pacman,
            gunfire,
            nitrospeed,
            virtual_quest
            ]
    
            
    def search_by_code(self, code: int) -> VideoGame: 
        """
        This method allows to search a videogame by code.
        
        Args:
            code (int): The code of the VideoGame.
        """
        for videogame in self.videogames:
            if videogame.code == code:
                return videogame
        return None
    
    def search_by_category(self, category: str) -> list[VideoGame]:
        """
        This method allows to search a videogame by category.
        
        Args:
            category (str): The category of the VideoGame.
        """
        games_by_category = []
        for videogame in self.videogames:
            if videogame.category == category:
                games_by_category.append(videogame)
        return games_by_category
    
    def show_games(self):
        """
        This method allows to show the games.
        """
        for videogame in self.videogames:
            print(f"code: {videogame.code}, Name: {videogame.name}, Category: {videogame.category}, Price: {videogame.price}")