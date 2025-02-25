#Stacks follow last in first out

#Q) Make a stack of Names

lenStack = 5

Names = [""]*lenStack

#represents the first empty space in the stack

StackPointer = 0

#Adding a value to stack

def PUSH(data):
    global Names, StackPointer

    if StackPointer > lenStack:
        print("Stack over flow")

    else:
        Names[StackPointer] = data
        StackPointer +=1

#Removing a value from stack 

def POP(): #no liberty to choose where to pop or what item to pop : value at the top of stack will be popped hence no parameter passed
    
    global StackPointer, Names
    
    if StackPointer == 0:
        print("Stack is empty")

    else:
        popped = Names[StackPointer-1]
        Names[StackPointer-1] = ""
        print(popped) 
        StackPointer -=1

flag = True
while flag:
    Number = input("Enter your command:")

    if Number == "exit":
        flag = False

    elif Number == "a":
        data = input("Please enter you data:")
        PUSH(data)

    elif Number == "b":
        print(Names)
        print(StackPointer)

    
    elif Number == "c":
        POP()




