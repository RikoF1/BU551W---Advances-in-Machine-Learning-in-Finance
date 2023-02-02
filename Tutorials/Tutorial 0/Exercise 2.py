print("Printing current and previous number sum in a range(10)")



def calculate():
    pnum = 0
    for num in range(10):
        sum = num + pnum
        print("Current Number ", num, " Previous Number ", pnum, " Sum: ", sum)
        pnum = num
        
calculate()