
class ClassWithDefaultConstructor:
    def __init__(self, some_int=1, some_string='a', some_list=None):
        if some_list is None:   # read the following if you want more details on why list must be initialized this way: https://florimond.dev/blog/articles/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
            some_list = [1, 2, 3]
        self.some_int = some_int
        self.some_string = some_string
        self.some_list = some_list


if __name__ == '__main__':
    myClass = ClassWithDefaultConstructor()
    print('myClass:', myClass.some_int, myClass.some_string, myClass.some_list)

    myClass2 = ClassWithDefaultConstructor(2)
    print('myClass2:', myClass2.some_int, myClass2.some_string, myClass2.some_list)

    myClass3 = ClassWithDefaultConstructor(2, 'b')
    print('myClass3:', myClass3.some_int, myClass3.some_string, myClass3.some_list)

    myClass4 = ClassWithDefaultConstructor(2, 'b', [3, 2, 1])
    print('myClass4:', myClass4.some_int, myClass4.some_string, myClass4.some_list)

    # argument can be explicitly defined
    myClass5 = ClassWithDefaultConstructor(some_list=[3, 2, 1], some_string='b', some_int=2)
    print('myClass5:', myClass5.some_int, myClass5.some_string, myClass5.some_list)

    myClass6 = ClassWithDefaultConstructor(some_string='b')
    print('myClass6:', myClass6.some_int, myClass6.some_string, myClass6.some_list)
