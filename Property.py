
class Rectangle:

    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        self._height
    
    @property
    def width(self):
        self._width

    @height.getter
    def height(self):
        return f"{self._height:.2f}"
    
    @width.getter
    def width(self):
        return f"{self._width:.2f}"
    
    @height.setter
    def height(self, new_height):
        self._height = new_height

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted.")

    @width.deleter
    def width(self):
        del self._width
        print("widht has been deleted.")


rectangle = Rectangle(5, 3)

print(rectangle.height)
print(rectangle.width)
rectangle.height = 10
rectangle.width = 30
print(rectangle.height)
print(rectangle.width)

del rectangle.height
del rectangle.width