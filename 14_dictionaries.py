# a = {"b":"blue","a":4.5,"iscute":True}
# print(a)
# print(a["b"]) #blue
#
# a2 = dict(n="Anna", a=4.5)
# print(a2)
# a3="iscute"
# print(a3)
# print(a[a3]) #True
#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
#
# full_name= artist["first"] +" " + artist["last"]
# print(full_name)
#
#                         #LOOPING THROUGH DICT #.VALUES #.KEYS #.ITEMS
# instructor = {
#     "name":"Colt",
#     "owns_dong":True,
#     "num_courses":4,
#     "fav_language":"Python",
#     "is_hilarious":False,
#     44:"my fav num"
# }
# # print(instructor.values()) #dict_value[]
# # # for value in instructor.values(): #Colt, True...
# # #     print(value)
# #
# # for c in instructor.keys(): #name, ows_dog... etc
# #     print(c)
# # print(instructor.items()) #dict_item([("name","Colt),()....])
# for k,v in instructor.items():
#     print(f"Key is {k} and value is {v}")

# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# print(donations)
# #moje rozwiązanie: (suma)
# for total_donations in donations.values():
#     total_donations = sum(donations.values())
# print(total_donations)
# #sugerowane: (print:dodawanie po kolei)
# total_donations = 0
# for donation in donations.values():
#     total_donations += donation
#     print(total_donations)
#
# instructor = {
#     "name":"Colt",
#     "owns_dong":True,
#     "num_courses":4,
#     "fav_language":"Python",
#     "is_hilarious":False,
#     44:"my fav num"}
# print("name" in instructor) #True
# print("phone" in instructor) #False
# print("name" in instructor.values()) #F
# print("name" in instructor.keys()) #True
#                                     #METHOOOOOOOOOOOOOOOOOOOOOOOOODS
#                                 #CLEAR
# instructor = {"name":"Colt","owns_dog":True,"num_courses":4,
#     "fav_language":"Python","is_hilarious":False,44:"my fav num"}
# print(instructor.clear())
#                                 #COPY
# d = dict(a=1, b=2,c=3)
# print(d)
# clone = d.copy()
# print(clone)
# print(clone==d) #T
# print(clone is d) #F
# #                                 #FROMKEYS
# new_user = {}.fromkeys(['name','score','email','profile bio'],'unknown')
# print(new_user)
# print(new_user.fromkeys(['phone'],'unknown'))
# print(new_user.fromkeys(range(1,10),'unknown'))
#                                 #GET - jak jest jakaś lista to potem
# instructor = {"name":"Colt","owns_dong":True,"num_courses":4,
#     "fav_language":"Python","is_hilarious":False,44:"my fav num"}
# print(instructor.get('name'))
# print(instructor.get('chuj'))
# chujek = instructor.get('japko')
# print(chujek is None)
#
# print("SZAKALAKALALAKA")
#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES
# # This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
#
# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {"almond croissant" : 12,"toffee cookie": 3,
#     "morning bun": 1,"chocolate chunk cookie": 9,"tea cake": 25}
# # CODE BELOW:
# #food = str(input("what"))
# if food in bakery_stock:
#     print("{}left".format(bakery_stock[food]))
# else:
#     print("We dont")
# #albo
# # print(str(input("what else")))
# quantity = bakery_stock.get(food)
# if quantity:
#     print("{}left".format(quantity))
# else:
#     print("we dont make that")
#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# #DO NOT TOUCH game_properties!
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"]
# # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
# initial_game_state = {}.fromkeys((game_properties),0)
# print(initial_game_state)
#
#                                     #POOOOP
# instructor = {"name":"Colt","owns_dog":True,"num_courses":4,
#     "fav_language":"Python","is_hilarious":False,44:"my fav num"}
# print(instructor.popitem())
# print(instructor.popitem())
# # print(instructor.popitem("name"))     =(1 given)
#                                   #POOOOP
# instructor = {"name":"Colt","owns_dog":True,"num_courses":4,
#     "fav_language":"Python"}
# person = {"city":"Antigua"}
# person.update(instructor)
# print(person)
# person['name'] = "Adam"
# print(person)
#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
# stock_list = inventory.copy()
# print(stock_list)
# # add the value 18 to stock_list under the key "cookie"
# stock_list['cookie']=18
# print(stock_list)
# # remove 'cake' from stock_list USE A DICTIONARY METHOD
# stock_list.pop('cake')
# print(stock_list)
#
# playlist = {
#     "title":"patagonia bus",
#     "author":"gabi",
#     "songs":[
#         {"name":"Pick Up", "author":["DJ Koze"],"duration":6.38},
#         {"name":"Mama", "author":["G-Eazy","Madison"],"duration":3.33}
#     ]
# }
# total_length = 0
# for song in playlist['songs']:
#     total_length += song["duration"]
# print(total_length)
#
# for song in playlist['songs']:
#     print(song["author"])
#                             #COMPREHENSIONSSSSSSSSSSSSSSSSSSSSSSS
# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]:str2[i] for i in range(0,len(str1))}
# print(combo)
#
# instructor = {'name':'Colt','city':'Wwa','color':'purple'}
# instructor1 = {k.upper():v.upper() for k,v in instructor.items()}
# print(instructor1)
#
# num_list=[1,2,3,4]
# num = {num:("even" if num%2 ==0 else "odd") for num in num_list}
# print(num)
# num2= {num:("even" if num%2 ==0 else "odd") for num in range (1,100)}
# print(num2)
#
# instructor = {'name':'Colt','city':'Wwa','color':'purple'}
# instructor2 = {(k.upper() if k is'color' else k):v.upper() for k,v in instructor.items()}
# print(instructor2)
#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE 15 ---------------------------
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]:list2[i] for i in range(0,len(list1))}
# print(answer)
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# # # use the person variable in your answer
# #moje rozwiązanie
# answer = dict(person)
# # using a dict comprehension:
# answer = {thing[0]:thing[1]for thing in person}
# #using dict comprehensions without any references to list indexes:
# answer = {k:v for k,v in person}
# print(answer)

