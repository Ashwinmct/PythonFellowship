import random

stake = 100
winning_status = 1
gambling_results_by_day = {}


def gamble(gambling_amount, dead_line, goal):
	money = gambling_amount
	while goal > money > dead_line:
		gamble_status = random.choice([0, 1])
		if gamble_status == winning_status:
			money += 1
		else:
			money -= 1
	return money


def print_result():
	total_money_loss_or_won = sum(gambling_results_by_day.values())
	if total_money_loss_or_won > 0:
		print("You WON by ", total_money_loss_or_won)
	else:
		print("You Loss by ", total_money_loss_or_won)


def simulate_gambling(days):
	global gambling_results_by_day
	money = stake
	for day in range(days):
		money_before_gamble = money
		money_hi_limit = 1.5 * money
		money_low_limit = 0.5 * money
		money = gamble(money_before_gamble, money_low_limit, money_hi_limit)
		gambling_results_by_day[day + 1] = money - money_before_gamble
	return print_result()


simulate_gambling(int(input("Enter no of days you want play gambling ")))
print(gambling_results_by_day)
