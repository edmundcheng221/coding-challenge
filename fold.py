class Fold:

    """
    Fold left:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example

    return a + b + c + d

    if there is a starting number specified

    return starting + (a + b + c + d)
    """
    @staticmethod
    def fold_left(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            l = list(lst)
            res = l[0]
            for num,ele in enumerate(l):
                if num == 0:
                    pass
                else:
                    res = operation(res, ele)
            if starting is not None:
                return operation(res, starting)
            return res
        except ZeroDivisionError:
            return None

    """
    Fold right:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example
    
    return a + (b + c + d)
    
    if there is a starting number specified
    
    return starting + (a + (b + c + d))
    """

    @staticmethod
    def fold_right(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            l = list(lst)
            temp = l[0]
            l.pop(0)
            res = l[0]
            for num,ele in enumerate(l):
                if num+1 < len(l):
                    res = operation(res, l[num+1])
            if starting is not None:
                result = operation(temp, res)
                return operation(result, starting)
            return operation(temp, res)
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