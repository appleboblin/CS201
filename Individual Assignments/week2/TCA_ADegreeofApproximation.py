import math
from decimal import Decimal
# Taylor / Maclaurin Series for Sin (x)
# https://www.youtube.com/watch?v=dp2ovDuWhro
# Assignment
# Simple way 2*3*4*5*6*7
#pi = 3.1415926
inPut = float(input())
# x = (angle*3.1415926)/180

# Calculate X
def deg(degrees):
    x = Decimal((degrees * 3.1415926)/180)
    return x
# a^b
def pow(base, exponent):
    return base ** exponent
# Factorial nth term Need better function
def fact(n):
    term = n
    while term >= 2:
        term -= 1
        n = n * term
    return n

def compute(x, n):
    if n == 1:
        return x
    else: 
        Decimal((x/n*compute(x,n-1)))
        return

# Taylor Expansion
def sin(x):
    rad = deg(x)
    signs = -1
    denom = 3
    count = 1
    nTerms = 100
    while count < nTerms:
        value = Decimal(rad) + Decimal((pow(rad, denom)/(fact(denom) * signs)))
        #x -= compute(x, denom)
        denom += 2
        count += 1
        signs = signs * -1
    return value #value x

rad = deg(45)
#pnt = pow(-1, n+1)* ((pow(rad, ((2*n)-1)))/fact((2*n)-1))
#pnt = ((pow(-1,))/())
#print(sin(rad))
#print(math.sin(1))
#print(fact(10))
print(sin(inPut))
print(math.sin(inPut))
print(math.cos(inPut))
print(math.tan(inPut))