# #EXERCEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# #myanswer
# answer={}.fromkeys(["a","e","i","o","u"],0)
# print(answer)
#dict comprehe
# answer={i:0 for i in "aeiou"}
# print(answer)
# #using
# answer=dict.fromkeys("aeiou",0)


#
# #EXERCISEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# # A = chr(65)
# # for i in range (65,90)
# #     print(i)
# # answer = answer.fromkeys(range(65,91),chr(65))
# # answer ={chr(65,90):k for k in range("A","Z")}
# # answer = {(chr(65),chr(90)):t for t in range(65,91)}
# # answer = {i for i in range (chr(65),chr(90)):k}
# #moje rozwiązanie
# answer={i:chr(i) for i in range(65,91)}
# print(answer)

# arr = ([3],[11,2 ,4],[4, 5 ,6],[10, 8 ,-12])
# #
# def s(ar):
#     primary_diagonal= ar[1][0]+ar[2][1]+ar[3][2]
#     secondary_diagonal=ar[1][2]+ar[2][1]+ar[3][0]
#     differenece=abs(primary_diagonal-secondary_diagonal)
#     return differenece
#
# arr = [[11,2 ,4],[4, 5 ,6],[10, 8 ,-12]]
# print(len(arr))
# def diagonalDifference(arr):
    # n=0
    # primary_diagonal=arr[0][n]+arr[1][n+1]+arr[2][n+2]
    # secondary_diagonal=arr[0][n+2]+arr[1][n+1]+arr[2][n]

#
#     result = diagonalDifference(arr)
#
# print(diagonalDifference(arr))
# n=input()
# for x in range(1,int(n)):
#     print("#"*x)
# n=input()
# liczba_kratek_w_linii=(int(n)+1)
# print(liczba_kratek_w_linii)
# for x in range(1,int(n)):
#     x += int(n)
#     print("#")

# x=1
# while x<4:
#     print("#"*x)
# def staircase():

# n=int(input())
# for x in range(1,n):
#     x=n-x
#     print(x*" "+(n-x)*"#")
# print("#"*n)

# arr = [1,2,3,4,5]
# def miniMaxSum(arr):
#     a = sum(arr)-max(arr)
#     b = sum(arr)-min(arr)
#     result = [a,b]
#     return ' '.join([str(x) for x in result])
#
# print(miniMaxSum(arr))

# arr = [1,2,3,4,5,6,9]
# arr= [256741038,623958417,467905213,714532089,938071625]
# arr = [int(x) for x in input().split()]
# def miniMaxSum(arr):
#     a = sum(arr)-max(arr)
#     b = sum(arr)-min(arr)
#     result = [a,b]
#     return ' '.join([str(x) for x in result])
#
# print(miniMaxSum(arr))


