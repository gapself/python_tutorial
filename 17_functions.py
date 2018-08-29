# FUNCTION - a process for executing a task
# - it can accept input and return output
# -useful for executing similar
colors = ['a', 'b', 'c', 'd']
print(colors)
colors.append('e')
print(colors)
colors.clear()
print(colors)


# WHY USE IT? stay DRY - dont repeat yself
def say_hi():
    print('Hi!')


def sing_happy_bday():
    print("Happy bday to U")


sing_happy_bday()


# RETURNING VALUES FROM FUNCTIONS
def print_square_of_7():
    print(7 ** 2)


print_square_of_7()

nums = [1, 2, 3, 4]
length = len(nums)
print(length)
last_item = nums.pop()
print(last_item)


def square_of_7():  # None
    7 ** 2


result = square_of_7()
print(result)


def square_of_7():  # 49
    return 7 ** 2


result = square_of_7()
print(result)


def say_hi():
    return 'Hi'

print(say_hi())

greeting = say_hi()
print(greeting)


def square_of_7():  # 49
    return 7 ** 2
    print('I am after the return')


result = square_of_7()
print(result)


def square_of_7():  # 49           #EXITS the function
    print('I am before the return')
    return 7 ** 2
    print('I am after the return')


result = square_of_7()
print(result)
# outputs whatever value is places after return keyword
# pops the func off of the call stack
# COIN_FLIP function
from random import random


def flip_coin():
    # generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())


# not separated
def flip_coin():
    # generate random number 0-1
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())


# EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEeEEEEEEE
# moje rozwiązanie 1: LIST COMPREHENSION
def generate_evens():
    num = [num for num in range(1, 50) if num % 2 == 0]
    return list(num)


print(generate_evens())


# moje rozw 2: (podobno słabe)
def generate_evens():
    print([num for num in range(1, 50) if num % 2 == 0])


generate_evens()


# rozw.sugerowane: return []
def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]


print(generate_evens())


# rozw.2 sugerowane: using loop
def generate_evens():
    result = []
    for x in range(1, 50):
        if x % 2 == 0:
            result.append(x)  # dodaję jedną rzecz do listy .result.extend, jkabymm dodała kilka
    return result


print(generate_evens())


def square(num):
    return num * num


print(square(4))
print(square(8))


def sing_happy_bday(name):  # NAME is PARAMETER
    print("Happy bday to U")
    print("Happy bday to U")
    print(f"Happy bday Dear {name}")


sing_happy_bday("Simon")  # SIMON IS ARGUMENT


def add(a, b):
    return a + b


def multiply(first, second):
    return first * second


multiply(5, 2)


def print_full_name(string1, string2):
    return (f"Your full name is {string1}{string2}")


def print_full_name(first_name, last_name):
    return (f"Your full name is{first_name}{last_name}")
    # PARAMETERS vs ARGUMENTS


def divide(num1, num2):
    return num1 / num2


print(divide(2, 5))
print(divide(5, 2))


# EXEEEEEEEEEEEEEEEEEEEEEEEEERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# moje rozw: Using the string format() method:
def yell(x):
    return ("{}!".format(x.upper()))


print(yell("go away"))


# inne moje, ale bez parameter + argument
# def yell():
#     x = "go away!".upper()
#     return (x)
# print(yell())
# Using string concatenation:
# def yell(x):
#     return x.upper() + "!"
# # Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(
# def yell(word):
#     return f"{word.upper()}!

# COMMON MISTAKES
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))


# 1+3+5+7 =16 we have only 1 cause "return" is inside the loop
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total  # return outside the"loop"


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))


def exponent(num, power):
    return num ** power


print(exponent(2, 3))
print(exponent(3, 2))


# DEFAULT PARAMS - be more defensive, aboids errors with incorrect param, more readable examples
def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))
print(exponent(7))

countries = ['F', 'A', 'G', 'R']
print(countries.pop())  # without specific item i=nothing, then it return last country 'R


def show_info(first_name='Colt', is_instructor=False):
    if first_name == 'Colt' and is_instructor:
        return "Welcome back inst Colt"
    elif first_name == 'Colt':
        return "I really thought you were an inst"
    return f"Hello {first_name}!"


print(show_info())
print(show_info(is_instructor=True))
print(show_info('Molly'))


def add(a, b):
    return a + b


def math(a, b, fn=add):
    return fn(a, b)


print(math(2, 2))  # 4


def subtract(a, b):
    return a - b


print(math(2, 2, subtract))  # 0


# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERCISEEEEEEEEEEEEEEEEe
# moje rozwiązanie
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == 'duck':
        return "quack"
    elif animal == "dog":
        return "woof"
    elif animal == "cat":
        return "meow"
    else:
        return "?"


print(speak("pig"))
print(speak("dog"))
print(speak("ho"))
print(speak())


# rozwiązanie z DICTIONARIES (z pomocą)
def speak(animal="dog"):
    noise = {"pig": "oink", "duck": "quack", "dog": "woof", "cat": "meow"}
    noise = noise.get(animal)
    if noise:  # it could be animal
        return noise
    return "?"


