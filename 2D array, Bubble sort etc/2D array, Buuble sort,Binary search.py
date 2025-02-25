#(a) The main program declares a 2D array of 10 by 10 integer elements.The array is initialised with a random number between 1 and 100 in each element

import random
# Declare ArrayData as a 2D array of 10 by 10 integer elements
ArrayData = [[0] * 10 for x in range(10)]

for x in range(0, 10):
    for y in range(0, 10):
        ArrayData[x][y] = random.randint(1, 100)
        
#(b) The following bubble sort pseudocode algorithm sorts the data in the first dimension of the 2D array into ascending numerical order.

ArrayLength = 10 
for X in range(0, ArrayLength): 
    for Y in range(0, ArrayLength-1): 
        for Z in range(0, ArrayLength - Y - 1): 
            if(ArrayData[X][Z] > ArrayData[X][Z+1]):       #remove in part c
                TempNumber = ArrayData[X][Z] 
                ArrayData[X][Z] = ArrayData[X][Z+1] 
                ArrayData[X][Z+1] = TempNumber
                
# (b) (ii)Write program code for a procedure to output all the values in the 2D array. The values should be output as a 2D grid, with values in rows and columns.
#Call the procedure before and after your bubble sort code.

def PrintArray(ArrayData): 
    for x in range(0, 10): 
        for y in range(0, 10): 
            print(ArrayData[x][y], " ", end='') 
        print("")

print("Before")
PrintArray(ArrayData)                        # remove for part c 2

ArrayLength = 10 
for X in range(0, ArrayLength): 
    for Y in range(0, ArrayLength-1): 
        for Z in range(0, ArrayLength - Y - 1): 
            if(ArrayData[X][Z] > ArrayData[X][Z+1]): 
                TempNumber = ArrayData[X][Z] 
                ArrayData[X][Z] = ArrayData[X][Z+1] 
                ArrayData[X][Z+1] = TempNumber

print("After")
PrintArray(ArrayData)

#(c) The following pseudocode function uses recursion to perform a binary search in the first row f the array, for the value SearchValue in the array SearchArray
#The function returns −1 if the item was not found, or it returns the index where it is found

def BinarySearch(SearchArray, Lower, Upper, SearchValue): 
    if Upper >= Lower: 
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue: 
            return Mid 
        elif SearchArray[0][Mid] > SearchValue: 
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue) 
        else: 
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue) 
    return -1

#(ii) In the main program, test the function BinarySearch() twice, outputting the returned value each time.
# One test should be for a number that is in the first line of the array.
# One test should be for a number that is not in the first line of the array.

print("Before")
PrintArray(ArrayData)

ArrayLength = 10 
for X in range(0, ArrayLength): 
    for Y in range(0, ArrayLength-1): 
        for Z in range(0, ArrayLength - Y - 1): 
            if(ArrayData[X][Z] > ArrayData[X][Z+1]): 
                TempNumber = ArrayData[X][Z] 
                ArrayData[X][Z] = ArrayData[X][Z+1] 
                ArrayData[X][Z+1] = TempNumber

print("After")
PrintArray(ArrayData)

firstcheck = int(input("Enter the number: "))
secondcheck = int(input("Enter the number: "))
print(BinarySearch(ArrayData, 0, 9, firstcheck))
print(BinarySearch(ArrayData, 0, 9, secondcheck))





















































