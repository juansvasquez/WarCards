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
      elif self.rank == other.rank and self.suit == other.suit:
         return False
      else:
         return False

   def __eq__(self, other):
      if self.rank == other.rank:
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

   def pushCard(self, card):
      self.cardlist.append(str(card))

   def pushCardToBottom(self, card):
      self.cardlist.insert(0,str(card))

   def popCard(self):
      return self.cardlist.pop()
      
   def getSize(self):
      return len(self.cardlist)

class Hand(Deck):
   def __init__(self):
      self.cardlist = []
      self.size = 0

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

def test():
    c = Deck()
    c.printdeck()
    print("-----------")
    c.shuffle()
    c.printdeck()
    print("-----------")
 
    d = Hand()
    print("dealing 5 cards")
    for i in range(5):
        d.pushCard(c.popCard())
    d.printdeck()
    print("-----------")
 
    a = Card(5,0)
    b = Card(1,1)
    print("comparing " + str(a) + " and " + str(b))
    print(str(a<b) + " a<b")
    print(str(a>b) + " a>b")
    print(str(a==b) + " a==b")

def war():
   d = Deck()
   p1 = Hand()
   p2 = Hand()
   d.shuffle()
   bucket = []
   print("dealing cards")
   for i in range(d.getSize()):
      if i %2 == 0:
         p1.pushCard(d.popCard())
      else:
         p2.pushCard(d.popCard())
 
   while(p1.getSize() > 0 and p2.getSize() > 0):
      card1 = p1.popCard()
      card2 = p2.popCard()
      print("Player 1 has thrown down " + str(card1) + "; Player 2 counters with " + str(card2))
      if card1 == card2:
         bucket.append(card1)
         bucket.append(card2)
         while card1 == card2:
            print("It's a tie! Draw again!")
            for i in range(3):
               card1 = p1.popCard()
               bucket.append(card1)
               card2 = p2.popCard()
               bucket.append(card2)
            card1 = p1.popCard()
            card2 = p2.popCard()
            print("Player 1 has thrown down " + str(card1) + "; Player 2 counters with " + str(card2))
         
      elif card1 > card2:
         p1.pushCardToBottom(card1)
         p1.pushCardToBottom(card2)
         if bucket != []:
            for i in bucket:
               p1.pushCardToBottom(bucket[i])
         print("Player 1 has won the battle... but not the war.")
      
      else:
         p2.pushCardToBottom(card1)
         p2.pushCardToBottom(card2)
         if bucket != []:
            for i in bucket:
               p2.pushCardToBottom(bucket[i])
         print("Player 2 has won the battle... but not the war.")
      print("Player 1 has " + str(p1.getSize()) + " cards left; Player 2 has " + str(p2.getSize()) + " cards left.")

   if p1.getSize() > 0:
      print("player 1 wins the war.")
   else:
      print("player 2 wins the war.")
      print("game over")

test()
war()
