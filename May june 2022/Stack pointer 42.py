global StackData #integer
global StackPointer# Integer
StackData = [0] * 10
StackPointer = 0

def PrintArray():
    print("StackPointer is ", StackPointer)
    for x in range(0, 10):
        print(StackData[x])

def Push(Number):
    global StackData
    global StackPointer
    if StackPointer > 9 :
        return False
    else:
        StackData[StackPointer] = Number
        StackPointer = StackPointer + 1
        return True

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        Temp = StackData[StackPointer]
        return Temp

# main d 1
StackPointer = 0
StackData = [0] * 10
for x in range(0, 11):
    TempNumber = int(input("Enter a number: "))
    if Push(TempNumber) == True:
        print("Stored")
    else:
        print("Stack full")
PrintArray()

Pop()
Pop()
PrintArray()
