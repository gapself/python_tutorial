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
    # return " ".join(word[0].upper() + word[1:] for word in string.split())
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
    for index, letter in enumerate(keys): #The optional argument allows us to tell enumerate from where to start the index. (keys,0)
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
'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
# not sure of it:
def same_frequency(num1,num2):
    if len(str(num1))==len(str(num2)):
        return True
    else:
        return False

print(same_frequency(551122,221515))
print(same_frequency(321142,3212215))
print(same_frequency(1212, 2211))
