from abc import abstractmethod

class shape:

    @abstractmethod
    def area(self):
        pass

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
class pizza(circle):
    def __init__(self, topping,  radius):
        super().__init__(radius)
        self.topping = topping
    
circle1 = circle(2)
print(circle1.area())

pizza1 = pizza("pepporoni", 10)
print(f"{pizza1.topping} and {pizza1.area()}")