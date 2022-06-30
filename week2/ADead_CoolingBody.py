# # Assignment
# # Ask for input
# temperature_0 = float(input())
# # Compute
# temperature_1 = temperature_0 + (27 - temperature_0) * 0.2
# temperature_2 = temperature_1 + (27 - temperature_1) * 0.2
# temperature_3 = temperature_2 + (27 - temperature_2) * 0.2
# temperature_4 = temperature_3 + (27 - temperature_3) * 0.2
# # Print output
# print(temperature_1)
# print(temperature_2)
# print(temperature_3)
# print(temperature_4)

# # Learning how class works
# # init for import modules and main for running the module itself
# class Temperature:
#     # Initialize
#     def __init__(self):
#         # Degree sigh
#         a = '\u00b0' 
#         # Ask for input
#         self.tmp = float(input("Temperature right when the body died ("+a+"C): "))

#     def compute(self):
#         # Compute temp Temperatures
#         tmp1 = self.tmp + (27 - self.tmp) * 0.2
#         tmp2 = tmp1 + (27 - tmp1) * 0.2 
#         tmp3 = tmp2 + (27 - tmp2) * 0.2 
#         tmp4 = tmp3 + (27 - tmp3) * 0.2 
#         tmp1 = str(tmp1)
#         tmp2 = str(tmp2)
#         tmp3 = str(tmp3)
#         tmp4 = str(tmp4)
#         print("Body temperature 1 hour after death: " + tmp1 + '\u00b0' + "C")
#         print("Body temperature 2 hours after death: " + tmp2 + '\u00b0' + "C")
#         print("Body temperature 3 hours after death: " + tmp3 + '\u00b0' + "C")
#         print("Body temperature 4 hours after death: " + tmp4 + '\u00b0' + "C")
# # Call class and function
# Temperature().compute()

# Main
def main():
    tmp = float(input("What is the temperature right when the body died ("+ '\u00b0' +"C)?: "))
    compute(tmp)
# Compute and print
def compute(tmp):
    hours = 0
    while hours <= 3:
        hours += 1
        hrTxt = " hours"
        tmp = tmp + (27 - tmp) * 0.2
        # # V1
        # if hours == 1:
        #     fmtTmp = "{:.2f}".format(tmp)
        #     ptTmp = str(fmtTmp)
        #     print("Body temperature " + str(hours) + " hour after death: " + ptTmp + '\u00b0' + "C")
        # else:
        #     fmtTmp = "{:.2f}".format(tmp)
        #     ptTmp = str(fmtTmp)
        #     print("Body temperature " + str(hours) + " hours after death: " + ptTmp + '\u00b0' + "C")
        # V2
        if hours == 1:
            hrTxt = " hour"
        fmtTmp = "{:.2f}".format(tmp)
        ptTmp = str(fmtTmp)
        print("Body temperature " + str(hours) + hrTxt +" after death: " + ptTmp + '\u00b0' + "C")
# Call main function
if __name__ == "__main__":
    main()
