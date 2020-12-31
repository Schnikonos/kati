
class ClassWithConstructor:
    # constructors are useful to prefill attributes and maybe do some initial computation
    def __init__(self, some_int, some_string, some_list):
        self.some_int = some_int
        self.some_string = some_string
        self.some_list = some_list

        self.some_double_int = some_int * 2


if __name__ == '__main__':
    myClass = ClassWithConstructor(1, 'a', [1, 2, 3])
    print('myClass:', myClass.some_int, myClass.some_string, myClass.some_list, myClass.some_double_int)

    # change values (some_double_int is only set during __init__ and will not be changed if some_int is changed)
    myClass.some_int = 111
    myClass.some_string = 'z'
    myClass.some_list = [3, 2, 1]
    print('myClass changed:', myClass.some_int, myClass.some_string, myClass.some_list, myClass.some_double_int)
