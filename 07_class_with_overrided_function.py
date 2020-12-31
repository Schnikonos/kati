
PI = 3.14


class ClassWithOverridedFunction:
    def __init__(self, radius: float, name: str):
        self.radius = radius
        self.name = name

    def get_circle_perimeter(self):
        return self.radius * 2 * PI

    # you can also show the return type of the function with typings
    def get_circle_area(self) -> float:
        return self.radius * PI * PI

    # [optional] by overriding __repr__, you can easily print your object the way you want it
    def __repr__(self):
        return 'Circle[r={}/area={}/name={}]'.format(self.radius, self.get_circle_area(), self.name)

    # [optional] by overriding __eq__, you can easily find your object in a list
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __hash__(self):
        return int(self.radius)


if __name__ == '__main__':
    myClass = ClassWithOverridedFunction(5.0, 'myClass')
    print('MyClass:', myClass)  # this use __repr__ to print the class. If not overrided, you'd get something like: <__main__.ClassWithFunction object at 0x00CDA970>

    myClass2 = ClassWithOverridedFunction(2.0, 'myClass2')
    print('MyClass2:', myClass2.radius, myClass2.get_circle_area(), myClass2.get_circle_perimeter())

    myClassBis = ClassWithOverridedFunction(5.0, 'myClassBis')
    myClass3 = ClassWithOverridedFunction(3.0, 'myClass3')
    myList = [myClass, myClass2]
    assert myClass in myList  # works even without __eq__ overrided because you are using the instance that is in the list
    assert myClassBis in myList  # works only because __eq__ is overrided and you use the radius to know if 2 circle are equal
    assert myClass3 not in myList

    # by overriding __lt__, you can easily sort your lists
    print(myList)
    myList.sort()
    print(myList)

    # by overriding __hash__ you can place your objects in sets
    mySet = {myClass, myClass2, myClassBis}
    print(mySet)  # as myClass and myClassBis have the same hash, only myClass appears in the set

    # by overriding __hash__, the object can also be used as a key in the dict
    myDict = {myClass: 'a', myClass2: 'b'}
    print(myDict)
    myDict[myClassBis] = 'c'  # overrides value of myClass as both have the same hash
    myDict[myClass3] = 'd'    # no similar hash in the dict -> is added to the dict
    print(myDict)
