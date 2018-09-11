# OOP - make code logical, hierarchical using classes
# hanging profile pic, log out, everyone has another way to do that
print(help(list))
nums = [1,2,3]
print(type(nums)) #<class 'list'>
                                # instances
alex = User('ales',78)

# class - a blueprint for objects, can contain methods(frunctions) and attributs
# instance - construted from a class blueprint that contain their class's methods...

# DEFINING THE SIMPLEST POSSIBLE CLASS
#defining function:
def add():
    return 3
class User:
    pass

user1 =User()
print(type(user1))

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(user1.first,user1.last)
print(user2.first,user2.last)

                            # INSTANTIATING a CLASS

# In this case, v becomes a Honda Civic, a new instance of Vehicle

class Vehicle:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year
v= Vehicle("Honda","Civic","2017")

print(v.make, v.year)

#JAK chcesz domyślnie wpisywać likes = 0 , jeśli nie ma lajków, to wtedy arg=0 :)
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment ("Davey123","bluethecat",3)
another_comment = Comment ("Rosa","omg so cute!")
print(c.username, c.text, c.likes)
print(another_comment.username, another_comment.text, another_comment.likes)

                                        # UNDERSCORES:
# _name
# __name
# __name__

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret= "hi!"
        self.__msg = "I like you"
        self.__lol = "hahaha"
p = Person()
print(p.name)
print(p._secret)
# print(dir(p))
print(p._Person__msg)

print("ODDZIELENIEEEEEEEEE")
print("ATTRIBUTES HERE")
class User:
    active_users =0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1
    def logout(self):
        User.active_users -=1
        return f"{self.first}has logged out"
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    def is_senior(self):
        return self.age >= 65
    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th bday, {self.first}"
print(User.active_users)
user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(User.active_users)
print(user2.logout())
print(User.active_users)
# print(user1.full_name())
print(user1.initials())
print(user1.is_senior()) #True or #False if not a senor
print(user2.age) #41
print(user2.birthday()) #42
print(user2.age) #42

# EXEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEe
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self,num):
        self.balance += num
        return self.balance

    def withdraw(self,num):
        self.balance -= num
        return self.balance

a = BankAccount ("Joe")
print(a.balance)
print(a.deposit(5))
print(a.withdraw(10))

class Pet:
    allowed = ['cat','dog','fish','rat']
    def __init__(self,name,species):
        if species not in Pet.allowed: #Pet.allowe/self.allowed
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species= species
    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        # allowed = ['cat', 'dog', 'fish', 'rat']
        self.species = species
cat = Pet ("Blue","cat")
dog = Pet ("Sis","dog")
tiger = Pet("blue","cat")
dog.species = "Tiger"
cat.allowed = ["bear","snake"]
print(tiger.name) #blue
print(dog.species)  #Tiger
print(cat.set_species("rat")) #None
print(cat.species) #rat
print(Pet.allowed) #['cat', 'dog', 'fish', 'rat']
print(Pet.allowed.append("pig")) #None
print(Pet.allowed) #[list(..),pig]
print(cat.name)
print(cat.allowed) #['bear', 'snake']
print(Pet.set_species)
print(id(cat.allowed))

# EXEEEEEEEEEEEEEEEEEEEEEEEERCIEEEEEEEEEEEEEEEEEEEEEEee
class Chicken:
    total_eggs = 0
    def __init__(self, name, species, eggs=0):
        self.species = species
        self.name= name
        self.eggs =eggs
    def lay_egg(self):
        Chicken.total_eggs +=1
        self.eggs += 1
        return self.eggs

c1 = Chicken("Alice","AAAA")
c2 = Chicken("Amelia","BBBB")
print(c1.eggs)
print(c1.lay_egg())
print(c1.lay_egg())
print(c1.lay_egg())
print(Chicken.total_eggs)
# print(c1.lay_eggs())
# print(c1.lay_eggs())
# print(c1.total_eggs)

                                    # CLASS METHODS
#ROBOOOOOOOOT
class Robots:
    num_of_robots = 0
    def __init__(self,name):
        self.name=name
        print(f"Welcome on the board Mr {self.name}")

        Robots.num_of_robots +=1
    def die(self):
        print("{} is being destroyed".format(self.name))

        Robots.num_of_robots -=1

        if Robots.num_of_robots ==0:
            print(f"{self.name}was the last robot.")
        else:
            print("The are still {:d} robots working".format(Robots.num_of_robots))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots".format(cls.num_of_robots))

robot1 = Robots("ROBOT")
robot1.how_many()

robot2 = Robots("PINK")
robot2.how_many()
robot2.die()





class User:
    active_users =0
    @classmethod
    def display_active_users(cls):
        return f"There're currently {cls.active_users}"
        # print(cls)
    @classmethod
    def from_string(cls,data_str):
        first, last, age = data_str.split(",")
        return cls(first,last,int(age)) #includes 3 variables # cls instead of USer

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1
    def __repr__(self):
        return f"{self.first} is {self.age}"
    def logout(self):
        User.active_users -=1
        return f"{self.first}has logged out"
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    def is_senior(self):
        return self.age >= 65
    def birthday(self):
        self.age +=1
        return f"Happy {self.age}th bday, {self.first}"
print(User.active_users)
user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(User.active_users)
print(user2.logout())
print(User.active_users)
print(User.display_active_users()) # a jeśli PRINT => <class '__main__.User'> , None
user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(User.display_active_users()) # z 2 robi się 4
tom = User.from_string("tom,jones,89")
print(tom.first)
print(tom.full_name())
print(tom.age)
print(tom.birthday())

                            STRING REPRESENTATION EXAMPLE
print(tom)
j = User ("judy","steele",18)
j= str(j)
print(j)

# DECK OF CARDS EXERCISE---------------------------------------
from random import shuffle
class Card:
    def __init__(self,value,suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    or "{} of {}".format(self.value, self.suit)
a = Card("A","Hearts")
print(a)

class Deck:
    def __init__(self):
        suits = ["H", "D", "C", "S"]
        values = ["A", "2", '3', "4", "5", "6"]
        self.cards = [Card(value,suit)for suit in suits for value in values]
        # print(self.cards)
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value,suit))
        # print(self.cards) #lists of multiple variables
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    def count(self):
        return(len(self.cards))
    def _deal(self,num): #num is no of cards which we wanna remove from self.cards
        count = self.count() #we chceck how many card are in the deck
        actual = min([count,num])   #
        print (f"Going to remove {actual} cards")
        if count == 0: #if 0 cards left
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards [:-actual] #gives slices 1,2,3
        #[1,2,3,4,5,6] #if we have 3 cards, [-act:1]gives us slice [4,5,6]
        return cards
    def shuffle(self):
        if self.count()<24:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
a = Deck()
print(a)            #DEck of 24 cards
print(a._deal(2))  #list tego, co wyciągam
print(a.count()) #liczba ile kart pozostało po wcyiągnięciu
print(a._deal(3)) #wyciągam kolejne
print(a.cards) #shuffle

