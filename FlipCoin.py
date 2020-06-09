import random


class FlipCoin:

    def simulate_flip(self, flipping_count=None):
        if (flipping_count is None):
            return random.choice(['H', 'T'])
        flipping_result = ''
        for flip in range(flipping_count):
            flipping_result += random.choice(['H', 'T'])
        return flipping_result

    def simulate_single_flip(self, count):
        singlet_combination = {'H': 0, 'T': 0}
        for term in range(count):
            combination = self.simulate_flip()
            singlet_combination[combination] = singlet_combination.get(combination) + 1
        return singlet_combination


flip_coin = FlipCoin()
print(flip_coin.simulate_single_flip(5))
