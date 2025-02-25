#Queues follow the fisrt in first out principle

#Q) Make a Queue of names of students#

lenQueue = 5

Names = [""]* lenQueue
HeadPointer = -1
TailPointer = 0  #usually represents the free space in the queue (sometimes also points to the last element)

def Enqueue(data):   #add and element to the end of the queue if there is an empty space
    
    global HeadPointer 
    global TailPointer
    global Names

    #IMP condition: there should be place in the queue
    
    if TailPointer < lenQueue:
        Names[TailPointer] = data

        #For the first insertion TailPointer and HeadPointer both need to be incremented

        TailPointer +=1

        if HeadPointer == -1:
            HeadPointer = 0

    else:
        print("The Queue is full")


def DeQueue(): #data removed from the head of the list (LIFO):
    
    global HeadPointer 
    global TailPointer
    global Names

    if HeadPointer == -1:
        print("The queue is empty")

    else:
        DeQueued = Names[HeadPointer]
        Names[HeadPointer] = ""
        print(DeQueued)
        HeadPointer +=1

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
















flag = True
while flag:
    Number = input("Enter your command:")

    if Number == "exit":
        flag = False

    elif Number == "a":
        data = input("Please enter you data:")
        Enqueue(data)

    elif Number == "b":
        print(Names)
        print("HP = ",HeadPointer)
        print("TP = ", TailPointer)

    
    elif Number == "c":
        DeQueue()
    

    