print(speak("cat"))
print(speak("dog"))


# inne
def speak(animal="dog"):
    noises = {"pig": "oink", "duck": "quack", "dog": "woof", "cat": "meow"}
    return noises.get(animal, "?")


print(speak("pig"))


# KEYWORD ARGUMENTS
def full_name(first, last):
    return f"Your name is {first} {last}"


print(full_name("G", "B"))  # / print(full_name(first = "G", last="B"))


def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49
print(exponent(power=3, num=4))

# SCOPE
instructor = "Colt"


def say_hello():
    return f'Hello {instructor}'


print(say_hello())


def say_hello():
    instructor = 'Colt'
    return f'Hello {instructor}'


print(say_hello())
print(instructor)  # if it is outisde the function, then its error


# total=0
# def increment():
#     total += 1
#     return total
# print(increment()) #error

def increment():
    total = 0
    total += 1
    return total


print(increment())  # 1
# GLOBAL
total = 0


def increment():
    global total  # i say to python what m refering to total(which is outside)
    total += 1
    return total


print(increment())

name = "Gabi"


def greet():
    return name


print(greet())  # Gabi

# name ="Gabi"
# def greet():
#     name += "Paszk"
#     return name
# print(greet()) #Error

name = "Gabi"


def greet():
    global name
    name += "Paszk"
    return name


print(greet())


# NONLOCAL
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()


print(outer())


# DOCUMENTING FUNCTION
def say_hello():
    """A simple funct that returns the str hello"""
    return 'Hello!'


say_hello.__doc__


# print.__doc__
# random.randint.__doc__

def exponent(num, power=2):
    """exponent(num,power) raised"""
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49
print(exponent.__doc__)


# EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def product(a, b):
    return a * b


print(product(2, 2))
print(product(2, -2))


# EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def return_day(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturdat']
    if num > 0 and num <= len(days):
        return days[num - 1]  # coś a la cofka, [num] np dla 1 wyjdzie Monday, a u nas Sunday musi być numerem 1
    return None


print(return_day(1))


# HARD SOL:
def return_day(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num - 1]
    except IndexError as e:
        return None


print(return_day(2))


# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def last_element(list):
    if list == [1, 2, 3]:
        return (list.pop())
    return None


print(last_element([]))


# #inne sugerowane:ale jakiś błąd??
# def last_element(list):
#     if list:
#         return list[-1]
#     return None
# print(last_element([1,2]))
# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"
    return "Numbers are equal"


print(number_compare(2, 3))


# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def single_letter_count(word, letter):
    if "Hello world":
        return word.lower().count(letter.lower())
    return 0


print(single_letter_count("Hello world", "h"))
print(single_letter_count("Hello world", "z"))
print(single_letter_count("Hello world", "l"))


# odp:
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


print(single_letter_count("Hello world", "h"))
print(single_letter_count("Hello world", "z"))
print(single_letter_count("Hello world", "l"))


# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEElle
# blisko
def multiple_letter_count(string):
    return {l: string.count(l) for l in "awesome"}


# if "awesome":
#     return {chr(string).lower():string.count() for string in range (65,90)}
print(multiple_letter_count("awesome"))


# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#zrobiłam sama!
def list_manipulation(list, command, location, value=2):
    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0)
    elif command == "add" and location == "beginning":
        list.insert(0, value)
    elif command == "add" and location == "end":
        list.append(value)
    return list
print(list_manipulation([1, 2, 3], "remove", "end"))
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print(list_manipulation([1, 2, 3], "add", "end", 30))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEee
#simple version that doesnt ignore whitespace:
def is_palindrome(a):
    return a == a[::-1]     #i tgives forward/backward reading
print(is_palindrome('testing'))
#whitespace
def is_palindrome(a):
    b = a.replace('','')    #remove all whitespace
    return b == b[::-1]
print(is_palindrome('testing'))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#sama:
def frequency(list,search_term):
    return list.index(search_term) #mogłam: list.count(searc..)
print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False) )

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def multiply_even_numbers(list):
    # num = [num for num in list if num %2 == 0]
    total = 1
    for num in list:
        if num %2 ==0:
            total *= num #tot=tot*num
    return total
print(multiply_even_numbers([2,3,4,5,6]))
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#sama zrobiłam:
def capitalize(string):
    string = string[0].upper() + string[1:]
    return string #rozw: return string[:1].upper()+string[1:]
print(capitalize("fuck"))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def compact(list):
    # true_value = []
    # for value in list:
    #     if value: true_value.append(value)
    # return true_value
    return  [value for value in list if value]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def intersection(l1,l2):
    return [value for value in l2 if value in l1]
print(intersection([1,2,3],[2,3,4]))
print(intersection(['a','b','z'],['x','y','z']))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def isEven(num):
    return num % 2 == 0
def partition(list,isEven):
    return [[num for num in list if num %2 ==0],[num for num in list if num %2 !=0]]
print(partition([1,2,3,4], isEven))
        #     for value in list
        #     if value: true_value.append(value)
        #     return true_value
        # return [value for value in list if value]
# SPR INNE ROZWIĄZANIA!!!!