# ar_count = (input().strip())
# n = int((input()))
# ar=list(map(int, input().split()[:n]))
# ar = ' '.join([n for n in input().strip()])
# ar = [n for n in input().strip().split()]
# ar = input().strip()
# for a in ar:
#     a.strip().split()
#
# #
# #
# def birthdayCakeCandles(ar):
#     return ar.sum(max(ar))
# print(birthdayCakeCandles(ar))

# ar_count= int(input())
# ar=list(map(int,input().split()[:ar_count]))
# def birthdayCakeCandles(ar):
#     heighest_candle = int(max(ar))
#     num_of_same_nums = ar.count(heighest_candle)
#     return num_of_same_nums
#
# print(birthdayCakeCandles(ar))


# print(max(ar))
# print(sum(str(max(ar))))


# v= 2.45678910
# v = str(round(v,6))
# print(v)

# n=int(input())
# Array=list(map(int, input().split(‘ ‘)[:N]))
# arr = list(input().strip().split())
# for a in arr:
#     print(a)
# print(n)


# ZADANKO!!!!
# n = int(input())
# arr =list(map(int, input().split()[:n]))
# def plusMinus(arr):
#     positive_nums = len([i for i in arr if i > 0])/n
#     negative_nums =len([i for i in arr if i < 0])/n
#     zero_nums = len([i for i in arr if i == 0])/n
#     a = [positive_nums, negative_nums, zero_nums]
#     # # result = [format(i, '.6f') for i in a]
#     # for x in a:
#     #     x = format(x,'.6f')
#     #     # print(i)
#     # return x
#     # return format(i,'.6f')#['0.500000', '0.333333', '0.166667']
#     part_posi_nums_decimal = format(positive_nums,'.6f')
#     part_neg_nums_decimal = format(negative_nums,'.6f')
#     part_zero_nums_decimal = format(zero_nums,'.6f')
#
#     print(part_posi_nums_decimal)
#     print(part_neg_nums_decimal)
#     return part_zero_nums_decimal
#
#
# print(plusMinus(arr))

#ZADANKO!!!
# a = list(map(int, input().rstrip().split()))
# b = list(map(int, input().rstrip().split()))
# def compareTriplets(a, b):
#     a_points = b_points = 0
#     for i in range(3):
#         if a[i]>b[i]:
#             a_points += 1
#         elif a[i]<b[i]:
#             b_points += 1
#     result = [a_points,b_points]
#     return result
# print(compareTriplets(a,b))

# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))
# def diagonalDifference(arr):
#     primary = sum(arr[i][i] for i in range(n))
#     secondary = sum(arr[i][n-i-1] for i in range(n))
#     result = abs(primary-secondary)
#     return result
# print(diagonalDifference(arr))

# s = input()
# def timeConversion(s):
#     timeformat = s.split(":")
#     hours = timeformat[0]
#     mins = timeformat[1]
#     ss= timeformat[2] #45PM
#     if ss[-2:] == "PM" and hours == "12":
#         return f"12:{mins}:{ss[:-2]}"
#     elif ss[-2:] == "AM" and hours == "12":
#         return f"00:{mins}:{ss[:-2]}"
#     elif ss[-2:] == "AM":
#         return f"{hours}:{mins}:{ss[:-2]}"
#     else:
#         hours24 = str(int(hours) + 12)
#         return f"{hours24}:{mins}:{ss[:-2]}"

    # else:
        # return f"{hours}:{mins}:{ss[:-2]}"
# print(timeConversion(s))


# n = int(input())

# grades = []
#
# for _ in range(n):
#     grades_item = int(input())
#     grades.append(grades_item)
#
# def gradingStudents(grades):
#     for grade in grades:
#         # difference = grade - grade %5
#         # if grade %5 >=3 and grade >= 38:
#         #     result = difference+5
#         # elif (grade %5) < 3 and grade >= 38:
#         #     result = grade
#         # elif grade <38:
#         #     result = grade
#         # print(result)
#         if grade >= 38:
#             difference = grade - grade%5
#             if grade%5 >=3:
#                 difference+=5
#             elif grade%5 <3:
#                 return grade

# print(gradingStudents(grades))



# s = [0,1,2]
# for i in s:
#     m = 2
#     # sum = 0
#     # sum = s[x]+sum
#     print(sum(s[i:]))


# n = int(input().strip())
#
# s = list(map(int, input().rstrip().split()))
#
# dm = input().rstrip().split()
#
# d = int(dm[0])
#
# m = int(dm[1])

# def birthday(s, d, m):
#     count = 0
#     for i in s:
#         if sum(s[i:m+i]) == d:
#             count += 1
#     return count
# print(birthday(s,d,m))

