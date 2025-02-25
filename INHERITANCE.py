class vehicle:
    def __init__(self, carBrand):
        self.brand = carBrand
    
    def DisplayBrand(self):
        print("This car was made by",self.brand)

# THE FOLLOING SIGNIFIES THAT THE CLASS CAR INHERITS FROM THE CLASS VEHICLE
class Car(vehicle):
    def __init__(self, carBrand, carModel):
        super().__init__(carBrand) # INITIALIZING PARENT CLASS IN THE CHILD CLASS 
        self.model = carModel

MY_CAR = Car("tesla", "X")
print(MY_CAR.model)

MY_CAR.DisplayBrand()


class Book:
    def __init__(self, Author, Title):
        self.__myAuthor = Author
        self.__myTitle = Title

    def DisplayBookdetails(self):
        print(f"The book {self.__myTitle} is written by {self.__myAuthor}.")

class Ebook(Book):
    def __init__(self, Author, Title, narrator):

        super().__init__(Author, Title)
        self.__narrator = narrator

    def DisplayEbookDetails(self):
        super().DisplayBookdetails()
        print(f"This book was narrated by {self.__narrator}.")
        

LOTR = Ebook("tolkion", "Lord of the rings", "robert ingles")
LOTR.DisplayEbookDetails()

#THE REAL USE OF SUPER IS TO BUILD UPON THE PARENT CLASS METHODS






