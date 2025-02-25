#Write program code to declare the class Character and its constructor. Do not program code for the other methods.

class Character:
    #private Name as string
    #private XCoordinate as integer
    #private YCoordinate as integer
    def __init__(self, NameP, XCoordinateP, YCoordinateP):
        self.__Name = NameP
        self.__XCoordiante = XCoordinateP
        self.__YCoordinate = YCoordinateP
#(b) Write program code for the three get methods for the class Character
        
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    
# (c) Write program code for the method ChangePosition()   
    def ChangePosition(self, Xchange, Ychange):
        self.__XCoordinate = self.__XCoordinate + Xchange
        self.__YCoordinate = self.__YCoordinate + Ychange
#The main program has a 1D array of characters. Each character is stored as an object of type Character

Characters = []
try:
    file = open("Characters.txt" , "r")
    for x in range(0, 10):
        name = file.readline().strip()
        xcord = int(file.readline().strip())
        ycoord = int(file.readline().strip())
        CharacterObject = Character(name, xcord, ycord)
        Characters.append(CharacterObject)
except:
    print("File not found")
#(e) The main program needs to read in a character’s name from the user, search for the character in the array and store the index of its position. It repeats until the user enters a name that 
#exists in the array
    
flag = True
while flag == True:
    username = input("Enter Username: ").lower()
    for x in range(10):
        namefromobject = Characters[x].GetName()
        if username.lower() == namefromobject.lower():
            Position = x
            flag = False
#The user will enter a letter to identify the direction the chosen character from part 2(e) should move
            
NewFlag = True
while NewFlag == True:
    direction = input("Enter A, W, S, D : ")
    if direction.upper() == "A":
        Characters[Position].ChangePosition(-1,0)
        NewFlag = False
    elif Direction.upper() == "W":
        Characters[Position].ChangePosition(0,1)
        NewFlag = False
    elif Direction.upper() == "S":
        Characters[Position].ChangePosition(0,-1)
        NewFlag = False
    elif Direction.upper() == "D":
        Characters[Position].ChangePosition(1,0)
        NewFlag = False
        
print(username , "has changed coordiantes to X =" , Character[Position].GetX(),"and Y = ", Character[Position].GetY() )
        
        
        





    
    
    
    
    
    