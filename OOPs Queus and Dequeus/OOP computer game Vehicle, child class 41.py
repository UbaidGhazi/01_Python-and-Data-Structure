#(a) (i) Write program code to declare the class Vehicle. All attributes must be private.

class Vehicle():
    # PRIVATE ID : STRING
    # PRIVATE MaxSpeed : INTEGER
    # PRIVATE CurrentSpeed : INTEGER
    # PRIVATE IncreaseAmount : INTEGER
    # PRIVATE HorizontalPosition : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

## (ii)Write program code for the get methods GetCurrentSpeed(),GetIncreaseAmount(), GetMaxSpeed() and GetHorizontalPosition()
        
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
#(iii)Write program code for the set methods SetCurrentSpeed() and SetHorizontalPosition()

    def SetCurrentSpeed(self, CurrentSpeedNew):
        self.__CurrentSpeed = CurrentSpeedNew

    def SetHorizontalPosition(self, HorizontalPositionNew):
        self.__HorizontalPosition = HorizontalPositionNew
        
# (iv) The method IncreaseSpeed():
# • adds IncreaseAmount to the current speed
# • adds the updated current speed to the horizontal position.

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
        
# (c)A procedure needs to output the horizontal position and speed of a vehicle. 

    def Outputprocedure(self):
        print("Current Speed: ", self.__CurrentSpeed)
        print("Horizontal Position", self.__HorizontalPosition)


#(b)The child class Helicopter inherits from the parent class Vehicle.(i)Write program code to declare the class Helicopter.

class Helicopter(Vehicle):
    # PRIVATE VerticalPosition : INTEGER
    # PRIVATE VerticalChange : INTEGER
    # PRIVATE MaxHeight : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VerticalChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalChange = VerticalChangeP
        self.__MaxHeight = MaxHeightP
        self.__VerticalPosition = 0
        
#(ii) The Helicopter method IncreaseSpeed() overrides the method from the parent class and:
# • adds the amount of vertical change to the vertical position
# • adds IncreaseAmount to the current speed
# • adds the updated current speed to the horizontal position.

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()
        
#(c) A procedure needs to output the horizontal position and speed of a vehicle. If the vehicle is a helicopter, it also outputs the vertical position.
#All outputs must include appropriate messages

    def Outputprocedure(self):
        super().Outputprocedure()
        print("Veritcal Position: ", self.__VerticalPosition)

#main
Car = Vehicle("Tiger", 100, 20)
Helicop = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.Outputprocedure()

Helicop.IncreaseSpeed()
Helicop.IncreaseSpeed()
Helicop.Outputprocedure()
        
        
        
        
        
        
        
        
        
        