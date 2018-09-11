                                #OBJECTIVES, INHERITANCE
#A key feature(kluczowa cecha) of OOP is the ability to define a class which inherits(dziedziczy) from another clsss("base"/"parent" class)
#
class Animal:
    cool = True
    def make_sound(self,sound):
        print(f"This animal says {sound}")
class Cat(Animal):
    pass
a = Animal()
# print(a.make_sound("CHIRP"))
b = Cat()
# print(b.make_sound("MEOW"))
# print(b.cool)   #True
# print(Cat.cool) #true
# print(isinstance(b,Animal)) #True
# print(isinstance(b,object)) #True
#it ilustrates us that b is instancde of Cat and at the same time instance of Animal

                                                #ALL ABOUT PROPERTIES
class Human:
    def __init__(self,first,last,age):
        self.first =first
        self.last = last
        if age>=0:
            self._age=age
        else:
            self._age=0

    @property
    def rage(self):
        return self._age
    @rage.setter
    def rage(self,value):
        if value>=0:
            self._age=value
        else:
            raise ValueError("age cant be negative")
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ")
    # def get_age(self):
    #     return self._age
    # def set_age(self, new_age):
    #     if new_age>=0:
    #         self._age=new_age
    #     else:
    #         self._age=0

j = Human("Jane","Goodall",35)
#sposób I. bez używania def
# print(j.get_age())
# print(j.set_age(20))
# print(j.get_age())
#sposób II. z użyciem @
# print(j.rage) #35
j.rage=20
# print(j.rage) #20
# print(j.full_name)
j.full_name ="Gabi PAszk"
# print(j.full_name)
# print(j.__dict__) #{'first': 'Gabi', 'last': 'PAszk', '_age': 20} full name is just property which we set up

class Animal:
    def __init__(self,name,species,sound):
        self.name=name
        self.species = species
        self.sound= sound
    def __repr__(self):     #we put it to the Animal, cause every animal has its species
        return f"{self.name} is a {self.species}"
    def make_sound(self): #or (self,sound), a wtedy ==> {sound}
        print(f"This animal says {self.sound}")
class Cat(Animal):
    def __init__(self, name, breed,toy):
        super().__init__(name,species = "cat",sound="meow") #super() - refers to (parent/based class) Animal in Cat class
        # Animal.__init__(self,name,species) #dłuższy sposób niż super()
        self.breed=breed
        self.toy=toy
    def play(self):
        print(f"{self.name} plays with {self.toy}")

b = Cat("Blue","Scottish Fold","String")
# print(b)
# print(b.species)
# print(b.play())
# print(b.make_sound())
c = Animal("Puszek","dog","wooof")
# print(c)
# print(c.make_sound())




                                        #INHERITANCE EXAMPLE = USER & MODERATOR
class User:
    active_users=0
    @classmethod
    def display_active_users(cls):
        return f"The're currently {cls.active_users} active users."
    @classmethod
    def from_string(cls,data_str): #nie pamiętam po co to???
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))
    def __init__(self,first,last,age):
        self.first= first
        self.last=last
        self.age=age
        User.active_users += 1
    def logout(self):
        User.active_users -=1
        return f"{self.first} has logged out"
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}. {self.last[0]}. "
class Moderator(User):
    active_mod= 0
    @classmethod
    def display_active_mod(cls):
        return f"There're {cls.active_mod} active mods."

    def __init__(self, first,last, age, platform):
        super().__init__(first,last,age)
        self.platform = platform
        Moderator.active_mod += 1

user1= User("Gabi","Paszka",18)
user2 = Moderator("Sylwia","Kołak",20,"jutub")
# print(user1.display_active_users())
# print(User.display_active_users())
# print(Moderator.display_active_mod())

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEee
#zrobione
class Character:
    def __init__(self,name,hp,level):
        self.name=name
        self.hp=hp
        self.level=level
class NPC(Character):
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)
    def speak(self):
        print("I heard there were ..")
villager = NPC("Bob",20,10)
# print(villager.speak())



                                            #MULTIPLE INHERITANCE
                                            #METHOD RESOLUTION ORDER(MRO)
#_mro_
#mro()
#help(cls)
#   A
#  / \
# B   C
#  \ /
#   D
# D,B,C, A
class A:
    def do_sth(self):
        print("Method def A")
class B(A):
    def do_sth(self):
        print("B")
        # super(B, self).do_sth()
class C(A):
    def do_sth(self):
        print("C")
class D(B,C):
    # pass #it'll print B
    def do_sth(self):
        print("D")
        super().do_sth()
# print(D.__mro__)
# print(D.mro()) #list
# print(help(D))
thing = D()
# print(thing.do_sth()) #D and then B

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
class Mother:
    def __init__(self):
        self.eye_color="brown"
        self.hair_color="dark brown"
        self.hair_type = "curly"
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
class Child(Mother,Father):
    #pass
    def __init__(self):
        self.eye_color = "b"
        self.hair_color = "bi"
        self.hair_type = "s"

m = Mother()
f=Father()
k = Child()
# print(k.eye_color)
# print(help(Child))



                                                #POLYMORPHISM
#The same class method works in a...

# raise NotImplementedError("blabla") -> def dupa w każdym class
class Human:
    def __init__(self,first,age):
        self.first=first
        self.age=age
    def __repr__(self):
        return f"Human {self.first}, {self.age} years old"
    def __len__(self):
        return self.age
    def __add__(self, other):
        if isinstance(other,Human):
            return Human(first="Newborn",age=0)
        return "You cant add that"
    def __mul__(self, other):
        if isinstance(other,int):
            return [self for i in range(other)]
        return "Cant multiply!"
        # return "You're multiplying humans"
h = Human("H",29)
j = Human("J",31)
# print(h)    #Human 29 years old
# print(len(h)) #29
# print(h+2) #You cant add that
# print(j*2) #"You're multiplying humans"



                                            #DICTIONARY
class GrumpyDict(dict):
    def __repr__(self):
        # return "None of your business"
        print("None of yr business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU want {key}? Well it aint here")

    def __setitem__(self, key, value):
        print("you want to change the dict?")
        print("Ok, fine..")
        super().__setitem__(key,value)

    def __contains__(self, item):
        print( "NO IT AINT IN HERE!")
        return False

d = GrumpyDict({"name":"Yolo","city":"NYC"})
print(d)
# d["animal"] #YOU want animal? Well it aint here
# d["animal"] = "cat"
# print(d)
# "city" in d #even if it is here (city in dict) it returns false

#EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars
    def __repr__(self):
        return "{} car train".format(self.num_cars)
    def __len__(self):
        return self.num_cars
a_train= Train(4)
# print(a_train)
# print(len(a_train))


