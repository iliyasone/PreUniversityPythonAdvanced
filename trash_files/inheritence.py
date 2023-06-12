from typing import Iterable


class Ingredient:
    country = "Russia" 
    
    def __init__(self, weigth: float, callorage: int) -> None:
        self._weigth = weigth
        self._callorage = callorage

    def get_weigth(self) -> float:
        return self._weigth
    
    def get_callorage(self) -> int:
        return self._callorage
    
    def prepare(self) -> None:
        """Готовит продукт к еде"""
        pass
    
class Bread(Ingredient):        
    def prepare(self):
        print("Bread servered")
    
class Tomato(Ingredient):
    def prepare(self):
        print("Tomato fried")
        self._weigth *= 0.8
        self._callorage *= 1.1

class Potato(Ingredient):
    def prepare(self):
        print("Potato salted")
        self._weigth += 0.01
        self._callorage
        
class Berries(Ingredient):
    def __init__(self, count: int, weigth: float, callorage: int) -> None:
        super().__init__(weigth, callorage)
        self._count = count
        
        
potato, tomato, bread = Potato(0.3, 500), Tomato(0.4, 200), Bread(0.1,10)

def make_dinner(ingredients: Iterable[Ingredient]):
    callorage = 0
    for ingredient in ingredients:
        ingredient.prepare()
        callorage += ingredient.get_callorage()
    print(f"Dinner was made, total {callorage}")

make_dinner((potato, tomato, bread))