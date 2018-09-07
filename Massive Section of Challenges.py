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

