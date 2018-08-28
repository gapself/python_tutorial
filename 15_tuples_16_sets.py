#TUPLE - ordered collection/items grouping IMMUTABLE-it cant be changed(cant update stored data)
#fasten than lists;makes code safer;valid keys in a dict;
siusiaks = ('small','medium','large')
print(siusiaks)
first_tuple = (1,2,3,3)
print(first_tuple[1])


locations = {
    (35.98, 43.90):"Tokyo",
    (40.90, 60.09):"NY"
}
print(locations[(35.98, 43.90)])
#locs = {[35,39]:'tokyo Office'} #(you cant use keys in a dic)
# print(locs)



                                #LOOPING
months = ('J','F','M','A')
for month in months:
    print(month) #J,F, M, A
print("PRZERWA")
i = len(months)-1       #A, M,F,J
while i>=0:
    print(months[i])
    i -= 1                 #3
x = (1,2,3,3,3)
print(x.count(3))

nums = (1,2,3,(4,5),6,7)
print(nums[3])
                               #SETS (dont have duplicate val/elements in sets arent ordered
s = set({1,2,3,4,5,5,5})
print(s)
print(4 in s) #True
print(9 in s) #F

numbers={1,2,3,4}
for number in numbers:
    print(number)

cities = ["LA","B","K"]
print(len(set(cities)))
                                                    #ADD
# print(list(set(cities.add("cizimizi"))))
# # print(cities.remove("LA"))
# print(cities.discard("LA"))

                                               #SET MATH
students = {"LA","BA","KA","KK"}
students2 = {"AA","BB","KK"}
print(students|students2)                 #union (dodaje do siebie sets, ale usuwa powtazrane)
print(students & students2)                #to,co się powatzras

########eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexerciseeeeeeeeee
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:
values = [10, 20, 30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 3 - Given the following variable
stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
print(unique_stuff) #{1,2,,3,5}

                                    #SET COMPREHENSIONS
b = {x**2 for x in range(10)}
print(b)

c = {x:x**2 for x in range(10)} #dict bo jest for X
print(c)

d = {x.upper() for x in "hello"} #
print(d)

e = len({x for x in "hello"}) #
print(e)

d = len({x for x in "hello"}) == 5  #FALSE
print(d)

string = "hellop"
x = len({x for x in string if x in "hellop"}) ==5  #TRUE
print(x)

m = {m for m in string if m in "hello"}
print(m)


                                #RECAP
                                #tuples're ordered coll of el, immutable
                                #tuples're faster than lists
                                #sets're unordered, immutable
                                #sets&tuples can be created {} and () or the set() or tuple()function
                                #dset comprehen is useful when converting other data types to a set
