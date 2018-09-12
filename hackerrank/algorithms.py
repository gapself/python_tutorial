# Bon Apetit!
nk= list(map(int, input().split()))
n,k=nk[0],nk[1]
bill = list(map(int, input().split()))
b = int(input().strip())
def bonAppetit(bill, k, b):
    b_actual= (sum(bill)-bill[k])//2
    return "Bon Appetit" if b_actual==b else b-b_actual

print(bonAppetit(bill, k, b))