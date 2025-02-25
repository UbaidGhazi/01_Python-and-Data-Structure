class Vehicle:
    def __init__(self, ID, Maxspeed, IncAmount):
        #self.__ID Integer
        #self.__Maxspeed Integer
        #self.__Currentspeed = 0
        #self.__IncAmount = 
        #self.__HorizontalPosition = 0
        
        self.__ID = ID
        self.__Maxspeed = Maxspeed
        self.__Currentspeed = 0
        self.__IncAmount = IncAmount
        self.__HorizontalPosition = 0
        
    def GetCurrentSpeed(self):
        return self.__Currentspeed
    
    def GetIncAmount(self):
        return self.__IncAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__Maxspeed
    
    def SetCurrentSpeed(self, val):
        self.__Currentspeed = val
        
    def SetHorizontalPosition(self, val):
        self.__HorizontalPosition = val
    
    def IncreaseSpeed(self):
        self.__Currentspeed += self.__IncAmount
        if self.__Currentspeed > self.__Maxspeed:
            self.__Currentspeed = self.__Maxspeed
            
        self.__HorizontalPosition += self.__Currentspeed
        
    
class helicopter(Vehicle):
    def __init__(self, ID, Maxspeed, IncAmount, VerticalCh, MaxH):
        Vehicle.__init__(self, ID, Maxspeed, IncAmount)   # If using super() then self will not be included
        self.__VerticalPos = 0
        self.__MaxH = MaxH
        self.__VerticalChange = VerticalCh
        self.__Maxheight = MaxH

    
    def IncreaseSpeed(self):
        self.__VerticalPos = self.__VerticalPos + self.__VerticalChange
        if self.__VerticalPos > self.__Maxheight:
            self.__VerticalPos = self.__Maxheight

        super().IncreaseSpeed

























