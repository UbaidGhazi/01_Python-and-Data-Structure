class TreasureChest:
    def __init__(self,question,answer,points):
        # declare Private question :string
        # declare Private answer : integer
        # declare Private points : integer
        self.question = question
        self.answer = answer
        self.points = points

    def getQuestion(self):
        return self.question
    
    def checkAnswer(self,u_answer):
        if u_answer == int(self.answer) :
            return True
        else:
            return False
        
    def getPoints(self,attempts):
        if attempts == 1 :
            return self.points
        elif attempts == 2 :
            p = int(self.points)
            p = p/2
            return p
        elif attempts == 3 or attempts == 4 :
            p = int(self.points)
            p = p/4
        else:
            return 0
        
        
def readData():
    f = open("D://treasure.txt","r")
    data = f.readline()
    data = data.strip("\n")
    while data != "":
        question = data
        data_a = f.readline().strip("\n")
        answer = data_a
        data_p = f.readline().strip("\n")
        points = data_p
        data = f.readline().strip("\n")
        arrayTreasure.append(TreasureChest(question,answer,points))
        
        
arrayTreasure = []
readData()


choice = int(input("Pick a treasure chest to open :"))
if choice >= 1 and choice <= 5:
    b = False
    attempts = 0
    while b == False and attempts < 5:
        x = arrayTreasure[choice-1]
        ques = x.getQuestion()
        print(ques)
        a = int(input("Enter your answer :"))
        b = x.checkAnswer(a)
        attempts = attempts + 1
    print(int(arrayTreasure[choice-1].getPoints(attempts))) 
        
        