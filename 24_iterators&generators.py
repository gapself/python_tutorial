#ITERATORS vs ITERABLES
name = "Gabi"
# print(next(name)) #TypeError: 'str' object is not an iterator
it = iter(name)
# print(it) #<str_iterator

nums = [1,2,3,4]
# print(next(nums)) #TypeError: 'list' object is not an iterator
it = iter(nums)
# print(next(it)) #1
# print(next(it)) #2

                                        #CUSTOM FOR LOOP
# for num in [1,2,3]
# for char in "hi there"

# iter()
# next()
# next()

def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
            # print(next(iterator)) #hello
        except StopIteration:
            # print("END of iterator")
            break
        else:
            func(thing)
def square(x):
    print(x*x)
#     print(next(iterator)) #h
#     print(next(iterator))  #e ..until StopIteration Error
# # my_for('hello')
# my_for([1,2,3,4],print) #1234
# my_for("lol",print) #lol (pion)
# my_for([1,2,3,4],square)

                                        #CUSTOM ITERATOR
class Counter:
    def __init__(self,low, high):
        self.current = low
        self.high =high
    def __iter__(self):
        return self
        # return iter("hello")
    def __next__(self):
        # return 1 #111111111 print infinite iterator
        if self.current < self.high:
            num = self.current
            self.current +=1
            return num
        raise StopIteration
# c = Counter(0,10)
# iter(c)
# for x in Counter(0,10): #low is 0, high is 10
#     print(x)
                                                #GENERATOR
def count_up_to(max):
    count=1
    while count <= max:
        yield count
        count +=1

c = count_up_to(10)
# print(c) #<generator object ...
# print(next(c)) #1... #it runs each time through every single number 1, then nextl 2, next, 3...
# for num in c:
#     print(num) #1-10 od razu, stop

def week():
    days= ["Mon","Tue","Wed","Thu","Fri","Sat","Sund"]
    for day in days:
        yield day

days = week()
# print(next(days)) #Mon
# print(next(days)) #Tue

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

gen = yes_or_no()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def current_beat():
#     max=100
#     nums=(1,2,3,4)
#     i=0
#     result=[] #drukuje [] -liste z tyloma 1, ile ustaliliśmy w max (100)
#     while len(result)<max:
#         if i>=len(nums): i = 0   ##jeśli i >= 4: i=0
#         result.append(nums[i])
#         # i +=1 #bez tego [1,1,1,1...], a z tym [1,2,3,4...1,2,3,4,,1,2....]
#     return result
# print(current_beat())
def currrent_beat():
    nums=(1,2,3,4)
    i=0 #zaczyna od 1[0], gdyby i=1, to od 2[1]
    while True:
        if i>=len(nums): i =0 #gdyby i=1, to po 1,2,3,4 byłoby 2; jeśli i wynosi już 4, albo więcej to zaczyanmy od i=0 znowu
        yield nums[i] #gdyby nums[2], to drukłoby 2,2,2,2,2, ale bez i+=1, to przy nums[i] druknęłoby same 1,1,1,1
        i+=1 #bez tego drukuje 1, po 1

a = currrent_beat()
# print(next(a)) #1
# print(next(a))  #2
# print(next(a))  #3
# print(next(a))  #4
# print(next(a))  #1

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
def make_song(count=99,beverage="soda"):
    for num in range(count,-1,-1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall"
        elif num == 1 :
            yield f"only {num} bottle of {beverage} left"
        else:
            yield f"No more {beverage}"
default_song=make_song()
# kombucha_song=make_song(5,"kombucha")
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(default_song))

def fib_list(max):
    nums=[]
    a,b=0,1
    while len(nums)<max: #to ustala, że w [] znajdzie się 9 liczb
        nums.append(b)
        a,b=b,a+b
    return nums
bb = fib_list(5)
# print(bb) #[1, 1, 2, 3, 5]

def fib_gen(max):
    x=0
    y=1
    count=0
    while count<max:
        x,y=y,x+y
        yield x
        count+=1
# for n in fib_gen(5):
#     # print(n)       #pion:1,1,2,3,5

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def get_mutiples(x=1,max=10):
    y=x
    while max>0:
        yield y
        max -=1
        y+=x
# default_multiples = get_mutiples()
# # evens= get_mutiples(2,3)
# print(list(default_multiples))
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))

def get_unlimited_multiples(x=1):
    y=x
    while True:
        yield y
        y += x


# sevens = get_unlimited_multiples(7)
# # sevens = [i for i in range(15)]
# print(next(sevens))
# print(next(sevens))

def nums():
    for num in range(1,10):
        yield num
g = nums()
# print(next(g)) #1
# print(next(g))  #2
# #at the end we get StopIteration Error
# gg=(num for num in range(1,10))
# print(next(gg))  #1
# ggg = [num for num in range(1,10)]
# print(ggg) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum([num for num in range(1,10)])) #45 #list comprehension
# print(sum(num for num in range(1,10))) #45 generator expression

import time
gen_start_time = time.time()
# print(sum(n for n in range(10000000)))
gen_stop = time.time() - gen_start_time

list_start_time = time.time()
# print(sum([n for n in range(10000000)]))
list_stop = time.time() - list_start_time

# print(f"sum(n for n in range(10000000) took {gen_stop}") #generator comprehension was faster
# print(f"sum([n for n in range(10000000)] took {list_stop}")

#POWTÓRZENIEEEEEEEEEEEEEEEEEEEEEEEEE
def week():
    days = ['Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for i in days:
        yield i
        # i += 1

days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            yield "no"
        elif answer == "no":
            yield "yes"

gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))