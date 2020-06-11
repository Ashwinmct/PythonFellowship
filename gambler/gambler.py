import random

stake = 100
goal = 200
empty_pocket = 0
is_win = 1


def simulate_gambling(times):
	global money
	for term in range(times):
		money = stake
		while goal > money > empty_pocket:
			gamble_status = random.choice([0, 1])
			if gamble_status == is_win:
				money += 1
			else:
				money -= 1
	if money == goal:
		return "YOU WON"
	return "YOU LOST"


print(simulate_gambling(int(input("Enter no of times you want play gambling "))))
