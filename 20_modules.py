#different ways to import
import random

print(random.choice(['a','b','c']))
print(random.randint(1,100))
print(random.shuffle(['ab','bc','cd'])) #None ?

import random as omg
print(omg.choice(['a','b','c']))

from random import choice, randint
print(choice(['a','b','c']))
print(randint(1,100))

from random import choice as pink, randint as blue
print(pink(['a','b','c']))
print(blue(1,100))
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#moje rozwiązanie(odp i tak jest ok)
from math import sqrt as answer
print(answer(15129))
#rozwiązanie sugerowane:
import math
answer = math.sqrt(15129)
print(answer)
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
import keyword
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False #to False nie może być pod if z "else:", ponieważ zwracałoby cały czas #False
print(contains_keyword("hello","goodbye")) #false
print(contains_keyword('four','for','if'))  #true

                                                #CUSTOM MODULES
# #1.sposób
# import MODULES_file
# print(MODULES_file.fn())

#2 sposób
from MODULES_file import fn as pink
print(pink())
                                            #EXTERNAL MODULES
#PIP
#-m pip install name_of_package
# -m pip install termcolor
from termcolor import colored
t = colored("HI there!",color='magenta')
print(t)
import termcolor
print(termcolor.colored("Purple",color='cyan',on_color="on_yellow",attrs=['blink']))
from termcolor import colored
print(colored("GREEN",color='green'))
                                                #HELP list color
# import termcolor
# help(termcolor)

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# moje rozwiązanie:
import pyfiglet
from termcolor import colored
help(pyfiglet.figlet_format)
            #Help on function figlet_format in module pyfiglet:
            #figlet_format(text, font='standard', **kwargs)
text = input('What message do you want to print?')
color = input('What color?')
print(colored(pyfiglet.figlet_format(text), color))

# #rozwiązanie typa:

import keyword
def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
        return False


print(contains_keyword("def", "goodbye"))

