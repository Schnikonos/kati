from typing import List


# intellij will understand that some_int is of type int, some_str is of type str and some_list is a list of int
class ClassWithTyping:
    def __init__(self, some_int: int, some_string: str, some_list: List[int]):
        self.some_int = some_int
        self.some_string = some_string
        self.some_list = some_list


if __name__ == '__main__':
    myClass = ClassWithTyping(1, 'a', [1, 2, 3])
    print('myClass:', myClass.some_int, myClass.some_string, myClass.some_list)
    # try to write myClass.some_list.   -> intellij will propose you all methods that are related to a list of int

    # no error mentioned by intellij as types are respected
    print('myClass:', myClass.some_int + 1, myClass.some_string + 'a', myClass.some_list + [4])

    # intellij shows you some warning. By leaving your mouse on them, you can get some details
    try:
        print('myClass:', 'a' + myClass.some_int, myClass.some_string + 1, myClass.some_list + 'b')
    except:
        pass

    # still typings are only here for information. You're free to not respect them if you wish
    myClass.some_int = 'a'
    myClass.some_string = 1
    myClass.some_list = 'b'
    print('myClass:', 'a' + myClass.some_int, myClass.some_string + 1, myClass.some_list + 'b')
