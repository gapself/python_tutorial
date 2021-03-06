# reverse string!
def reverse_string(string):
    return string[::-1]

print(reverse_string("awesome"))

# list check
def list_check(a):
    return all(type(x) == list for x in a)
print(list_check([[],[1],[2,3], (1,2)])) #False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True

# remove_every_other
def remove_every_other(list):
    if len(list)>1:
        return list[0::2]
    return list

print(remove_every_other([1,2,3,4,5])) # [1,3,5]
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1]
print(remove_every_other([1,2,3,4,5,8,9,0])) # [1,3,5,9]

# sum_pairs
# ar[i]+ar[j]//k
# ar[0]+ar[1]==6

# my solution!! #błąd, np ([4,5,6],8) =>używa [4,4] tych samych cyfr ..
def sum_pairs(a,num):
    for i in a: #(for loop dla każdego x)"
        for s in a[:i:]:
            if i+s == num:
                return [i,s]
    return []

print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([4, 2, 10, 5, 1], 8))  # []
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []
print(sum_pairs([3, 4, 5, 2, 3, 1, 7, 3, 4, 5], 9))
print(sum_pairs([3, 4, 5, 2, 3, 1, 7, 3, 4, 5, 10, 20, 30, 12], 12))

# # my similar solution from hackerrank.com
def sum_pairs(a,num):
    for i in range(len(a) - 1):
        # print(i) 0,1,2,3,
        for x in range(1 + i, len(a)):
            # print(x) i=0#x=1234 1#234 2#34 3#4
            if (a[i] + a[x]) == num:
                return [a[i], a[x]]
    return []
print(sum_pairs([4, 2, 10, 5, 1], 8))  # [4,2]

# solution
def sum_pairs(ints, s):
     already_visited = set()
     for i in ints:
         difference = s - i
         if difference in already_visited:
             return [difference, i]
         already_visited.add(i)
     return []

# VOWEL_COUNT
def vowel_count(string):
    return {x:string.lower().count(x) for x in string if x in "aeiou"}

print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1})
print(vowel_count('Elie'))   # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}

# TITLEIZE
def titleize(string):
    return " ".join(word[0].upper() + word[1:] for word in string.split())
    return string.split()
print(titleize('this is awesome')) # "This Is Awesome"

# FIND FACTORS
def find_factors(num):
    return [nums for nums in range(1,num+1) if num %nums ==0]

print(find_factors(10)) # [1,2,5,10 ]
print(find_factors(11)) # [1,11]
print(find_factors(111)) # [1,3,37,111 ]

# REPEAT
def repeat(str,num):
    if (num == 0):
        return ''
    i=0
    newstr=''
    while (i<num):
        newstr += str
        i += 1
    return newstr
print(repeat('*', 3))  # '***'
print(repeat('abc', 2))  # 'abcabc'
print(repeat('abc', 0))  # ''


# two list dictionary
'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''
def two_list_dictionary(keys,values):
    # solution = {keys[i]:values[i] for i in range(0,len(keys))} #to działa jedynie wtedy, kiedy len(keys)=len(values), else: out of range ;)
    solution={}
    for index, letter in enumerate(keys):
        # return index,letter #(0, 'a')
        if index < len(values):
            solution[keys[index]] = values[index] #dict[keys[index]]=dict[keys[0]]=dict["a"] = values[index] = values[0] = 1
        else:
            solution[keys[index]] = None
    return solution

print(two_list_dictionary(['a', 'b', 'c','d'], [1, 2, 3]))


#range in list
'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''
def range_in_list(list,start=0,end=None):
    # return sum(x for x in range(list[start], list[end+1])) #jedynie dla list,start,end
    end = end or len(list) # same as list[-1]
    return sum(list[start:end+1])

print(range_in_list([1,2,3,4],0,2))
print(range_in_list([1,2,3,4]))

# same frequency
# not sure of it:
# def same_frequency(num1,num2):
#     if len(str(num1))==len(str(num2)):
#         return True
#     else:
#         return False
def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
    return d1,d2

print(same_frequency(551122,221515)) #t
print(same_frequency(321142,3212215))   #f
print(same_frequency(1212, 2211))   #t

#answer
def two_list_dictionary(keys, values):
    collection = {}

    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None

    return collection

#NTH
def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]    #dla idx=(-8), arr[-4]

# moje:
#   return lis[num]

print(nth(['a', 'b', 'c', 'd'], 1))  # 'b'
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'

#FIND THE DUPLCATE
def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)
#moje rozw:
def find_the_duplicate(list):
    d = {x:list.count(x) for x in list}
    for key,value in d.items():
        if value >=2:
            return key

print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None

#SUM UP DIAGONALS
def sum_up_diagonals(arr):
    total = 0
    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total

#min_max_key_in_dictionary
def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]
# return [min(d.keys()),max(d)]

#two oldest
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]


# odd string
def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0 #ord('a')=97 Unicode position of the letter!
    return total % 2 == 1

print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False


def find_greater_numbers(lis):
    total=0
    i=0
    j=1
    while i<len(lis):
        while j<len(lis):
            if lis[j]>lis[i]:
                total +=1
            j+=1
        j=i+1
        i+=1
    return total

print(find_greater_numbers([1,2,3])) # 3
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[]) #!!!!!!!!!!!!!!default
list3 = extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

def valid_parentheses(string):
    total=0
    i=0
    while i <len(string):
        if string[i]=='(':
            total+=1
        if string[i]==')':
            total-=1
        if total<0:
            return False
        i+=1
    return total==0


print(valid_parentheses(")(()))"))  # False
print(valid_parentheses("(())((()())())")) # True


#TRIANGLE
n=4
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end='+')
    k-=1
    for j in range(0,i+1):
        print('G',end='=')
    print("\r")

#RECTANGLE
for i in range(n-1,0,-1):
    # k=n-i
    print('*' * i + '=')

#counting num of decimals
n=1
res=0
while n>0:
    n/=10
    res+=1
    print(res,n)

#fibonacci
a=0
b=1
while a <= b:
    print(a)
    c=a+b
    a=b
    b=c
    if a==8:
        break

# binary gap
def binary_gap(N):
    return len(max(bin(N)[2:].strip('0').split('1')))
print(binary_gap(5))

# cyclic rotation
n = int(input())
A= list(map(int, input().rstrip().split()))
k= int(input())
i=1
while k>=i:
    A.insert(0,A[n-1])
    A.pop()
    print(A)
    i+=1
