#Declare queue array : Array [0,9] of string
QueueArray = [""] * 10#string 
HeadPointer = 0 #integer 
TailPointer = 0 #integer 
NumItems = 0 #integer

def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumItems
    
    if NumItems >= 10: 
        return False
    
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9: 
        TailPointer = 0 
    else: 
        TailPointer = TailPointer + 1
        
    NumItems = NumItems + 1 
    return True

def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumItems
    
    if NumItems == 0: 
        return False
    else:
        value = QueueArray[HeadPointer] 
        HeadPointer = HeadPointer + 1
        
        if HeadPointer >= 9: 
            HeadPointer = 0
            
        NumItems = NumItems - 1 
        return value
    
    
for x in range(0, 11): 
    data = input("Enter data :")
    flag = Enqueue(data)
    
    if flag == True:
        print("Successful")
        
    else: 
        print("Queue is full")
        
flagdequeue = Dequeue()
flagdequeue2 = Dequeue()
print(flagdequeue)
print(flagdequeue2)
        
        
        
        
        
        
        
        




























