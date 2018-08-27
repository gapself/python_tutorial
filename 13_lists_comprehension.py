n = [1,2,3]
# [x*10 for x in nums]
print(n)

numbers = [1,2,3,4,5]
doubled_numbers=[]

for num in numbers:
    doubled_number = num*2
    doubled_numbers.append(doubled_number)
print(doubled_numbers)

num = [1,2,3,4,5]
doubled_num = [n*2 for n in num]
print(doubled_num)



name= 'colt'
[nam.upper() for nam in name]    #['C','O','L','T']
friends = ['ashley','matt','michael']
[friend[0].upper() for friend in friends] # ['Ashley','Matt','Michael']
[num*10 for num in range(1,6)] #10,20,30,40,50]]
[bool(val) for val in [0,[],'']] #[False,false,false]

print(bool(""))
print(bool("xyz"))
print(bool(0)) #wszystkie liczby True poza 0

n = [1,2,3,4,5]
string_list = [str(nu) for nu in n]
print(string_list)

colors = ["green", "blue","pink"]
# [color.upper() for color in colors] #GREEN,....
list = [1,2,3]
# [str(l) for l in list] #[1,2,'3']
# [str(l)+"HELLO" for l in list] #'1HELLO,'2HELLO....

#===============                   #LC with CONDITIONAL LOGIC!!!
m = [1,2,3,4,5,6]
evens = [mi for mi in m if mi % 2==0]
print(evens)
odds = [mi for mi in m if mi % 2 != 0]
print(odds)
# [mi*2 if m % 2 == 0 else mi/2 for mi in numbers] #0,5 ; 4 ; 1,5 ; 8....

with_vowels = "This is so much fun!"
ii= ''.join(w for w in with_vowels if w not in "aeiou")
print(ii)
ia = '...'.join(["join", "dude"])
print(ia)
ib = ''.join(w for w in with_vowels if w not in "aeiou")
print(ib)

#EXCERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# Using list comprehensions:
#
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
print(answer) #['E', 'T', 'M']

# answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
# Using good old manual loops:
#
# answer = []
# for person in ["Elie", "Tim", "Matt"]:
#     answer.append(person[0])
# answer2 = []
# for num in [1,2,3,4,5,6]:
#     if num % 2 == 0:
#         answer2.append(num)

#EXCERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# Using
# list
# comprehensions(the
# more
# Pythonic
# way):
#
answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer) #[3, 4]
# # # the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(answer2) #['eile', 'mit', 'ttam']
# Without
# list
# comprehensions, things
# are
# a
# bit
# longer:
answer = []
for x in [1, 2, 3, 4]:
    if x in [3, 4, 5, 6]:
        answer.append(x)
print('HALLO')
# answer2 = []
# for name in ["Elie", "Tim", "Matt"]:
#     answer2.append(name[::-1].lower())

#EXCEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
for numbers in range (1,101):
    if numbers % 12 ==0 or numbers == 100:
        print(numbers)
answer = [num for num in range(1,101) if num %12 ==0]
print(answer)

answers = [w for w in "amazing" if w not in 'aeiou']
print(answers) #m,z,n,g

#coś tu nie tak???
a = "amazing"
l = ''.join(w for w in a if w not in "aeiou")
print(a)
                                            #NESTED LISTS = complex data sttuctures / game boards /mazes/rows columns for visualizations,tabulation, grouping data
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0][1]) #2
print(nested_list[1][-1]) #6
print(nested_list[2][1]) #8
print(nested_list[-1][-2]) #8
print("PRZERWAWAWAWAWA")
for l in nested_list:           #l - loop, first loop starts over and then it takes values from the second loop and third
    for val in l:
        print(val)
#[[print(val) for val in 1]  for l in nested_list]

coords = [[10.423,913.234],[78.293,-14.092],[21.980,32.098]]
for loc in coords:
    #print(loc) #3 lists
    for coord in loc:
        print(coord) #values without lists
board = [[num for num in range(1,4)]for val in range(1,5)]
print(board) #drukuje (1,5)list z (1,4)ilością liczb
x = [["X" if num%2!=0 else "O" for num in range(1,4)]for val in range(1,4)]
print(x)
y = ["*" for i in range(5,8)]
print(y)
o = [["*" for y in range[1,2,3]] for val in range(1,4)]
print(o)

#EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
ans = [[num for num in range(0,3)]for val in range(1,4)]
print(ans)

a = [[num for num in range(0,10)]for num in range(0,10)]
print(a)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

                                            #RECAP


