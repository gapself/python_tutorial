#yamaha PĘTLA :D
    #printPhoto
    #printprice
#sraha
     #printPhoto
     #printprice
#iterate = powtarzać, quirks = dziwactwa
#FOR - every item, or very number in some range
#for item in iterable_object:
    #do sth with item
#iterable object = collection of items f.ex. list of numbers etc

# [40,32,73]
# for char in "hello": #whatever a char is it represents every single structureof the "hello"
# range(1,10)

# range(7) gives integers from 0 thru 6 (shown) count starts at 0 and is exclusive
# range(1,8) gives integers from 1,7
# range (1,10,2) gives odds from 1 to 10 (not including 10)
# range (7,0,-1) gives integers from 7 to 1

for number in range (1,8): #====> 1, 2, 3, ...., 7
    print(number)
for x in range(1,10):
    print(x)
    print(x*x)
for whatever in "coffee": #whatever odpowiada 1 literce
    print(whatever*10)

r = range (10)
print (list(r))
print(r)
nums = range(1,10,2)
print(nums)
print (list(nums))

for num in range(1,10,2):
    print(num)

nums = range(5)
print(nums)
# #--------------------------ZADANIE------------------
y=0
for m in range (10,21):
    if m%2 !=0:
        y+=m

for i in range(11,21,2):
    x+=i
#
# #----------------------------------------------------ZADANIEEEE----------------
times=input("How many times do I have to tell you?")
times=int(times)
for time in range(times):
    print("CLEAN UP YR ROOM")

#
# times=input("How many times do I have to tell you?")
# times=int(times)
# for time in range(times):
#     print(f"time {time}:CLEAN UP YR ROOM")
#
# times=input("How many times do I have to tell you?")
# times=int(times)
# for time in range(times):
#     print(f"time {time+1}:CLEAN UP YR ROOM")
#
# times=input("How many times do I have to tell you?")
# times=int(times)
# for time in range(5):
#     print(f"time {time}:CLEAN UP YR ROOM")

# ------------WHILE LOOOOOOOOOPS -------------------------------------------------------
#while im_tired:  #while this (imtired) is true We can also iterate using a while loop, which has a different format:
    #seek caffeine
#   while loops continue to execute while a certain condition i struthy and wil end when they become falsy.
user_response = None
while user_response != "please":
    user_response = input("Ah ah ah, you didnt say magic word: ")

msg = input("Whats the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("Whats the secret password")
print("CORRECT!")

for num in range(1,11):  #SAME AS BELOW !!!!!!!!!!!!! COMPARISON
    print(num)

num=1
while num<11:
    print(num)
    num+=1
#---------------------------EXERCISE!!---------------------------------------- EMOOOOOOOOOOOOJI

for x in range(3):                  #MULTIPLYING
    for num in range (1, 11):
        print("\U0001f600"*num)

num=1
while num<11:
    print(num*"\U0001f600")
    num+=1                     # !!!!!!! to powoduje, że nam tak nie zapętla non stop, tylko się zatrzymuje

#WONKY WAY OF DOING THIS EXERCISE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for num in range (1, 11):
    count=1
    smileys = ""
    while count<num:
        smileys += "\U0001f600"
        count+=1
    print(smileys)

#HOW TO CENTER THEM ALL? 1) numbers of emoji should be odd, cause it builds centered pyramid-----------CENTER
num=1
while num<20:
    print(num*"\U0001f600")
    num+=2



# każda linijka emotek(num) musiała by być od samego
# końca przestawiona o jedną emotkę w bok -->
# przestawienie = usunięcie pierwszej i dodanie jeszcze jednej emotki do linjiki w range(1,19) 19, bo nie liczę ostatniej
# wydrukuj dla każdego pola puste miejsce

for num in range (1,2):
    print(num*"\U0001f600")
#for nums in range(2+1,19):

#----------------------------------------EXCERCISE ---------STOP COPYING ME
msg = print("Say sth: ")
while msg == print(input()):
    print((input()))
    if msg is input("Stop copying me"):
        print("UGH FINE YOU WIN")

msg = input("Say sth: ")
while msg != "Stop copying me":
    print (msg)
    msg = input()
print ("UGH")

    #print("UGH FINE YOU WIN")

user_response = None
while user_response != "please":
    user_response = input("Ah ah ah, you didnt say magic word: ")

msg = input("Whats the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("Whats the secret password")
print("CORRECT!")



#najpierw muszę dla każdej wiadomości ustawić taką samą odpowiedź + zapętlić LOOP

#------------------------------CONTROLLED EXIT-------------------------------------
#break - gives the possibility to exit out of WHILE LOOPS whenever we want

while True:
    command = input ("Type 'exit' to exit: ")
    if (command == "exit"):
        break

for x in range(1,100):
    print(x)
    if x == 3:
        break

times=input("How many times do I have to tell you?")
times=int(times)
#times=int(input("How many times do I have to tell ya?"))
for time in range(times):
    print("CLEAN UP YR ROOM")
    if time>= 4:            #zaczyna się od 0,1,2,3,
        print ("WTF")
        break

#co to incrementing??? i+=i zamiast i=i albo i=+i, bo się zapętli do nieskończoności
i=1
while i<10:       #dzieje się 1+1 dla i=1, 2+2 dla i=2, 4+4 dla i=4, 8+8 dla i=8
    i+=i
    print(i)

i=0
while i<=5:    # dla i=0 druknie 1, dla i=1 druknie 2, dla i=2 druknie 3
    i+=1
    print(i)

x=0             #jeśli jest x!=11, to będzie się drukowało w nieskończoność, bo x są parzyste, zatem x nigdy nie będzie 11
while x!=10:   #*jeśli zmienimy na x!=10 dla x=0 druknie: 2, dla x=2, druknie=4,dla x=4 druknie 6, dla x=6 8, dla x=8 10
    x+=2
    print(x)
    # if x ==10:          #dodanie if +break sprawi, iż funkcja nie będzie nieskońćzenie zapętlona
    #     break


#MOJA WERSJA --------------------------------------------------------------------
import random
number = 0
i=0
while number !=5:
    i += 1
    number = random.randint(1, 10)
    print(number)


from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:  # keep looping while number is not 5
    i += 1
    number = randint(1, 10)
    print(number)
