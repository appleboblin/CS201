When dining out, tip calculation always bothers me because the bill is never in an easily dividable number. I created a macro on my phone where I can enter the bill amount, select pre-set tip percentages or custom percentages, and the macro will output the bill total and tip amount to write. (a) Input: Cost of bill and percent tip wanted. (b) Output: Total bill amount. (c) Computation: cost of bill multiplied by percent tip (divide by 100 if not given in decimal places), and plus original bill amount to output total bill cost. (d) customers who need to tip often can save some time when paying their bill, since the program dives them the total bill value and the tip amount to write.

My Code:
def tip(bill, percent):
total = (bill*percent/100)+bill
tips = bill*percent/100
return total, tips

I've written a factorial function using a while loop for the assignment a few weeks ago, your function seems a lot easier than what I came up with. Factorial is useful in many applications such as determining the amount of school buses needed for each school district.
Suggestions about the code: to print out new lines you can use `\n` instead of `print()`
