from collections import defaultdict
from typing import List, Dict

if __name__ == '__main__':
    # Solution 1: use a function that test if the key is present, and if not, initialize it
    def get_1(key: str, d: Dict[str, List]) -> List:
        if key not in d:
            d[key] = []
        return d[key]

    my_dict1 = {}
    get_1('a', my_dict1).extend([1, 2, 3])
    get_1('a', my_dict1).extend([4, 5, 6])
    get_1('b', my_dict1).extend([3, 2, 1])
    print(my_dict1)

    # solution 2: use setdefault
    def get_2(key: str, d: Dict[str, List]) -> List:
        d.setdefault(key, [])
        return d[key]

    my_dict2 = {}
    get_2('a', my_dict2).extend([1, 2, 3])
    get_2('a', my_dict2).extend([4, 5, 6])
    get_2('b', my_dict2).extend([3, 2, 1])
    print(my_dict2)

    # solution 3 (my favourite): use default dict
    my_dict3 = defaultdict(list)
    my_dict3['a'].extend([1, 2, 3])
    my_dict3['a'].extend([4, 5, 6])
    my_dict3['b'].extend([3, 2, 1])
    print(my_dict3)