# s=[1,2,3]
# for ss in s:
#     print(s[s:s+m])


# year=int(input())
# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
# print(is_leap(year))

# n = int(input())
# for x in range(n):
#     x += 1
#     print(x,end='a')

# s = list(input()) #abraka
# posichar =input().split() #0 #a
# posi,char=int(posichar[0]),str(posichar[1])
# def mutate_string(s, posi, char):
#     # #1st version
#     # s[posi]= char
#     # return "".join(s)
#     #shorter way:
#     return s[posi + 1:]
# # s[:posi] s[:0] []
# # s[posi:] s[0:] ['a', 'b', 'r', 'a', 'k', 'a']
# #s[1:] posi=0  ==>s[posi + 1:]    [b,r,a,k,a]
# # s[1+1:] ['r','a','k',a]
#
# print(mutate_string(s, posi,char))

# N = int(input())
# student_marks = {}
# for namelines in range(N):
#     # line = input().split()
#     # name, scores = line[0], line[1:]
#     # scores = map(float, scores)
#     name,*lines = input().split()
#     scores = list(map(float,lines))
#     student_marks[name]=scores
# query_name=input()
# query_score=student_marks[query_name]
# for key, value in student_marks.items() :
    # if key==query_name: print ("{0:.2f}".format(sum(value)/len(value)))

# if __name__ == '__main__':
#     n = int(input())    #num of elements in tuple
#     integer_list = map(int, input().split()) #elements separated
#     t = tuple(integer_list)
#     print(hash(t))


# python_students = [[input(),float(input())] for x in range(int(input()))]
# # sorted(python_students) #sortuje po nazwie, a nie najwiekszych wynikach
# # max(python_students)
#
# second_lowest = sorted(list(set([marks for [name, marks] in python_students])))[1]
# # print(second_highest) #20,30 dla 2 wrzuconych przez mnie
#
# # 5
# # m
# # 30
# # f
# # 40
# # g
# # 80
# # r
# # 100
# # p
# # 100
# # [30.0, 40.0, 80.0, 100.0]
# # z [1], to będzie 40
#
# # tu określamy imię 40, czyli f
# print('\n'.join([name for name,marks in sorted(python_students) if marks == second_lowest]))


# string, substring = (input().strip(), input().strip())
# print(len(string),len(substring))
# def count_substring(string, substring):
#     # return sum([1 for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring])
#
# # print(string[0:3])
# print(count_substring(string,substring))



# abcdcdcd
# cdc
# 8 3
# 2

# s = "HackerRank.com presents "'"Pythonist 2"'"."
# def swap_case(s):
#     return s.swapcase()
# print(swap_case(s))

# s = "qA2"
#
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())


#     elif char.isupper():
#         print(True)
#     elif char.isdigit():
#         print(True)
#     elif char.islower():
#         print(True)
#     elif char.isupper():
#         print(True)
#     return False
# print(s.isalpha() for)


# s= input().split()
# def solve(s):
#     return s[0][0].upper()+s[0][1:]+" "+s[1][0].upper()+s[1][1:]
# print(solve(s))


# name_surname = input().split(' ')
# print(' '.join(string.capitalize() for string in name_surname))
#
# s=input().split()
# def solve(s):
#     for word in s:
#         return ' '.join(word.capitalize())
# print(solve(s))

# U MNIE DZIAŁA iks de
# s=input().split()
# n, sur= s[0],s[1]
# def solve(s):
#     return n[0].upper() + n[1::1] + " "+ sur[0].upper()+sur[1::1]
# print(solve(s))

# n, k = input(), input()
#
# bill = list(input().split())
# k=bill[inxex]
# n=len(bill)
# print(k)

# nk= list(map(int, input().split()))
# n,k=nk[0],nk[1]
# bill = list(map(int, input().split()))
# b = int(input().strip())
# def bonAppetit(bill, k, b):
#     b_actual= (sum(bill)-bill[k])//2
#     if b_actual==b:
#         return "Bon Appetit"
#     elif b_actual!=b:
#         return b-b_actual
# print(bonAppetit(bill, k, b))



# s, max_w= input(), int(input())
# # def wrap(s,max_w):
# #     for x in s:
# #         x = int(s//max_w)
# #         print(x)
# if len(s)//max_w == 0:
#     print("litery w sekcji max_w")
# elif len(s)//max_w !=0:
#     print("litery w seksji, a ostaynia linijke z resztą len(s)%max_w")
# # print(wrap(s,max_w))
# print(len(s))
# # print(len(s)%max_w)


