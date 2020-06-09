import random


class FlipCoin:

    def simulate_flip(self, flipping_count=None):
        flipping_result = ''
        for flip in range(flipping_count):
            flipping_result += random.choice(['H', 'T'])
        return flipping_result


    def simulate_combinational_flip(self, count):
        flipping_combinations={'H': 0, 'T': 0, 'HH': 0, 'TT': 0, 'HT': 0, 'TH': 0,
                              'HHH': 0, 'HHT': 0, 'TTT': 0, 'TTH': 0, 'HTH': 0, 'HTT': 0, 'THT': 0, 'THH': 0}
        for term in range(count):
            combination = self.simulate_flip(random.choice([1,2,3]))
            flipping_combinations[combination] = flipping_combinations.get(combination) + 1
        return flipping_combinations


flip_coin = FlipCoin()
print(flip_coin.simulate_combinational_flip(24))
