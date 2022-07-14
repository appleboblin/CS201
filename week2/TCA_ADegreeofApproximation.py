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
from decimal import Decimal # able to process larger numbers
# Taylor / Maclaurin Series for Sin (x)
# https://www.youtube.com/watch?v=dp2ovDuWhro
# Assignment
# Simple way 2*3*4*5*6*7 for gradescope

def outPut(angle): # define get user input function
    while True: # continue to run the loop 
        if 1 <= angle <= 90: # only accepts angle ranging 0-90 and numbers
            print("Sin for %s"  % angle + '\u00b0' + " is : " + str(sin(angle))) # Print sin
            print("Cos for %s"  % angle + '\u00b0' + " is : " + str(cos(angle))) # Print cos
            print("Tan for %s"  % angle + '\u00b0' + " is : " + str(tan(angle))) # Print tan
            break # breaks out of while loop
        else: # if input not between 0-90
            angle = float(input("Try Again, Please enter angle size (0 - 90) : ")) # Prompt the user to enter the angle if the input is not within 0-90
            outPut(angle) # run function again
            break # exit out of while loop

# Calculate x Radian
def radian(degrees): # define radian function
    x = Decimal((degrees * 3.1415926)/180) # formula to calculate radian
    return x # return radian

# Factorial nth term
def factorial(n): # define factorial function
    term = n # set current term
    while term >= 2: # loop to run while current term is greater than 2
        term -= 1 # current term minus 1
        n = n * term # multiply previous term with current term and set new value to previous term(n)
    if n == 0: # account for factorial 0 = 1
        return 1 # set n to 0
    return n #  return final number

# Taylor Expansion
def sin(x): # define sin function
    list = [] # Create list
    rad = radian(x) # Create radian variable
    signs = 1 # start at positive
    denominator = 1 # starting denominator for factorial
    count = 1 # starting count
    nTerms = 100 # precision of the calculation, larger number = more accurate
    while count < nTerms: # loop when count is smaller than nTerms
        value = Decimal((pow(rad, denominator)/(factorial(denominator) * signs))) # Calculate each term
        list.append(value) # add each term to list
        denominator += 2 # add two to denominator each term
        count += 1 # add 1 to count, adding up to nTerms
        signs = signs * -1 # change sign each term
    return sum(list) # add lists together and return the number

def cos(x): # define cos function
    list = [] # Create list
    rad = radian(x) # Create radian variable
    signs = 1 # start at positive
    denominator = 0 # starting denominator for factorial
    count = 1 # starting count
    nTerms = 100 # precision of the calculation, larger number = more accurate
    while count < nTerms: # loop when count is smaller than nTerms
        value = Decimal((pow(rad, denominator)/(factorial(denominator) * signs))) # Calculate each term
        list.append(value) # add each term to list
        denominator += 2 # add two to denominator each term
        count += 1 # add 1 to count, adding up to nTerms
        signs = signs * -1 # change sign each term
    return sum(list) # add lists together and return the number

def tan(x): # define tangent function
    return sin(x)/cos(x) # return tangent

def main(): # define main function
    angle = input("Please enter angle size (0 - 90): ") # prompt user to enter angle
    try:
        angle = float(angle)
        outPut(angle) # runs outPut function
    except Exception: # run when theres an error, input not numbers
        print("Error, Please enter a number.") # print out why theres an error
        main() # run main function again

# Call main function
if __name__ == "__main__":
    main()