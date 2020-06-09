import random


class FlipCoin:

#flip a coin and return 'H' for heads and 'T' for tails
   def simulateFlip(self):
       return random.choice(['H', 'T'])


flip_coin = FlipCoin()
print(flip_coin.simulateFlip())





