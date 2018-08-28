#LIST - collection of other data
from typing import List, Union

first_task = "Install Python"
second_task = "L Python"
third_task = "Take a break"


tasks = ["food", float(8), "Take a break"] #jeśli jest polecenie zawarcia liczby FLOAT, to po prostu mogę wpisać: 8.5
print (type("food"))
#tasks = [first_task, second_task, third_task]
len(tasks)
print(len(tasks))
print(tasks)

t = list(range(1,4))
print(t)
print(len(t))

colors = ["purple", "pink", "blue"]
the_best = colors [0]
print(the_best)
x=10
y=x
print(x)
print(colors)
print(colors[2])
print(colors[-2])

print("purple" in colors) #True
print("green" in colors) #False

if "pink" in colors:
    print("YOU'RE GENIUS")

numbers = [1,2,3,4]
for number in numbers:
    print(number)
#print(quit())
for x in range(1,5):
    print(x)
no = [4,6,2,7]
for nos in no:
    print(nos)

#all values in a list
numberss = [1,2,3,4]
i=0
while i < len(numberss):
    print(numberss[i])
    i +=1

colorss = ["purple","pink","orange","green","blue"]
index = 0
while index < len(colorss):
    print(f"{index}: {colorss[index]}")
#     print(colorss[index])
    index +=1
"0 color: purple"
"1 color: teal"
# for color in colorss:
#     print(color)
#-----------1 wersja zadania===========
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s.upper()
#     print(result)
#============2 wersja zadania===========
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s        #SSSSSSSSSSSSS nie 1 (str)
result = result.upper()
print(result)

#UPPERCASE - duże litery!!

data=[1,2,3]
print(data)
######################## 3 METHODS- APPEND (1), EXTEND(few), INSERT(,)
first_list= [1,2,3,4]
first_list.append(5)    #dodaje na koniec liczbę
print(first_list)

nums = [1,2,3]
print(len(nums))
nums.append([4,5])                 #NUMS APPEND - if I wanna add 1 thing into the list
len(nums)
print(len(nums))
print(nums)
nums.extend([4,5])                  #NUMS EXTEEEEEEEEEEEEEEEEEEEEEEEEND - MORE than 1
print(nums)

sec_list = [1,2,3,4]
sec_list.insert(2, "Hi")          #ZA 2 wstawia Hi
print(sec_list)
sec_list.insert(-1,"The end")
print(sec_list)
sec_list.insert(len(nums),"LAST")
print(sec_list)
sec_list.append("The endend")
print(sec_list)

instructors = []
instructors.extend(["Colt","Blue","Lisa"])
print(instructors)

                                #CLEAR
third_list =[1,2,3]
third_list.clear()
print(third_list)
                                #POP
first_list=[1,2,3,4]
first_list.pop(2)                   #usuwa i=2 (Czyli3) z listy
print(first_list)

items= ["dupa","pipka","siusiak"]
item=items.pop()                    #usuwa ostanią i = "siusiak"
print(items)
items.pop(0)
print(items)
first = items.pop(0)
print(first)
                                #REMOVE
lis=["a","b","c"]
lis.remove("c")
print(lis)
                                #INDEX.
numbers = [4,4,5,5,6,8,8,8,9]
print(numbers.index(5))
print(numbers.index(5,1))       #find the index of 5 after index of 1 (its sth like start point)
print(numbers.index(5,3))
print(numbers.index(8,6,8))
print("ODDZIELENIE")            #COUNT
l = ["a","b","c","d","e","f","a"]
print(l.index("a"))
print(l.index("a",6))
print(l.count("a"))
print(l.count("g"))
#                                 #REVERSE
li = [1,2,4,5]
li.reverse()
print(li)
#                                 #SORT
a = [6,7,4,1,2,3]
a.sort()
print(a)
b = ["a","b",'c','d','e','f','k','a']
b.sort()
print(b)
                                #JOIN
m=['coding','abs','xyz']
m = ",parówka,".join(m)
print(m)

w=['coding','abs','xyz']
w= ",LOL: ".join(w)
print(w)

instructorr =[]
instructorr.extend(["Colt","Blue","Lisa"])
print(instructorr)
instructorr.pop()
print(instructorr)
instructorr.remove("Colt") #/instructorr.pop(0)
print(instructorr)
instructorr.insert(0,"Done")
print(instructorr)

                                #SLICES = make new lists using slices of the old list!

# some_list[start:end:step]

fi = [1,2,3,4]
print(fi[::-1])
print(fi[-2:])

f=["yellow","red","orange"]
print(f[1:])           #red, orange
f2 = f[0:]              #yel, red, orange
print(f2)
print(f==f2)
print(f2 is f)
print(f[:2])    #yel, red
print(f[0:1])   #reference(0,1) wydruknie 0 #yellow
print(f[:-1])   #yell, red

l = ['P','y','t','h','o','n']
print(l[1:-3:])

k = [1,2,3,4]

print(k[:1:-2])
print(k[:2:-2])
print(k[1:])
print(k[:3])
print(k[::2])
print(k[1::-1])
print(k[:1:-1])     #starts from 1 and go -1
print(k[2::-1])
print(k[::-1])
print(k[::-2])
print(k[-2:])
print(k[:-2])
print(k[1:3])           #druknie 2,3(bo dla i=1 i=2
string = "this is fun!"
print(string[::-1])
print(k[-2])
                        #SWAPPING VALUEEEEEEEES- SHUFFLING/SORTING/ALGORITHMS
names = ["j","m"]
names [0], names[1] = names[1], names[0]
print(names)

