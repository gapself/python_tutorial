                                #ASSERTIONS (keyword)

def add(x,y):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return x+y
    # assert x > 0 and x < 0, "Both numbers must be positive"

def double(values):
    """ double the values in a list
    >>> double ([1,2,3,4])
    [2, 4, 6, 8]
    >>> double ([])
    []
    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']
    """
    return [2 * element for element in values]


print(add(1,1)) #2
print(add_numbers(1,-1)) #AssertionError: Both n o must be posi


#if it runs with the -O flag, then assertions're not evaluate

def eat_junk(food):
    assert food in [
        'pizza',
        'ice cream',
        'candy',
        'fried butter'
    ], "food must be a in [junkfood]"
    return f"NOMNOM Im eating {food}"

food = input("ENTER A FOOD, PLEASE")
print(eat_junk(food))


                            #UNITTESTS
from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy,bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "because YOLO!"
    if is_healthy:
        ending = "cause my body"
    return f"Im eating {food}, {ending}"
def nap(num_hours):
    # beginning =
    if num_hours <= 1:
        return f"Im feeling refreshed after {num_hours}hr"
    return f"I overslept {num_hours}hrs"
def laugh():
    return choice(['lol','haha','hehe'])
def is_funny(anyone):
    anyone = ("gabi","srabi")
    if not is_funny:
        return False
    return True
# def bolean(food,is_healthy):