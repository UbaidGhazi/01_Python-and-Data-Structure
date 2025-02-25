ArrayNodes=[[0]*3 for x in range (20)] # For Integer
RootPointer = -1 
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode): 
   NodeData = int(input("Enter the Data")) 
   if FreeNode <= 19: 
      ArrayNodes[FreeNode][0] = -1 
      ArrayNodes[FreeNode][1] = NodeData 
      ArrayNodes[FreeNode][2] = -1 
       
      if RootPointer == -1:  # Add to start 
          RootPointer = 0       
      else: 
          Placed = False 
          CurrentNode = RootPointer        
          while Placed == False: 
                 
              if NodeData < ArrayNodes[CurrentNode][1]: 
                  if ArrayNodes[CurrentNode][0] == -1: 
                    ArrayNodes[CurrentNode][0] = FreeNode 
                    Placed = True 
                  else: 
                    CurrentNode = ArrayNodes[CurrentNode][0] 
              else: 
                  if ArrayNodes[CurrentNode][2] == -1: 
                     ArrayNodes[CurrentNode][2] = FreeNode 
                     Placed = True 
                  else: 
                    CurrentNode = ArrayNodes[CurrentNode][2] 
      FreeNode = FreeNode + 1 
   else:
      print("Tree is full") 
   return ArrayNodes, RootPointer, FreeNode


def PrintAll(ArrayNodes):
  for x in range(0, 20):
    print(str(ArrayNodes[x][0]), " ", str(ArrayNodes[x][1])," ", str(ArrayNodes[x][2]))

for X in range(0,10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)
    
PrintAll(ArrayNodes)


def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])
InOrder(ArrayNodes,0)









