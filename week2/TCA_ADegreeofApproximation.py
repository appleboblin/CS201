# # Just for gradescope to give points.
# inPut = float(input())
# x = inPut * 3.14/180
# def sin(x):
#     return x - ((x*x*x)/(3*2*1)) + ((x*x*x*x*x)/(5*4*3*2*1)) + ((x*x*x*x*x*x*x)/(7*6*5*4*3*2*1))
# def cos(x):
#     return 1 - ((x*x)/(2*1)) + ((x*x*x*x)/(4*3*2*1)) + ((x*x*x*x*x*x)/(6*5*4*3*2*1))
# def tan(x):
#     # return sin(x)/cos(x)
#     return x + ((1/3)*(x*x*x)) + ((2/15)*(x*x*x*x*x)) + ((17/315)*(x*x*x*x*x*x*x))
# print(sin(x))
# print(cos(x))
# print(tan(x))

# Accurate calculations
from decimal import Decimal
# Taylor / Maclaurin Series for Sin (x)
# https://www.youtube.com/watch?v=dp2ovDuWhro
# Assignment
# Simple way 2*3*4*5*6*7 for gradescope

# Nicer looking
def inPut():
    angle = float(input("Please enter angle size (0 - 90): "))
    while True:
        if 1 <= int(angle) <= 90:
            print("Sin for %s"  % angle + '\u00b0' + " is : " + str(sin(angle)))
            print("Cos for %s"  % angle + '\u00b0' + " is : " + str(cos(angle)))
            print("Tan for %s"  % angle + '\u00b0' + " is : " + str(tan(angle)))
            break
        angle = float(input("Try Again, Please enter angle size (0 - 90) : "))  

# inPut = float(input())

# Calculate X
def deg(degrees):
    x = Decimal((degrees * 3.1415926)/180)
    return x
# a^b
def pow(base, exponent):
    return base ** exponent
# Factorial nth term
def fact(n):
    term = n
    while term >= 2:
        term -= 1
        n = n * term
    if n == 0: # factorial 0 = 1
        n = 1
    return n

# Taylor Expansion
def sin(x): 
    list = [] # Create list
    rad = deg(x)
    #list.append(rad) # append rad to list
    signs = 1
    denom = 1
    count = 1
    nTerms = 100
    while count < nTerms:
        value = Decimal((pow(rad, denom)/(fact(denom) * signs))) # skips term 1
        list.append(value) # add term to list
        denom += 2
        count += 1
        signs = signs * -1
    return sum(list) # add lists together

def cos(x):
    list = []
    rad = deg(x)
    signs = 1
    denom = 0
    count = 1
    nTerms = 100
    while count < nTerms:
        value = Decimal((pow(rad, denom)/(fact(denom) * signs)))
        list.append(value)
        denom += 2
        count += 1
        signs = signs * -1
    return sum(list)

def tan(x):
    return sin(x)/cos(x)

inPut()