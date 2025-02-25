# (a) Write program code to declare a global 1D array, DataArray, with space for 100 integer values.
DataArray = [0] * 100

# (b) The procedure ReadFile() must read in the numbers from the text file and store each one in the array. Use appropriate exception handling
def ReadFile(): 
    global DataArray 
    
    try:
        File = open("IntegerData.txt" , "r") 
        for x in range(0, 100): 
            temp =int(File.readline().strip()) 
            DataArray[x] = temp
        File.close() 
    except IOError:
        print("Count not find file")
# (c) The function FindValues() asks the user to enter a number to search for in the array.The number input must be a whole number between 1 and 100 inclusive. The function then 
#returns the number of times the number input appears in the array

def FindValues():
    global DataArray
    
    flag = False
    
    while flag == False:
        DataToFind = int(input("Enter the number : " ))
        if DataToFind > 1 and DataToFind < 100:
            flag = True
            
    count = 0
    for x in range(0,100):
        if DataArray[x] == DataToFind:
            count = count + 1
            
    return count
# (d) (i) Write program code to call ReadFile() and FindValues() from the main program.The return value from FindValues() must be output with an appropriate message.

ReadFile()
numcount = FindValues()                                           # removed and placed in bubblesort
print("The count of this number is" + " " + str(numcount))

# (e) The procedure BubbleSort() needs to perform a bubble sort on the array and print the contents of the sorted array.
# Write program code for the procedure BubbleSort() and call it from the main program.

def BubbleSort():
    global DataArray
    
    for x in range(0,100):
        for y in range(0,99): 
            if DataArray[x] > DataArray[y+1]:
                temp = DataArray[y]
                DataArray[y] =  DataArray[y+1]
                DataArray[y+1] = temp                
                
                
#main     
ReadFile()
numcount = FindValues()
print("The count of this number is" + " " + str(numcount))

BubbleSort()
for x in range(100):
    print(DataArray[x])

        
    