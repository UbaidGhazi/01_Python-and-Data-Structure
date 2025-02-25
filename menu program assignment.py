def main():
    num_array=[0]* 14
    
    choice=0
    while choice<6:
        print("Press 1 to fill array")
        print("press 2 for print array")
        print("press 3 for linear search")
        print("press 4 for bubblesort")
        print("press 5 for binary search")
        print("press 6 to exit")
         
        choice=int(input("enter your choice"))
        if choice ==1:
            fillarray(num_array)
        elif choice==2:
            printarray(num_array)
        elif choice==3:
            linearsearch(num_array)
        elif choice==4:
            bubblesort(num_array)
        elif choice==5:
            result=binarysearch(num_array)
            if result!=-1:
                print(result)
            else:
                print("EEE")
                   

import random


def fillarray(num_array):
    for x in range(14):
        number=int(random.randint(10,99))+1
        num_array[x]=number

def printarray(num_array):
        #must be a loop
        print(num_array)
        
def linearsearch(num_array):
    x=0
    found=False
    enternum=int(input("Enter a num"))
    while x<14 and found==False:
        if enternum==num_array[x]:
            found= True
        else:
            x=x+1
    if found== True:
        print("item found")
    else:
        print("item not found")
        

def bubblesort(num_array):
    temp=0
    for i in range(len(num_array)):
        for j in range(0,len(num_array)-i-1):
            if num_array[j] > num_array[j+1]:
                temp=num_array[j]
                num_array[j]=num_array[j+1]
                num_array[j+1]=temp
                
        
def binarysearch(num_array):
    enternum=int(input("enter a nnum"))
    low=0
    mid=0
    high=13
    while low <= high:
        low=0
        high=13
        
        mid=(high+low)//2
        if enternum == num_array[int(mid)]:
            return mid
        
        elif enternum < num_array[int(mid)]:
            low=mid+1
        else:
            high=mid-1
        return -1
         
main()
