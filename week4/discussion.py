def tip(bill, percent):
    tips = bill*percent/100
    total = tips+bill
    return total, tips

total, tips = tip(17,17)
print("Total: " + str(total) + "\nTips: " + str(tips))