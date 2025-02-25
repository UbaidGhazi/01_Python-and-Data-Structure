# DECLARE Animal : ARRAY [0 : 19 ] OF STRING
# DECLARE Colour : ARRAY [0 : 9 ] OF STRING
global Animal
global Colour
global AnimalTopPointer # INTEGER
global ColourTopPointer # INTEGER
AnimalTopPointer = 0
ColourTopPointer = 0
Animal = [" "] * 20
Colour = [" "] * 10


def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer = AnimalTopPointer - 1
        returnedvalue = Animal[AnimalTopPointer]
        return returnedvalue

def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", "r")
        for line in AnimalFile:
            PushAnimal(line.strip())
        AnimalFile.close()
    except IOError:
        print("File Does Not Exist")

    try:
        ColourFile = open("ColourData.txt", "r")
        for line in ColourFile:
            PushColour(line.strip())
        ColourFile.close()
    except IOError:
        print("File Does Not Exist")


def PushColour(DataToPush):
    global Colour
    global ColourTopPointer

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global Colour
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer = ColourTopPointer - 1
        returnedvalue = Colour[ColourTopPointer]
        return returnedvalue

def OutputItem():
    ColourPop = PopColour()
    AnimalPop = PopAnimal()

    if ColourPop == "":
        print("No Colour")
        PushAnimal(AnimalPop)
    elif AnimalPop == "":
        print("No Animal")
        PushColour(ColourPop)
    else:
        combine = ColourPop + " " + AnimalPop
        print(combine)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()