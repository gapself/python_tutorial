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

# my solution!!
def sum_pairs(a,num):
    for i in a: #(for loop dla każdego x)"
        li= a[:i:]
        for s in li:
            if i+s == num:
                return [i,s]
        return []
print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []

# my similar solution from hackerrank.com
def sum_pairs(a,num):
    for i in range(len(a) - 1):
        # print(i) 0,1,2,3,
        for x in range(1 + i, len(a)):
            # print(x) i=0#x=1234 1#234 2#34 3#4
            if (a[i] + a[x]) == num:
                return [a[i], a[x]]
            return []

print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []
