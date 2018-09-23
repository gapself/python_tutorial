                        #HIGHER ORDER FUNCT
def sum(n,func):
    total =0
    for num in range(1,n+1):
        total += func(num)
    return total
def square(x):
    return x*x
def cube(x):
    return x*x*x
print(sum(3,cube))  #36
print(sum(3,square)) #14
# 0+1+2
# 0+1+4 range(3)
# 1,2,3
# 1 4 9 = # 14 range(1,n+1)
print(sum(2,square)) #1
print(sum(4,square)) #14

# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#niby dobra odp, a nie działa:
#
# from functools import wraps
def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Here'are the args: {args}") #albo ("Here are the args:", args)
        print(f"Here're the kwargs {kwargs}")
        return fn(*args,**kwargs)
    return wrapper

wrapper(1,2,3,a="nie"")

#moja działą:
from functools import wraps
def show_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(f"Here are the args: {args}")
        print(f"Here are the kwargs {kwargs}")
        return fn (*args,**kwargs)
    return wrapper
@show_args
def do_nothing(*args,**kwargs):
    pass

# do_nothing(1, 2, 3,a="hi",b="bye")


from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sory:(")
        return fn(*args,**kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi there {name}")

# greet("Tony")

# #EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
from functools import wraps
def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        val = fn(*args,**kwargs)
        return [val,val]
    return wrapper
@double_return
def add(x,y):
    return x+y
@double_return
def greet(name):
    return "Hi,I'm " + name
print(add(1,2))
print(greet("Tom"))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#GOT IT :)
from functools import wraps
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def sth(*args):
        if len(args)>= 3:
            return "Too many arguments!"
        return fn(*args)
    return sth
@ensure_fewer_than_three_args
def add_all(*args):
    return sum(args)
print(add_all(1,2))

#EXEEEEEEEEEEEEEEEEEEEEe
#byłam blisko, ale chciałam używać if, a powinnam FOR IN (FOR nums in lista args: JEŚLI COŚ, to druknij)
from functools import wraps
def only_ints(fn):
    @wraps(fn)
    def only_ints(*args):
        for arg in args: #nie mój zapis: if any ([arg for arg in args if type(arg) != int]): returm""
            if type(arg) != int:
                return "Please only invoke with integers."
            return fn(*args)
    return only_ints
@only_ints
def add (x,y):
    return x+y
print(add(1,2))
print(add("1","2"))
# print(add("1","2"))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#:< z ifem zabalowałam
from functools import wraps
def ensure_authorized(fn):
    @wraps(fn)
    def ensure_authorized(*args,**kwargs):
        if kwargs.get("role") == "admin": #PRZYPOMNIJ SOBIE GEEEEEEEET!!
            return fn(*args, **kwargs)
        return "Unauthorized"
    return ensure_authorized
@ensure_authorized
def show_secrets(*args,**kwargs):
    return 'Shh! Dont tell anybody!'

show_secrets(role="admin")
print(show_secrets(role="admin"))
print(show_secrets(role="nobody"))
print(show_secrets(a="b"))

                                #ZIP DECORATORS !!
def enforce(*types):
    def decorator(f):
        def new_func(*args,**kwargs):
            newargs = []
            for (a,t) in zip (args,types):
                newargs.append(t(a))
            return f(*newargs,**kwargs)
        return new_func
    return decorator
@enforce(str,int)
def repeat_msg(msg,times):
    for time in range(times):
        print(msg)
@enforce(float,float)
def divide(a,b):
    print (a/b)
repeat_msg("hello",5)
                       # ZIP # ("hello", str) ("3",int)
                       #  ["hello","3"]
divide("2","3")
divide("2","4")


                                    #FIRST_ARG!
from functools import wraps
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args and args[0] != val: #if args exist (args) and if first one (args[0])
                return f"Invalid! First argument must be {val}"
            return fn(*args,**kwargs)
        return wrapper
    return inner
@ensure_first_arg_is("burrito")
def fav_foods(*args):
    return args

print(fav_foods("burrito","ice cream"))
print(fav_foods("ice cream","burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1,num2):
    return num1+num2
print(add_to_ten(10,12))
print(add_to_ten(1,2))

#ExEEEEEEEEEEEEEEE WHAAAAAAAAAAAAAAAAAAAAAAAAAAAT THE FUCK- czemu to się nie drukuje!!!!!!!!!!!!! KURWAAAAAAAAAAAAAAAAAA

from functools import wraps
from time import sleep

def delay(time):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            print (f"Waiting {} before running {}".format(time,fn.__name__)
            sleep(time)
            return fn(*args,**kwargs)
        return wrapper
    return inner
@delay()
def say_hi():
return "hi"

print(say_hi(3))
