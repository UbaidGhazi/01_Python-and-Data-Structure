#(a) Create a new program. Write program code to declare the class TreasureChest.

class treasureChest:
     #Private question : String
     #Private answer : Integer
     #Private points : Integer
    
     def __init__(self, questionP, answerP, pointsP):
         self.__question = questionP
         self.__answer = answerP
         self.__points = pointsP
         
#c  (i)The class TreasureChest has a method getQuestion() that returns the question.
         
def getQuestion(self):
    return self.__question
#c2  The class TreasureChest has a method checkAnswer() that takes the user’s answer as a parameter. It returns True if the answer is correct and False otherwise.

def checkAnswer(self, answerP):
    if int(self.__answer) == answerP:
       return True
    else:
       return False
#c3The class TreasureChest has a method getPoints() that takes the number of attempts as a parameter.
    
def getPoints(self, attempts):
    if attempts == 1:
        return int(self.__points)
    elif attempts == 2:
        return int(self.__points) // 2
    elif attempts == 3 or attempts == 4:
        return int(self.__points) // 4
    else:
         return 0 
 
#b)The text file TreasureChestData.txt stores data for five questions, in the order of question, answer, points. 
#arrayTreasure(5) as treasureChest
        
def readData():
    filename = "treasureChestData.txt"
    try:
       file= open(filename,"r")
       dataFetched = (file.readline()).strip()
       while(dataFetched != "" ):
           question = dataFetched
           answer = (file.readline()).strip()
           points = (file.readline()).strip()
           arrayTreasure.append(treasureChest(question, answer, points))
           dataFetched = (file.readline()).strip()
       file.close()
    except IOError:
        print("Could not find file")
 



#c4 (iv) Write program code for the main program to
        
readData()
choice = int(input("Pick a treasure chest to open between 1 - 5"))
if choice > 0 and choice < 6:
   result = False
   attempts = 0
   while result == False:
       answer = int(input(arrayTreasure[choice-1].getQuestion()))
       result = arrayTreasure[choice-1].checkAnswer(answer)
       attempts = attempts + 1
   print(int(arrayTreasure[choice-1].getPoints(attempts)))
   
   
   
   
   
   
   
   