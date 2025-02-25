#DECLARE StackVowel : ARRAY[0:99] OF STRING
#DECLARE StackConsonant : ARRAY[0:99] OF STRING
global StackVowel
global StackConsonant
StackVowel = [""] * 100
StackConsonant = [""] * 100

global VowelTop
global ConsonantTop
VowelTop = 0 # integer
ConsonantTop = 0 # integer

def PushData(Letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop

    if Letter == "a" or Letter == "e" or Letter == "i" or Letter == "o" or Letter == "u":
        if VowelTop == 100:
            print("The Vowel Stack Is Full")
        else:
            StackVowel[VowelTop] = Letter
            VowelTop = VowelTop + 1
    else:
        if ConsonantTop == 100:
            print("The Consonant Stack Is Full")
        else:
            StackConsonant[ConsonantTop] = Letter
            ConsonantTop = ConsonantTop + 1


def ReadData():
    try:
        file = open("StackData.txt", "r")
        for line in file:
            PushData(line.strip())
        file.close()
    except IOError:
        print("The File Does Not Exist")


def PopVowel():
    global StackVowel
    global VowelTop

    if VowelTop == 0:
        return "No data"
    else:
        VowelTop = VowelTop - 1
        PoppedItem = StackVowel[VowelTop]
        return PoppedItem

def PopConsonant():
    global StackConsonant
    global ConsonantTop

    if ConsonantTop == 0:
        return "No data"
    else:
        ConsonantTop = ConsonantTop - 1
        PoppedItem = StackConsonant[ConsonantTop]
        return PoppedItem

ReadData()

combine = ""

for x in range(5):
    UserChoice = input("Enter a Vowel or Consonant: ")
    if UserChoice.lower() == "vowel":
        PoppedVowel = PopVowel()
        if PoppedVowel == "No data":
            print("No Vowels Available")
        else:
            combine = combine + PoppedVowel
    elif UserChoice.lower() == "consonant":
        PoppedConsonant = PopConsonant()
        if PoppedConsonant == "No data":
            print("Now Consonant Available")
        else:
            combine = combine + PoppedConsonant
print(combine)