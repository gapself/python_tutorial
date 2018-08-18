#-------------===================VARIAAAAABLES=========================================------------

print(1 / 3)  # division returns float, even when dividing two ints
# variables assignment
x = 100
m_of_d = 1
print(x + 1)

num_of_cats = 99
print(num_of_cats)
print(num_of_cats * 2)

# assigned to to other variables
python_is_awesome = 100
just_another_var = python_is_awesome  # reassigned at any time
python_is_awesome = 1337
all, at, once = 5, 10, 15
print(python_is_awesome)

num_of_dog = 99
num_of_dog = num_of_dog - 1
print(num_of_dog)

friends = 0
friends = num_of_dog - 1
print(friends)
catsblahblah = 1
print(catsblahblah)

some_string = "8"
type(some_string)
another_string = "HEllo"
type(another_string)
print(type)

name = "Dusty"
child = "Pamela"
print(name, child)

name= 'Colt'
name2="Colt"
print(name)
print(name2)

message = "he said 'hello there'"
print(message)
msg2= 'I am "funny"'
print(msg2)
print (type(msg2))

x = "city"
y = True
x=y
print(type(x))

#SEQUENCES -------------------------------------
new_line = "hi\nhello"
print(new_line)

str="hel\blo"
print(str)

#-------------------------EXCERCISE----------
# Set the message variable equal to any string containing a new-line escape sequence
message = "message\n"
print(message)

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\" #"/\/\/\ "can i do this????
print(mountains)
# Set the quotation variable to any string that contains an escaped double quotation mark

quotation = "\"quotation\""
print(quotation)

#STRING CONCATE---------------------------------------------

x= "8" + "cat"
print (x)

name = "colt"
# name = name + "steele"
name += "steele"
print(name)
people=100
people -= 10
print (people)

#FORMATTING STRINGS --------------------------
x=10
formatted = f"I've told you {x} times already!"
print (formatted)
fruit= "banana"
ripeness= "unripe"

#print(f"The {fruit} is {ripeness}")
print("The {} is {}".format(fruit, ripeness))

#-----------------------------------------------------
x = "lol"[0]
print (x)
name= "Chuck"
print(name[1])

#CONVERT DATA TYPES ------------------------------------
decimal = 12.57899
integer = int(decimal) #12
print(integer)
num=12
print (type (num))
num = float(num)
print(type(num))
print(num)

#KM -> Miles CONVERTER---------------
print("How many kms did you make last time?")
kms = float(input())
miles = kms/1.60934
#miles= float(kms/1...)
# miles = round(miles,2)
print(f"That is {kms} kms equals to {round(miles,2)} miles")

#round (thing to round, how many decimal points)





