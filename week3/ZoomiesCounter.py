run = 0
jump = 0
stairs = 0
couch = 0
floor = 0
pant = 0
collapse = 0
nap = 0
while True:
    # action = str(input("What's the action of the dog? "))
    # try:
    #     if action == "run":
    #         run += 1
    #     elif action == "jump":
    #         jump += 1
    #     elif action == "stairs":
    #         stairs += 1
    #     elif action == "couch":
    #         couch += 1
    #     elif action == "floor":
    #         floor += 1
    #     elif action == "pant":
    #         pant += 1
    #     elif action == "collapse":
    #         collapse += 1
    #     elif action == "nap":
    #         nap += 1
    #         print("run=" + str(run))
    #         print("jump=" + str(jump))
    #         print("stairs=" + str(stairs))
    #         print("couch=" + str(couch))
    #         print("floor=" + str(floor))
    #         print("pant=" + str(pant))
    #         print("collapse=" + str(collapse))
    #         print("nap=" + str(nap))
    #         break
    #     else:
    #         print("Action not in the pre-programed list.")
    # except:
    #     print("Please enter an action.")
    action = str(input())
    if action == "run":
        run += 1
    elif action == "jump":
        jump += 1
    elif action == "stairs":
        stairs += 1
    elif action == "couch":
        couch += 1
    elif action == "floor":
        floor += 1
    elif action == "pant":
        pant += 1
    elif action == "collapse":
        collapse += 1
    elif action == "nap":
        nap += 1
        break
print("run=" + str(run))
print("jump=" + str(jump))
print("stairs=" + str(stairs))
print("couch=" + str(couch))
print("floor=" + str(floor))
print("pant=" + str(pant))
print("collapse=" + str(collapse))
print("nap=" + str(nap))