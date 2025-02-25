# (a) Write program code to declare the global 2D array Jobs and the global variable NumberOfJobs.

# declare Jobs : Array[0:99 , 0:1] of integer
#Declare NumberOfJobs : Integer
global NumberOfJobs
global Jobs
Jobs = []
NumberOfJobs = 0

# (b) The procedure Initialise() stores –1 in each of the array elements and assigns 0 to NumberOfJobs
def Initialise():
    global Jobs
    global NumberOfJobs
    for x in range(0, 100):
        Jobs.append([-1, -1])
        
    NumberOfJobs = 0

#(c)  The procedure AddJob():
# • takes a job number and priority as parameters
#• stores the job in the next free array element
#• outputs ‘Added’ if the job was successfully stored in the array
#• outputs ‘Not added’ if the job was not successfully stored in the array.
#Write program code for the procedure AddJob()

def AddJob(JobNumber, Priority):
   global NumberOfJobs
   global Jobs
   
   if NumberOfJobs < 100:
       Jobs[NumberOfJobs][0] = JobNumber
       Jobs[NumberOfJobs][1] = Priority
       
       print("Added")
       NumberOfJobs = NumberOfJobs + 1
   else:
       print("Not Added")

#(e) When a new job has been added, the array is sorted into ascending numerical order of priority using an insertion sort.
#Write program code for the procedure InsertionSort() to sort the data into ascending numerical order of priority     
       
def InsertionSort():
    global Jobs
    global NumberOfJobs
    
    for pointer in range(1, NumberOfJobs):
        valuejob = Jobs[pointer][0]
        valuepriority = Jobs[pointer][1]
        
        holeposition = pointer
        
        while holeposition > 0 and Jobs[holeposition-1][1] > valuepriority:
            Jobs[holeposition][0] = Jobs[holeposition-1][0]
            Jobs[holeposition][1] = Jobs[holeposition-1][1]
            holeposition = holeposition - 1
            
        Jobs[holeposition][0] = valuejob
        Jobs[holeposition][1] = valuepriority

#(f) The procedure PrintArray() outputs each job number and priority on a line
def PrintArray():
    global Jobs
    global NumberOfJobs
    for x in range(0, NumberOfJobs):
        jobs = Jobs[x][0]
        priority = Jobs[x][1]
        line = str(jobs) + " " + str(priority)
        
        print(line)

#(d) The main program should call the procedure Initialise() and then use the AddJob()procedure to store the following jobs in the order given:
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

InsertionSort()
PrintArray()