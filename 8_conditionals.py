
goal = input("What's yr name?")
print(f"You said {goal}")

print("Whats yout favourite color?")
data= input()
print("You said "+data)

# ---------------------- IF ELIF ELSE
# == equality (Im comparing sth)
print("Who're you?")
name = input()
if name ==  "Gabi Pa":
    print("gapself")
elif name == "Zu Pa":
    print("I love you")
else:
    print("pacman")

print("Are you funny?")
ans = input ()
if ans == "yes":
    print ("no, you're not")
elif ans == "no":
    print ("yes, you're")
elif ans == "dunno":
    print("shit happens")
else:
    print("no fucking answer")

#------------------------------------------------

animal = input("enter yr fav anim\n")

if animal:
    print(animal+" is my fav too")
else:
    print("you didnt say anything")

#COMPARISON OPERATORS---------------------------------------
age=18
age>=18
if age >= 18:
    print("you're and adult")

# LOGICAL OPERATORS-----------------------
a = 6
if a > 2 and a<8:
    print("YOU PAY CHILD PRICE!")

city = input ("Where do U live")
if city == "Los Angeles" or city == "San Francisco" or city == "BU":
    print("OH WOW")
else:
    print("NO WOW")

age=21
 # 2-8 2 dollar ticket
 # 65 5 dollar ticket
 # 10 dollars for everyone else

#if not ((age>=2 and age<= 8) or age>=65):
if False:
    print("you PAY 10 dollars")
else:
    print("you're a child or senior")

# IS VS. "==" not the same, but similar a=1 a==1 a is 1 ===>true
#a=[1,2,3] b=[1,2,3] a==b #true a is b #false  ---> c = b so b is c #true (cause we didnt have c before

x=13
y=13
if (x or y)== 14:
    print("YES")
else:
    print("OFC")

age = input ("How old are you? ")
if age:         #if age != "":           for if - previous if should be true, but for elif previous ifs must be true..
    age = int(age)   #if IF AGE is false then everything (if, elif, else) is false
    if int(age) >= 18 and int(age) <21: #without int => if age >= 18 and age <21:
        print("You can enter, but...")
    elif int(age) >= 25:
        print("You can drink")
    else:
        print("You cant come in, little one:9")
else:
    print("Please enter an age!")

ag = input ("How old? ")
if ag:
    ag = int(ag)
    if int(ag) >= 21:
        print("You can enter, but...")
    elif int(ag) >= 18:
        print("You can drink")
    else:
        print("You cant come in, little one:")
else:
    print("Please enter an age!")

if am_hungry:
    print("get food")
else:
    print("go learn python")
