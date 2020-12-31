
# parent class
class Rectangle:
    def __init__(self, height: int, length: int):
        self.height = height
        self.length = length

    def get_area(self) -> int:
        return self.length * self.height

    def get_name(self) -> str:
        return 'I am a rectangle'


# child class -> a square is like a rectangle
class Square(Rectangle):
    def __init__(self, height: int):
        super().__init__(height, height)

    # parent's methods can be overridden
    def get_name(self) -> str:
        return 'I am a square'


if __name__ == '__main__':
    myRectangle = Rectangle(2, 3)
    print('rectangle', myRectangle.get_name(), myRectangle.get_area())

    # square reuses the structure and methods of Rectangle, and can overwrite some
    # here get_area is defined in Rectangle and doesn't change in Square
    # This is useful when you use objects that are highly similar and you wish to avoid code duplication
    mySquare = Square(3)
    print('square', mySquare.get_name(), mySquare.get_area())
