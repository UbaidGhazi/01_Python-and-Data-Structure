# (a) (i) Write program code to declare the class Character and its constructor.

import datetime

class Character():
    #PRIVATE CharacterName : STRING
    #PRIVATE DateOfBirth : DATE
    #PRIVATE Intelligence : REAL
    #PRIVATE Speed : INTEGER

    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = IntelligenceP
        self.__Speed = SpeedP
        
# (ii) The get methods GetIntelligence() and GetName() return the attribute values

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

#(iii)The method SetIntelligence() assigns the value of its parameter to the attribute.

    def SetIntelligence(self, NewIntelligenceP):
        self.__Intelligence = NewIntelligenceP
        
# (iv) The method Learn() increases the current value of Intelligence by 10%.

    def Learn(self):
        self.__Intelligence = self.__Intelligence + (self.__Intelligence * 0.1)
        
# (v) The method ReturnAge() calculates and returns the age of the character in years as an integer        
        
    def ReturnAge(self):
        Age = 2023 - self.__DateOfBirth.year
        return Age

# (c) The class MagicCharacter inherits from the class Character. (i)Write program code to declare the class MagicCharacter and its constructor.
class MagicCharacter(Character):
    #PRIVATE Element : STRING
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP, ElementP):
        super().__init__(CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP)
        self.__Element = ElementP

# (c)(ii)  The method Learn() overrides the parent class method and increases the intelligence depending on the character’s element.
#• If the element is fire or water, intelligence increases by 20%.
#• If the element is earth, intelligence increases by 30%.
#• If the element is not fire, water or earth the intelligence increases by 10%.

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.2)
        elif self.__Element == "earth":
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.3)
        else:
            newintelligence = super().GetIntelligence() + (super().GetIntelligence() * 0.1)

        super().SetIntelligence(newintelligence)



#(b) (i) Write program code to create a new instance of Character with the identifier FirstCharacter.
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70.0, 30)
#(ii)Write program code to call the method Learn() for the character created in part 3(b)(i).
FirstCharacter.Learn()
Name = FirstCharacter.GetName()
Age = FirstCharacter.ReturnAge()
Intelligence = FirstCharacter.GetIntelligence()
print(Name, "is", Age, "years old and his intelligence is", Intelligence)

#(d) (i) Write program code to create a new instance of MagicCharacter with the identifier FirstMagic

FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75.0, 22, "fire")

# (ii) Write program code to call the method Learn() for the character created in part 3(d)(i)

FirstMagic.Learn()
Name2 = FirstMagic.GetName()
Age2 = FirstMagic.ReturnAge()
Intelligence2 = FirstMagic.GetIntelligence()
print(Name2, "is", Age2, "years old and his intelligence is", Intelligence2)










