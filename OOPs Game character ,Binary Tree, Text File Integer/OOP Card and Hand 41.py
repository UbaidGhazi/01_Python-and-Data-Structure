#(a) (i) Write program code to declare the class Card, its attributes and constructor.
#Number as integer , #Colour as string
class Card:
 def __init__(self, NumberP, ColourP):
     self.__Number = NumberP;
     self.__Colour = ColourP;
#(ii) Write program code for the class methods GetNumber() and GetColour()     
 def GetNumber(self):
      return self.__Number
 def GetColour(self):
      return self.__Colour
    
#(b) (i) Write program code to declare the class Hand, its attributes and constructor
    
class Hand:
  #Private Card: Array[0,9] of card
  #Private FirstCard :integer
  #Private NumberCards as integer
    
  def __init__(self, Card1, Card2, Card3, Card4, Card5):
      self.__FirstCard = 0
      self.__NumberCards = 5
      self.__Cards = []
      self.__Cards.append(Card1)
      self.__Cards.append(Card2)
      self.__Cards.append(Card3)
      self.__Cards.append(Card4)
      self.__Cards.append(Card5)
#(b)(ii) The get method GetCard() takes an index as a parameter and returns the card stored at that index in the array.
      
  def GetCard(self, index):
      return self.__Cards[index]

#(a)(iii) The program is tested with the following cards:
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")
    

#(iii) Two players are declared with 5 cards each.

    
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)

#  (c) The function CalculateValue() takes a player’s hand as a parameter and returns a score calculated using the following rules

def CalculateValue(Player):
    Score = 0
    for x in range(0, 5):
        Card = Player.GetCard(x)
        Score = Score + Card.GetNumber()
        Colour = Card.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score

score1 = CalculateValue(Player1)
score2 = CalculateValue(Player2)


if score1 > score2:
    print("Player 1 wins")
elif score2 > score1:
    print("Player 2 wins")
else:
    print("draw")
    
    
    
    