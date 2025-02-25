mylist = (10, 20, 30, 40, 50, 60, 70, 80, 90)

def LINEAR_SEARCH(item):
    found = False
    while found == False:
        for i in range(len(mylist)):
            if mylist[i] == item:
                found = (not found)
                index = i
    if found  :
        print("Item found at position :",index)
    else:
        print("Item not found")

#item = int(input("Enter item to be found: "))
#LINEAR_SEARCH(item)

def BINARY_SEARCH(item) :
    found = False
    lowerbound = 0
    upperbound = len(mylist)
    while found == False :
        i = int((upperbound + lowerbound) /2)
        if mylist[i] == item :
            found = (not found)
            index = i
        if i == lowerbound or i == upperbound :
            return("item not found")
        if item > mylist[i] :
            lowerbound = i + 1
        
        if item < mylist[i] :
            upperbound = i - 1
    if found :
        print("item found at position", i)
    else :
        print("item not found")
            
            
#BINARY_SEARCH(item)
        
        
sortlist = [20, 2, 40, 30, 80, 7, 5, 90, 4, 2]


def BUBBLE_SORT() :
    top = int(len(sortlist))
    
    swap = False
    while swap or top > 0 :
        swap = not swap
        for i in range(top - 1) :
            if sortlist[i] > sortlist[i + 1] :
                temp = sortlist[i]
                x = sortlist[i + 1]
                sortlist[i] = x
                sortlist[i + 1] = temp
                swap = False
        top = top - 1
                
#BUBBLE_SORT()
#print(sortlist)
        
        

def INSERTION_SORT() :
    lower = 0
    upper = len(sortlist)
    for i in range(lower + 1,upper) :
        key = sortlist[i]
        place = i - 1
        if sortlist[place] > key :
            while place >= lower and sortlist[place] > key :
                temp = sortlist[place + 1]
                sortlist[place + 1] = sortlist[place]
                sortlist[place] = temp
                place = place - 1
            sortlist[place + 1] = key
            
#INSERTION_SORT()
#print(sortlist)
            