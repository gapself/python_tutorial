#----------------------------------------PAPIER KAMIEN NOZYCE------------------------
choice1 = "rock"
choice2 = "paper"
choice3 = "scissors"



#print("Enter Players 1's choice\n")
player1 = input("Enter 1st Player's choice:\n")
print("***NO CHEATING!\n" * 20)
if player1:
    if player1 == ("rock" or "paper" or "scissors"):
        print("*1st Player's Answer*")
player2 = input("Enter 2nd Player's choice:\n")
if player2:
    if player1=="rock" and player2=="rock" or player1=="paper" and player2=="paper" or player1=="scissors" and player2=="scissors":#== ("rock" or "paper" or "scissors"):
        print("REMIS")
    elif player1=="rock" and player2=="paper" or player1=="scissors" and player2=="rock" or player1=="paper" and player2=="scissors":
        print("2nd Player won")
    else:
        print("1st Player won")
#another shorter way:
player11 = input("player1: ")
player22 = input ("player2: paper, scissors, rock)")
if player11 == player22:
    print("TIE/DRAW")
elif player11=="rock" and player22=="paper" or player11=="scissors" and player22=="rock" or player11=="paper" and player22=="scissors":
        print("2nd Player won")
else:
        print("1st Player won")


#another way:
if player1 == "rock":
    if player2 == "scissors":
        print("player1 wins")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("BLA")

#gracz 1 wpisuje choice i printuje mu zakryta odpowiedz
#gracz 2 wpisuje choice i printuje mu rozwiazanie
#warunki jeśl gracz 1 i gracz 2 wpiszą to i tamto
#rock rock => remis
#paper paper => remis
#scissors scissors =>  remis
#rock paper => SHOOT! gracz2 wygrał xxxxx
#paper rock => SHOOT! gracz1 wygrał
#rock scissors => SHOOT! gracz1 wygrał
#scissors rock => SHOOT! gracz2 wygrał
#paper scissors => SHOOT! gracz2 wygrał
#scissors paper => SHOOT! gracz1 wygrał
