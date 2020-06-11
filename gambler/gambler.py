import random

stake = 100
goal = 200
empty_pocket = 0
is_win = 1
gambling_results_by_day = {}


def simulate_gambling(days):
	global money, gambling_results_by_day
	money = stake
	for day in range(days):
		money_before_gamble = money
		money_hi_limit = 1.5 * money
		money_low_limit = 0.5 * money
		while goal > money > empty_pocket and money_hi_limit > money > money_low_limit:
			gamble_status = random.choice([0, 1])
			if gamble_status == is_win:
				money += 1
			else:
				money -= 1
		gambling_results_by_day[day + 1] = money - money_before_gamble
	if money == goal:
		return "YOU WON"
	return "YOU LOST"


print(simulate_gambling(int(input("Enter no of times you want play gambling "))))
print(gambling_results_by_day)

