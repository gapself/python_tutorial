def square(num):
    return num*num
print(square(9))    #81
#---------------------------------------
def square(num): return num*num

square2 = lambda num: num*num       #lambda as a variable
add = lambda a,b: a+b
# print(square(9))
# print(square2(3))
# print(add(3,10))
print(square.__name__)
print(square2.__name__)
print(add.__name__)
#-------------------------
#you can use lmbda instead of any function like say_hello
#lambda is nameless function and then --> print("sth")
                                                #MAAAAAAAAAAAAP
# function, która akceptuje 2 argumenty: funckję i ITERABLE,
#iterable - list, strings,dict,sets,tuples
#runs lambda for each value in the iterable and returns a map object
people = ["Aga", "Beci", "Cycek"]
peeps = map (lambda name: name.upper(),people)
print(list(peeps))
#--------------------------
el=[1,2,3,4]
doubles = list(map(lambda x: x*2,el))
print(doubles) #[2,4,6,8]
#-------------------------------
names = [
    {'first':'Rusty','last':'Steele'},
    {'first':'Colt','last':'Steele'}
]
first_names = list(map(lambda x: x['first'],names))
print(first_names)
#------------------------------
nums = [2,4,6,8,10]
doubles = list(map(lambda x: x*2,nums))
print(doubles)  #[4,8,12,16,20]
#---------------- EXCEEEEEEEEEEEER-----------
names = [1,2,3,4]
decrement_list = (map(lambda x: x-1, names))
print(list(decrement_list))
#to powinno wyglądać tak: bo map nie jest callable:
def decrement_list(l):
    return list(map(lambda n: n-1, l))
print(decrement_list([1,2,3,4]))
                                    #FILTEEEEEEEER
#returns filter object
#the obcject conatins the values that return true to the lammbda
l=[1,2,3,4]
evens = list(filter(lambda x: x%2==0,l))
print(evens)
#----------------------
names = ["austin","penny","anth",'angel','billy']
a_names=filter(lambda n: n[0]=='a',names)
print(list(a_names)) #['austin', 'anth', 'angel']
#--------------------
users = [
    {"username":"gabi", "tweets":['I love cake']},
    {"username":"kazik", "tweets":[]}
]
inactive_users = list(filter(lambda u: len(u['tweets'])==0,users))
#inactive_users = list(filter(lambda u: u['tweets'],users))     it prints users who are active
#inactive_users = list(filter(lambda u: not ['tweets'],users))  thats why I negate with"not"
print(inactive_users)
#-------------------                            #MAP and FILTEEEEEER
names = ["Lassie",'Colt','Rusty']
koko = list(map(lambda name: f"Your instr is {name}",
    filter(lambda value: len(value) <5, names)))
print(koko)
#-----------------
usernames = list(map(lambda user: user['username'].upper(),
    filter(lambda u: not u['tweets'],users)))
print(usernames)

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#sama
def remove_negatives(l):
    #return list(map(lambda u: u<0,l)) #[True, False, False, True]
    return list(filter(lambda u: not u<0, l))
print(remove_negatives([-1,3,4,-99]))

                                            #BUILT-IN FUNCTION

                                                    #ALL
print('blablablabla')
#return True if all el of the iterable are truthy(or empty)
l = all([char for char in 'eio' if char in 'aeiou']) #True, withou all() its #['e','i','o']
print(l)
b = [num for num in [4,2,10,6,8,9] if num%2==0] #[4, 2, 10, 6, 8]
# bb = all([num for num in [4,2,10,6,8,9] if num%2==0]) #True
print(b)
# print(bb)
people = ['charlie','casey','cody','gabi']
c=[name[0]=='c' for name in people]
print(c) #[True, True, True, False]
#------
nums = [2,60,26,18]
c = all([num %2==0 for num in nums]) #true
print(c)
#------
nums = [2,60,26,18,21]
c = all([num %2==0 for num in nums]) #false
print(c)
#------
for person in people:
    if person[0] != 'g':
        print(person)
#------                                             GENERATOR OBJECT
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#moje rozw: z GENERATOR EXPRESSION
def is_all_strings(list):
    # return all([iter for iter in list if iter == str(iter)]) #['a','b'] drukuje tylko str (bez all czyli określenia True/False) z all #True wszędzie, gdzie jest str
    return all([type(iter) == str for iter in list]) #tutaj działa też (iter == str(iter)...)
print(is_all_strings(['a','b',2,])) #False
print(is_all_strings(['a','b']))    #True
#LIST COMPREHENSION:
def is_all_strings(lst):
    return all([type(l) == str for l in lst])
#-----------                                          SORTED (!=SORT)
# returns new sorted list from the items in iterable
                                                    #MIN & MAX
