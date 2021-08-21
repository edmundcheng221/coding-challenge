class Fold:

    """
    Fold left:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example

    return a + b + c + d

    if there is a starting number specified

    return ((((starting + a) + b) + c) + d)
    """
    @staticmethod
    def fold_left(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            if starting is not None:
                lst.insert(0, starting)
            res = lst[0]
            for num,ele in enumerate(lst):
                if num+1 < len(lst):
                    res = operation(res, lst[num+1])
            return res
        except ZeroDivisionError:
            return None

    """
    Fold right:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example
    
    return (a + (b + (c + d)))
    
    if there is a starting number specified
    
    return (starting + (a + (b + (c + d))))
    """

    @staticmethod
    def fold_right(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            if starting is not None:
                new_lst = lst[::-1]
                res = operation(new_lst[0],starting)
                new_lst.pop(0)
                for ele in new_lst:
                    res = operation(ele,res)
                return res
            else:
                new_lst = lst[::-1]
                res = new_lst[0]
                new_lst.pop(0)
                for ele in new_lst:
                    res = operation(ele,res)
                return res
        except ZeroDivisionError:
            return None


def add(item1, item2):
    return item1 + item2


def subtract(item1, item2):
    return item1 - item2


def multiply(item1, item2):
    return item1 * item2


def divide(item1, item2):
    # Cannot divide by 0
    if item2 == 0:
        raise ZeroDivisionError
    return item1 / item2


if __name__ == '__main__':
    instance = Fold()
    output = instance.fold_left(add, [1, 2, 3])
    expected = 6
    assert output == expected, "Incorrect Answer"
