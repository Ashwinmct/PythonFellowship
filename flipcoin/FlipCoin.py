import random
import operator


class Input:

    @staticmethod
    def get_input(message, input_type):
        try:
            value = input_type(input(message))
            return value
        except ValueError:
            print(" Wrong type of value Entered, Enter again")
            return Input.get_input(message, input_type)



class FlipCoin:
    def simulate_flip(self, flipping_count=None):
        if flipping_count == None:
            flipping_count = 1
        result_of_flipping = ''
        for flip in range(flipping_count):
            result_of_flipping += random.choice(['H', 'T'])
        return result_of_flipping

    def simulate_combinational_flip(self, count):
        flipping_combinations = {'H': 0, 'T': 0, 'HH': 0, 'TT': 0, 'HT': 0, 'TH': 0,
                                 'HHH': 0, 'HHT': 0, 'TTT': 0, 'TTH': 0, 'HTH': 0, 'HTT': 0, 'THT': 0, 'THH': 0}
        for term in range(count):
            combination = self.simulate_flip(random.choice([1, 2, 3]))
            flipping_combinations[combination] = flipping_combinations.get(combination) + 1
        return self.calc_flipping_combination_percentage(count, flipping_combinations)

    def calc_flipping_combination_percentage(self, combinations_count, combinations_dictionary):
        for combination in combinations_dictionary.keys():
            combinations_dictionary[combination] = (combinations_dictionary.get(combination) / combinations_count) * 100
        return combinations_dictionary

    def find_lucky_combination(self, coin_combination_dictionary):
        return max(coin_combination_dictionary.items(), key=operator.itemgetter(1))[0]


#driver code
flip_coin = FlipCoin()
count_of_flips = Input.get_input("Enter numbers of time you want to flip coin ", int)
flipped_coin_combinations = flip_coin.simulate_combinational_flip(count_of_flips)
print(flipped_coin_combinations, "\nYour lucky combination is, ",
      flip_coin.find_lucky_combination(flipped_coin_combinations))