print((max('a','d','c'), min("b","d","f"))) #tuple
print(max("Hello Gabi"))
print(max(1,100,400,3093892838))
print(max((3,5,60))) #tuple
names = ["A","Samson","Tomek","Abrakadabra"]
print(max(len(names) for name in names)) #4
print(max(names, key = lambda n: len(n))) #Abrakadabra
#---
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]
print(min(songs, key=lambda s: s['playcount'])) #{'title': 'happy birthday', 'playcount': 1}
#if I wanna find only a title of the most often played song:
print(max(songs, key=lambda s: s['playcount'])['title'])
#-------
#long version with FOR LOOP
max = 0
for song in songs:
    if song['playcount'] > max:
        max = song['playcount']
print(max) #99
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#zrobiłam sama, jest tak też w rozwiązaniu, ale nie wiem czemu MAX(li) nie można użyć
# def extremes(li):
#     return(min(li), max(li))
# print(extremes([1,2,3,4,5]))
#extremes([1,2,3,4,5]) #(1,5) return TUPLE!!

                                                    # REVERSED
a = "hello"[::-1] #olleh
print(a)
print(list(reversed("hello"))) #['o', 'l', 'l', 'e', 'h']
print(reversed("hello")) #<reversed object at 0x000001FFD42CFFD0>

for x in reversed(range(0,4)): #pionowo druk pojedynczych cyfr 4->0
    print(x)

                                                    #LEN
print(len(range(0,10))) #10
print(len({'s':10, "10":'as'})) #2
print('hello'.__len__())    #5
                                                    #ABS
#return the absolute no of
print(abs(-23)) #23
print(abs(-3.44444))
print(abs(float('20'))) #20.0
                                                    #SUM
#form lef to right
print(sum([1,2,3])) #6
print(sum([1,2,3],-6)) #0
                                                    #ROUND
#rounded to ndigits precision
print(round(3.56487)) #4
print(round(3.56487,3)) #3,565

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#hint use max & abs: poprawne, ale znowu problem z MAX
def max_magnitude(l):
    return max(abs(el) for el in l)
print(max_magnitude([300,20,-900]))
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#moja pierwsza odpowiedź: z list comprehension:
def sum_even_values(l):
    return sum([el for el in l if el %2 == 0])
print(sum_even_values([1,2,3,4,5,6]))   #12
print(sum_even_values([2,5,6])) #8
#-----2------
#MUSZĘ WYKORZYSTA ARG!!!! zeby nie używać listy, bo print(s_e_v(ma jeden argument, a nie sto))
def sum_even_values(*args):
    return sum(el for el in args if el %2 == 0)
print(sum_even_values(1,2,3,4,5,6))     #12

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
def sum_floats(*args):
    # for el in args:
    #     if el == float(el):
    #         return sum(args)
    #     else:
    #         return 0
    return sum(el for el in args if type(el) == float) #dając coś takiego : (iter == str(iter)...), druk inf: że nie przekonwertuje mi 'awesome' na float
print(sum_floats(1.5, 2.4, 'awesome', [], 1))
                                                    #ZIP
#
first_zip = zip([1,2,3],[4,5,6])
# print(list(first_zip))  #[(1, 4), (2, 5), (3, 6)]
print(dict(first_zip)) #{1: 4, 2: 5, 3: 6}
#---
nums1=[1,2,3,4,5]
nums2=[6,7,8,9,10]
words = ['hi','b','c']
z = zip(nums2,nums1,words)  #[(6, 1, 'hi'), (7, 2, 'b'), (8, 3, 'c')]
print(list(z)) #[(6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]
#---
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']
# final_grades = {"dan":98,'ang':91,'kate':78}
# final_grades = [min(pair) for pair in zip(midterms, finals)] #duk [98,91,78]
# final_grades = {t[0]: min(t[1],t[2]) for t[2] in zip(students, midterms, finals)} #duk [98,91,78]
# print(final_grades)
grades = dict(
    zip(
        students,
        map(
            lambda t:min(t),
            zip(midterms,finals)
        )   )
)
print(dict(grades)) #{'dan': 80, 'ang': 89, 'kate': 53}
#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def interleave(one,two):
    # return str(list(zip(one,two))) #[('h', 'n'), ('i', 'o')]
    #return str(list(''.join(t) for t in zip(one, two))) ['hn', 'io']
    return "".join(''.join(t) for t in zip(one,two))       #hnio
print(interleave('hi','no'))

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def triple_and_filter(l):
    return list(filter(lambda x: x%4==0,map(lambda x: x*3,l)))
print(triple_and_filter([1,2,3,4]))     #[12]
# #EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def extract_full_name(l):
    names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
    return list(map(lambda x:'{}{}'.format(val['first]'],val['last']),l))
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']






