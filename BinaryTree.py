ArrayNodes = [[0]*3 for i in range(0,20)]
rootptr = -1
freeptr = 0

def AddNode(data):
    global rootptr, freeptr, ArrayNodes
    #Do i have free space in my tree
    if freeptr <= 19:
        ArrayNodes[freeptr][0] = -1
        ArrayNodes[freeptr][1] = data
        ArrayNodes[freeptr][2] = -1

        if rootptr == -1:
            #rootptr = freeptr
            rootptr = 0

        else:
            placed = False
            currentptr = rootptr

            while not placed:
                if data < ArrayNodes[currentptr][1]:
                    #in the aboved mentioned case we will be travelling to the left

                    #if no left node
                    if ArrayNodes[currentptr][0] == -1:
                        #link the current node as the left node
                        ArrayNodes[currentptr][0] = freeptr
                        placed = True
                    
                    else:
                        currentptr = ArrayNodes[currentptr][0]
            freeptr +=1

           
    else:
        print("The tree is full")


