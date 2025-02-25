#(a) (i) A linear queue is implemented using the 1D array, Queue. The index of the first element in the array is 0.Write program code to declare:


# DECLARE Queue : ARRAY[0:49] OF STRING
global Queue
global HeadPointer # int
global TailPointer # int
Queue = [""] * 50
HeadPointer = -1
TailPointer = 0

# (ii) The procedure Enqueue() takes a string parameter.

def Enqueue(Value):
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer == 50:
        print("The Queue Is Full")
    else:
        Queue[TailPointer] = Value
        TailPointer = TailPointer + 1
        if HeadPointer == -1:
            HeadPointer = 0

# (iii) The function Dequeue() checks if the queue is empty.

def Dequeue():
    global Queue
    global TailPointer
    global HeadPointer

    if HeadPointer == -1:
        print("The Queue Is Empty")
        return "Empty"
    else:
        RemovedItem = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1

    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
    return RemovedItem

#(b)The procedure ReadData() reads the data from the text file and inserts each item of data into the array Queue.

def ReadData():
    try:
        file = open("QueueData.txt", "r")
        for line in file:
            Enqueue(line.strip())
        file.close()
    except IOError:
        print("File Does Not Exist")

#(c) Record structure
class RecordData():
    #PUBLIC ID : STRING
    #PUBLIC Total : INTEGER
    def __init__(self, IDP, TotalP):
        self.ID = IDP
        self.Total = TotalP
        
#(d)The pseudocode algorithm for the procedure TotalData():

#DECLARE Records : ARRAY[0:49] OF RecordData
global Records
global NumberRecords
NumberRecords = 0
Records = []
for x in range(50):
    Records.append(RecordData("", 0))

def TotalData():
    global NumberRecords
    global Records

    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total = Records[x].Total + 1
                Flag = True

    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords = NumberRecords + 1
        
# (d) The procedure OutputRecords() outputs the ID and total of each record in Records in the format:

def OutputRecords():
    global NumberRecords
    for x in range(NumberRecords):
        print("ID", Records[x].ID, "Total", Records[x].Total)

# (e) The main program needs to:
# • call ReadData()
# • call TotalData() for each element in the queue
# • call OutputRecords().
S
ReadData()
while HeadPointer != -1:
    TotalData()
OutputRecords()