def tip(bill, percent):
    total = (bill*percent/100)+bill
    tips = bill*percent/100
    return total, tips

total, tips = tip(17,17)
print("Total: " + str(total) + "\nTips: " + str(tips))