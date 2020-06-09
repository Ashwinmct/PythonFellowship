import random


class FlipCoin:

#flip a coin and return 'H' for heads and 'T' for tails
   def simulateFlip(self,flipping_count=None):
       if (flipping_count is None):
           return random.choice(['H', 'T'])
       flipping_result=''
       for flip in range(flipping_count):
           flipping_result+=random.choice(['H','T'])
       return flipping_result


flip_coin = FlipCoin()
print(flip_coin.simulateFlip(5))
