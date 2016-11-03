import random

class Card:
   ranknames =["Two", "Three", "Four", "Five", "Six", "Seven",
                "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"] #len(13)
   suitnames = ["Clubs", "Diamonds", "Hearts", "Spades"] #len(4)

   def __init__(self,rank,suit):
      self.rank = rank
      self.suit = suit

   def getRank(self):
      return self.ranknames[self.rank]
      
   def setRank(self, rank):
      self.rank = rank

   def getSuit(self):
      return self.suitnames[self.suit]

   def setSuit(self, suit):
      self.suit = suit

   def __str__(self):
      return str(self.ranknames[self.rank])+ " of " + str(self.suitnames[self.suit])

   def __lt__(self, other):
      if self.rank < other.rank:
         return True

      elif self.rank == other.rank:
         if self.suit < other.suit:
            return True
      else:
         return False
       
class Deck():
   def __init__(self):
      self.cardlist = []
      for i in range(4):
         for j in range(13):
            self.cardlist.append(str(Card(j,i)))
            
   def printdeck(self):
      print(self.cardlist)
      
   def shuffle(self):
      random.shuffle(self.cardlist)

def main():
   a = Card(1, 2)
   print("expected output: Three of Hearts")
   print(a)

   b=Card(11,3)
   print("expected output: King of Spades")
   print(b)
   b.setRank(12)
   b.setSuit(0)
   print("expected output: Ace of Clubs")
   print(b)

   print("expected output: false")
   print(a>b)

   c = Deck()
   print("expected output: Two of Clubs, Three of Clubs, etc.")
   c.printdeck()

   c.shuffle()
   print("expected output: Random cards, 52 of them with no repeats")
   c.printdeck()

main()
