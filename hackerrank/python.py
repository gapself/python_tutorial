#Mutations
# s = list(input())
# posichar =input().split()
# posi,char=int(posichar[0]),str(posichar[1])
# def mutate_string(s, posi, char):
#     #1st version
#     s[posi]= char
#     return "".join(s)
def mutate_string(s, posi, char):
    #shorter way:
    return s[:posi]+char+s[posi+1:]

#Text Wrap
def wrap(s, m):
    return "\n".join([s[i:i+m] for i in range(0, len(s), m)])

#Swap Case
def swap_case(s):
    return s.swapcase()

#Find a String
def count_substring(string, substring):
    long=len(string)
    short=len(substring)
    sum=0
    for i in range(long-short+1):
        if string[i:i+short] == substring:
            sum += 1
    return sum

#find the second max value
n = int(input())
arr = list(map(int, input().split()))
removed=max(arr)
while max(arr)==removed:
    arr.remove(max(arr))
print(max(arr))

# COMMANDS
n = int(input())
lista = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

#CONCATENATE
import numpy
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print(numpy.concatenate((array_1, array_2), axis = 1))
import numpy as np
N,M,P=map(int,input().split())
arrN=np.array([input().split() for _ in range(N)],int)
arrM=np.array([input().split() for _ in range(M)],int)
print(np.concatenate((arrN,arrM),axis=0))

#MIN MAX
import numpy

my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.min(my_array, axis = 0))       #Output : [1 0]
print(numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
print(numpy.min(my_array, axis = None))      #Output : 0
print(numpy.min(my_array))                   #Output : 0

N,M = map(int,input().split())
arrayN= numpy.array([input().split() for _ in range(N)],int)
print(max(numpy.min(arrayN,axis=1)))

# Classes: Dealing with Complex Numbers
import math
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+no.real*self.imaginary)
    def __truediv__(self, no):
        return Complex((self.real*no.real+self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2),(self.imaginary*no.real-self.real*no.imaginary)/(no.real**2+no.imaginary**2))
    def mod(self):
        return Complex(math.sqrt(self.real**2+self.imaginary**2),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

C = Complex(*map(float, input().strip().split()))
D = Complex(*map(float, input().strip().split()))
print(C+D)
print(C-D)
print(C*D)
print(C/D)
print(C.mod())
print(D.mod())