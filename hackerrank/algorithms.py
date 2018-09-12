# Bon Apetit!
nk= list(map(int, input().split()))
n,k=nk[0],nk[1]
bill = list(map(int, input().split()))
b = int(input().strip())
def bonAppetit(bill, k, b):
    b_actual= (sum(bill)-bill[k])//2
    return "Bon Appetit" if b_actual==b else b-b_actual

print(bonAppetit(bill, k, b))

# Divisible Sum Pairs
n, k = (int(x) for x in input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr) - 1):
    for x in range(1 + i, len(arr)):
        if (arr[i] + arr[x]) % k == 0:
            count += 1

print(count)

# Migratory Birds
input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))