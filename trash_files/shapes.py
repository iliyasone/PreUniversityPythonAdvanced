from abc import ABC, abstractmethod
from math import pi

# делаем Shape абстрактным базовым классом, чтобы нельзя
# было создавать экземпляры этого класса
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        return 0
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self._radius = radius
        
    def area(self) -> float:
        return self._radius ** 2 * pi

class Rectangle(Shape):
    def __init__(self, width: float, length: float) -> None:
        super().__init__()
        self._width = width
        self._length = length
        
        
    def get_length(self) -> float:
        return self._length
    
    def get_width(self) -> float:
        return self._width
    
    def area(self):
        return self._width * self._length
        
    def perimeter(self):
        return (self._width + self._length) * 2
    
def get_square(length: float):
    return Rectangle(length, length)

class Square(Rectangle):
    def __init__(self, length: float) -> None:
        super().__init__(length, length)
    
    def area(self):
        return self._width * self._width
    
c = Circle(1)
print(c.area())