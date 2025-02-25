class PuzzlePlayer():
    def __init__(self):
        self.PlayerID = "PL12a3"
        self.Name = ""
        self.score = 0
        
    def GetPlayerID(self):
        return self.PlayerID
    
    def SetPayerID(self, NewPlayerID):
        ID_para = NewPlayerID
        if len(ID_para) == 6 and Substring(ID_para,0,2) == "PL" :
            return True
        else:
            return False
        
class FoodItem():
    def __init__(self, FoodID_para):
        self.FoodID = FoodID_para
        self.Name = ""
        self.Calories = 0
        
    def GetCalories(self):
        return self.Calories
    
    def SetCalories(self, NewCalories):
        if NewCalories >= 0 and NewCalories <2000:
            self.Calories = NewCalories
            return True
        else:
            return False
        
        
class Lesson():
    def __init__(self, Lesson_type, Lesson_Instructor):
        self.Lesson = Lesson_type
        self.Instructor = Lesson_Instructor
        
    def GetLessonType(self):
        return self.Lesson
    
    def GetFee(self, skill_level):
        if skill_level != 'B' or 'I' or 'A' :
            return -1
        else:
            if skill_level == 'B':
                return $45
            
            elif skill_level == 'I':
                return $50
            
            elif skill_level == 'A':
                return $55
            
            
            
            
            
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    