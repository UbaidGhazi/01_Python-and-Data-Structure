global Queue
global HeadPOinter
global TailPointer

Queue = [] * 100 #Integer
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global Queue
    global TailPointer
    global HeadPOinter
    if TailPointer < 100 :      
        Queue[TailPointer] = Data
        TailPointer = TailPointer + 1
        
    if HeadPointer  == -1:
        HeadPointer = 0
        
        return True
    return False

def Dequeue(Data):
    global Queue
    global TailPointer
    global HeadPOinter
        
    if HeadPointer  == -1:
        print("Queue is empty")
    else:
        item = Queue[HeadPointer]
        return item
        HeadPointer = HeadPointer + 1
    
    if HeadPointer == TailPointer:
        TailPointer = 0
        HeadPointer = -1


finalflag = True
for num in range(1, 21):
    temp = Enqueue(num)
    if temp == False:
        finalflag = False
        
if finalflag == True:
    print("Success")
else:
  print("UnSuccessful")
  
def RecursiveOutput(Start):
    if Start < 0 :
        return 0
    else:
         return Queue[Start] + RecursiveOutput(Start - 1) 
           
temp = RecursiveOutput(TailPointer)
print(temp)