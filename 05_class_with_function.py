
PI = 3.14


class ClassWithFunction:
    def __init__(self, radius: float):
        self.radius = radius

    def get_circle_perimeter(self):
        return self.radius * 2 * PI

    # you can also show the return type of the function with typings
    def get_circle_area(self) -> float:
        return self.radius * PI * PI


if __name__ == '__main__':
    myClass = ClassWithFunction(5.0)
    print('MyClass:', myClass.radius, myClass.get_circle_perimeter(), myClass.get_circle_area())

    myClass2 = ClassWithFunction(2.0)
    print('MyClass2:', myClass2.radius, myClass2.get_circle_perimeter(), myClass2.get_circle_area())
