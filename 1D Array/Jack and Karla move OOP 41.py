class Character():
    #PRIVATE Name : STRING
    #PRIVATE XPosition : INTEGER
    #PRIVATE YPosition : INTEGER
    def __init__(self, NameP, XPositionP, YPositionP):
        self.__Name = NameP
        self.__XPosition = XPositionP
        self.__YPosition = YPositionP

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, NewXPosition):
        if NewXPosition > 10000:
            NewXPosition = 10000
        elif NewXPosition < 0:
            NewXPosition = 0

        self.__XPosition = NewXPosition

    def SetYPosition(self, NewYPosition):
        if NewYPosition > 10000:
            NewYPosition = 10000
        elif NewYPosition < 0:
            NewYPosition = 0

        self.__YPosition = NewYPosition

    def Move(self, Direction):
        if Direction == "up":
            self.__YPosition = self.__YPosition + 10
        elif Direction == "down":
            self.__YPosition = self.__YPosition - 10
        elif Direction == "left":
            self.__XPosition = self.__XPosition - 10
        elif Direction == "right":
            self.__XPosition = self.__XPosition + 10


Jack = Character("Jack", 50, 50)

class BikeCharacter(Character):
    def __init__(self, NameP, XPositionP, YPositionP):
        super().__init__(NameP, XPositionP, YPositionP)

    def Move(self, Direction):
        if Direction == "up":
            super().SetYPosition(super().GetYPosition() + 20)
        elif Direction == "down":
            super().SetYPosition(super().GetYPosition() - 20)
        elif Direction == "left":
            super().SetXPosition(super().GetXPosition() - 20)
        elif Direction == "right":
            super().SetXPosition(super().GetXPosition() + 20)

Karla = BikeCharacter("Karla", 100, 50)

UserCharacter = input("Choose Character : Jack or Karala: ")
UserDirection = input("Direction: up, down, left, right: ")

if UserCharacter == "Jack":
    Jack.Move(UserDirection)
    Xvalue = Jack.GetXPosition()
    Yvalue = Jack.GetYPosition()
    print("Jack's new position is X =", Xvalue, "Y =", Yvalue)
elif UserCharacter == "Karala":
    Karla.Move(UserDirection)
    Xvalue = Karla.GetXPosition()
    Yvalue = Karla.GetYPosition()
    print("Karala's new position is X =", Xvalue, "Y =", Yvalue)