import random


class FlipCoin:

    def simulate_flip(self, flipping_count=None):
        flipping_result = ''
        for flip in range(flipping_count):
            flipping_result += random.choice(['H', 'T'])
        return flipping_result

    def simulate_single_flip(self, count):
        singlet_combination = {'H': 0, 'T': 0}
        for term in range(count):
            combination = self.simulate_flip(1)
            singlet_combination[combination] = singlet_combination.get(combination) + 1
        return singlet_combination

    def simulate_doublet_flip(self, count):
        doublet_combination = {'HH': 0, 'TT': 0, 'HT': 0, 'TH': 0}
        for term in range(count):
            combination = self.simulate_flip(2)
            doublet_combination[combination] = doublet_combination.get(combination) + 1
        return doublet_combination

    def simulate_triplet_flip(self, count):
        triplet_combination = {'HHH': 0, 'HHT': 0, 'TTT': 0, 'TTH': 0, 'HTH': 0, 'HTT': 0, 'THT': 0, 'THH': 0}
        for term in range(count):
            combination = self.simulate_flip(3)
            triplet_combination[combination] = triplet_combination.get(combination) + 1
        return triplet_combination


flip_coin = FlipCoin()
print(flip_coin.simulate_triplet_flip(5))
