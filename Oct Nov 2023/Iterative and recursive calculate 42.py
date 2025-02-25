def IterativeCalculate(Number):
    Total = 0
    ToFind = Number
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total

temp = IterativeCalculate(10)
print(temp)


def Recursivevalue(Number, ToFind):
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + Recursivevalue(Number -1, ToFind)
        else:
            return Recursivevalue(Number - 1, ToFind)


temp2 = Recursivevalue(50, 50)
print("Recursive:", temp2)