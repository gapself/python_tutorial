#*args - special operator we can pass to function; gathers remaining arguments as a tuple
#this is just a parameter-call it how you want
def sum_all_nums(num1,num2,num3):
    return num1+num2+num3
print(sum_all_nums(4,6,9))  #19
#want add more numbers after num3 or write only (4,6)
def sum_all_nums(*args):
    print(args)                #19
print(sum_all_nums(4,6,9))  #TUPLE containing (4,6,9)
def sum_all_nums(num1,*args):
    print(num1)
    total=0
    for num in args:
        total+=num
    return total
print(sum_all_nums(4,6)) # 4 ...6
print(sum_all_nums(4,6,9,10,9)) #4..34

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def contains_purple(*args):
#moje rozwiązanie:
        for arg in args:
            if arg == "purple":
                return True
        return False            #dlaczego nie mogę esle:return False?
print(contains_purple(25,"purple"))
print(contains_purple(25,"wow",False))
print(contains_purple("wow"))
print(contains_purple("purple", 1,2))
print(contains_purple(25,"purple"))
#rozw:
def contains_purple(*args):
    if "purple" in args: return True
    return False
print("wow")
print(contains_purple(25,"purple"))
                                        #**KWARGS !!
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person} fav color is {color}")

print(fav_colors(colt="purple",ruby="red",ethel="teal"))
#colt fav color is purple

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs ['David']=='special':
        return "You get a special greeting"
    elif 'David'in kwargs:
        return f"{kwargs ['David']} David!"
    return "Not sure who this is.."
print(special_greeting(David="hello"))
print(special_greeting(Bob="hello"))
print(special_greeting(David="special"))
print(special_greeting(David="special",Heather ="hello"))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEERCISEEEEEEEEEEEEEEEEEEEEEEE
#:)sama:
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return f"{kwargs['prefix']}{word}" #albo  "{}{}".format(kwargs['prefix'],word)
    elif 'suffix' in kwargs:
        return f"{word}{kwargs['suffix']}"
    else:
        return word

print(combine_words("child"))
print(combine_words("child",prefix="man"))
print(combine_words("child",suffix="ish"))
print(combine_words("work",suffix="er"))
# print(combine_words(word=1))
                                    #PARAMETER ORDERUNG
                                    #1.parameters
                                    #2.*args
                                    #3.defauls parameters
                                    #4**kwargs
def display_info(a,b,*args,instr="colt",**kwargs):
    # return[a,b,args,instr,kwargs]
    print(args) #(3,), None
    print(type(args)) #SINGLE ITEM tuple
    print(kwargs)
print(display_info(1,2,3,last="Steele",job="inst"))
#[1, 2, (3,), 'colt', {'last': 'Steele', 'job': 'inst'}]
#(3,) cause its tuple

                                #TUPLE * as an ARGUMENT UNPACKING values
def sum_all_values(*args):
    print(args)             #([1, 2, 3, 4, 5, 6],)
    total =0
    for num in args:
        total += num
    print(total)
# print(sum_all_values(1,2,3)) #6
nums = (1,2,3,4,5,6)        #(1, 2, 3, 4, 5, 6) ... 21
sum_all_values(*nums)
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:
result1 = count_sevens(1,4,7)
result2 =count_sevens(*nums)
print(result1)      #1 bo w result1 jest jedna 7
print(result2)      #14 (bo tyle jest 7 w list)
#=============================NIE CZAJE ================================
def display_names(first, second):
    print(f"{first} says hello to {second}")
# names = {"first":"Colt","second":"Rusty"}
# # display_names(first="Charlie", second="Sue")
# # display_names(**names)
display_names(first="Colt",second="Rusty")

def add_and_multiply_nums (a,b,c,**kwargs):
    print(a+b*c)
    print("other stuff...")
    print(kwargs)               #{'d': 55, 'name': 'Tony'}
data = dict (a=1,b=2,c=3,d=55, name="Tony")
# print(add_and_multiply_nums())
#
add_and_multiply_nums(**data, cat="blue") #7 #{'d': 55, 'name': 'Tony'  it added cat:blue}
 #EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def calculate (**kwargs):
    # print("make_float")
    if "make_float" in kwargs:
        return False
    # else:
list = calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
print(calculate(5))
