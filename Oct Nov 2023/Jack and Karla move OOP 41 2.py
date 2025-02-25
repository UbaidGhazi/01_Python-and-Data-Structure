class Character:
    #self.XPosition integer
    #self.YPosition integer
    #self.Name string
    def __init__(self, XPositionP, YPositionP, NameP):
        self.__XPosition = XPositionP
        self.__YPosition = YPositionP
        self.__Name = NameP

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, Value):
        self.XPosition = self.XPosition + Value
        if(self.XPosition > 10000):
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0
            
        self.__XPosition = NewXPosition

    def SetYPosition(self, Value):
        self.YPosition = self.YPosition + Value
        if(self.YPosition > 10000):
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0
            
        self.__YPosition = NewYPosition 

    def Move(self, Direction):
        if(Direction == "up"):
            self.__YPosition = self.__YPosition + 10
        elif(Direction == "down"):
            self.__YPosition = self.__YPosition - 10
        elif(Direction == "right"):
            self.__XPosition = self.__XPosition + 10
        elif(Direction == "left"):
            self.__XPosition = self.__XPosition - 10

class BikeCharacter(Character):
    def __init__(self, XPositionP, YPositionP, NameP):
        super().__init__(XPositionP, YPositionP, NameP)

    def Move(self, Direction):
        if(Direction == "up"):
            super().SetYPosition(super().GetYPosition() + 20)
        elif(Direction == "down"):
            super().SetYPosition(super().GetYPosition() - 20)
        elif(Direction == "right"):
            super().SetXPosition(super().GetXPosition() + 20)
        elif(Direction == "left"):
            super().SetXPosition(super().GetXPosition() - 20)

Jack = Character(50, 50, "Jack")
Karla = BikeCharacter(100, 50, "Karla")

CharacterToMove = input("Would you like to move Jack or Karla?").lower()
while CharacterToMove != "jack" and CharacterToMove != "karla":
    CharacterToMove = input("Invalid try again")
Direction = input("Which direction? Up, down, left or right?")
while Direction != "up" and Direction != "down" and Direction != "left" and Direction != "right":
    Direction = input("Invalid try again")
if CharacterToMove == "jack":
    Jack.Move(Direction)
    print("Jack's new position is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
else:
    Karla.Move(Direction)
    print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())
