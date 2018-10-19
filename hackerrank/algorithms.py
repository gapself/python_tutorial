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


# KANGAROO
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
def kangaroo(x1,v1,x2,v2):
    num_of_jumps1=0
    num_of_jumps2=0
    while x1>x2 and v2>v1 or x2>x1 and v1>v2:
        x1+=v1
        num_of_jumps1+=1
        x2+=v2
        num_of_jumps2+=1
    if x1==x2 and num_of_jumps1==num_of_jumps2:
        return "YES"
    return 'NO'
print(kangaroo(x1,v1,x2,v2))
