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

#cats&mouse
q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    def catAndMouse(x,y,z):
        distance_B=abs(y-z)
        distance_A=abs(z-x)
        return 'Cat A' if distance_B>distance_A else 'Cat B' if distance_A>distance_B else 'Mouse C'
    print(catAndMouse(x,y,z))

# picking numbers
n = int(input().strip())
a = map(int, input().rstrip().split())
def pickingNumbers(a):
    a=list(a)
    return list(a.count(num) + a.count(num+1) for num in a)
print(pickingNumbers(a))

#migratory birds
n = int(input())
k = list(map(int,input().strip().split()))
count = ([0]*n)
for t in k:
    count[t] += 1
    print(count[1:])
print(count.index(max(count))) #index() returns the lowest index in list that obj appears

#breaking the records
n = int(input())
k= list(map(int, input().rstrip().split()))
def breakingRecords(k):
    best=worst=0
    maxi=low=k[0]
    for i in range(0,n):
        if k[i]>maxi:
            best+=1
            maxi=k[i]
        elif k[i]<low:
            worst+=1
            low=k[i]
    result=[best,worst]
    return ' '.join(map(str, result))
print(breakingRecords(k))