#Declare FileData : Array[0:10, 0:1] of string

FileData = [[""] *2 for i in range(11)]

def ReadHighScores(): 
    File = open("Highscore.txt" , "r") 
    for x in range(0, 10): 
        FileData[x][0] = File.readline().strip() 
        FileData[x][1] = File.readline().strip()
    File.close()
 
 
def OutputHighScores(): 
    for x in range(0, 11): 
        Output = FileData[x][0] + " " + str(FileData[x][1]) 
        print(Output)
        
        
#print("before")
#ReadHighScores() 
#OutputHighScores()

#userflag = False
#while userflag == False:
#    Username = input("Enter a username")
#    if len(Username) ==3:
#        userflag = True
        
#scoreflag = False
#while scoreflag == False:
#    Score=int(input("Enter score"))
#    if Score > 1 and Score < 10000:
#        scoreflag = True
        
    
def Arrange(Username,Score):
    for x in range(0,10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = Score
            
            count = x + 1
            while count < 10:
                second1 = FileData[count][0]
                second2 = FileData[count][1]
                FileData[count][0] = Temp1
                FileData[count][1] = Temp2
                
                
                Temp1 = second1
                Temp2 = second2
                count = count +1
            break
        
print("before")
ReadHighScores() 
OutputHighScores()
userflag = False
while userflag == False:
    Username = input("Enter a username")
    if len(Username) ==3:
        userflag = True
        
scoreflag = False
while scoreflag == False:
    Score=int(input("Enter score"))
    if Score > 1 and Score < 10000:
        scoreflag = True

Arrange(Username , Score)
print("After")
OutputHighScores() 

def WriteTopTen(): 
    File = open(Filename, 'w') 
    for x in range(0, 10): 
        Filename.write(str(FileData[x][0]) + '\n') 
        Filename.write(str(FileData[x][1]) + '\n') 
        Filename.close
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    