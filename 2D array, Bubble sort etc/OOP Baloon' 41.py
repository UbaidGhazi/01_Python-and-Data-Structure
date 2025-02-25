class Balloon:
    #Health as integer
    #Colour as string
    #DefenceItem as string
    def __init__(self, PDefenceItem, PColour):
        self.__Health = 100
        self.__Colour = PColour
        self.__DefenceItem = PDefenceItem 
#2(b)
    def GetDefenceItem(self):
        return self.__DefenceItem
#2(c)     
    def ChangeHealth(self, Change):
        self.__Health = self.__Health + Change
# 2(d)
    def CheckHealth(self):
        if self.__Health <= 0:
             return True
        else:
             return False
# 2(e)
Method = input("Enter balloon defence method ")
Colour = input("Enter the balloon colour ")
Balloon1 = Balloon(Method, Colour)
# 2(f)
def Defend(MyBalloon):
    Strength = int(input("Enter the strength of opponent"))
    MyBalloon.ChangeHealth(-Strength)
    print("You defended with ", str(MyBalloon.GetDefenceItem()))
    if(MyBalloon.CheckHealth() == True):
        print("Defence failed")
    else:
         print("Defence succeeded")
    return MyBalloon
# 2(e)
Method = input("Enter balloon defence method ")
Colour = input("Enter the balloon colour ")
Balloon1 = Balloon(Method, Colour)
# 2(g)(i)
Balloon1 = Defend(Balloon1)