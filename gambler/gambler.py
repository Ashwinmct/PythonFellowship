import random

stake = 100
empty_pocket = 0
is_win = 1
gambling_results_by_day = {}


def gamble(gambling_amount, dead_line, goal):
	money = gambling_amount
	while goal > money > dead_line:
		gamble_status = random.choice([0, 1])
		if gamble_status == is_win:
			money += 1
		else:
			money -= 1
	return money


def simulate_gambling(days):
	global gambling_results_by_day
	money = stake
	for day in range(days):
		money_before_gamble = money
		money_hi_limit = 1.5 * money
		money_low_limit = 0.5 * money
		money = gamble(money_before_gamble, money_low_limit, money_hi_limit)
		gambling_results_by_day[day + 1] = money - money_before_gamble


simulate_gambling(int(input("Enter no of days you want play gambling ")))
print(gambling_results_by_day)
