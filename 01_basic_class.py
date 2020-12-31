
class BasicClass:
    # attributes are defined with 'name = value'
    some_int = 42
    some_string = 'a'
    some_list = [1, 2, 3]


if __name__ == '__main__':
    myClass = BasicClass()  # creates a new instance of the class
    print('myClass:', myClass.some_int, myClass.some_string, myClass.some_list)

    # change values
    myClass.some_int = 111
    myClass.some_string = 'z'
    myClass.some_list = [3, 2, 1]
    print('myClass changed:', myClass.some_int, myClass.some_string, myClass.some_list)

    # create other separate instance
    myOtherClass = BasicClass()
    print('myOtherClass:', myOtherClass.some_int, myOtherClass.some_string, myOtherClass.some_list)
    print('myClass:', myClass.some_int, myClass.some_string, myClass.some_list)

    # attributes aren't typed and you can change them (but this is highly discouraged !!)
    myClass.some_int = 'a'
    myClass.some_string = [1, 2, 3]
    myClass.some_list = 1
    print('myClass mixed attributes:', myClass.some_int, myClass.some_string, myClass.some_list)
