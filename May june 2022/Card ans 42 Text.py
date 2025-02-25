class Card:
 
    def __init__(self, Numberp, Colourp):
        self.__Number = Numberp
        self.__Colour = Colourp

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

#Declare Cardarray : Array[0:29] of card
#CardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] both same method
CardArray = [0] * 30

File = open("CardValues.txt", "r")

for x in range(30):
    NumberRead = int(File.readline().strip())
    ColourRead = File.readline().strip()
    CardArray[x] = Card(NumberRead, ColourRead)
File.close()
    


NumbersChosen = [False] * (30)

def ChooseCard():
    global NumbersChosen
    flagContinue = True
    while flag == True:
        CardSelected = int(input("Select a Card from 1 to 30: "))
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30")
        elif NumbersChosen[CardSelected - 1] == True:
            print("Already taken")
        else:
            print("Valid")
            flag = False
            
    NumbersChosen[CardSelected - 1] = True
    return CardSelected - 1


Player1 = []
for x in range(4):
    ReturnNumber = ChooseCard()
    Player1.append(CardArray[ReturnNumber])

for x in range(4):
    print(Player1[x].GetColour())
    print(Player1[x].GetNumber())
    
    
    
    
    
    