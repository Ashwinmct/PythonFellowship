import random

stake = 100
winning_status = 1
gambling_results_by_day = {}


def gamble(gambling_amount, dead_line, goal):
	money = gambling_amount
	while goal > money > dead_line:
		gamble_status = random.choice([0, 1])
		money = money+1 if gamble_status else money - 1
	return money


def print_monthly_report():
	winning_day_details = dict(filter(lambda day: day[1] > 0, gambling_results_by_day.items()))
	print("Total days you won: %d, Days you won are " % (len(winning_day_details)), winning_day_details)
	lost_day_details = dict(filter(lambda day: day[1] <= 0, gambling_results_by_day.items()))
	print("Total days you lost: %d, Days you won lost " % (len(lost_day_details)), lost_day_details)


def print_result():
	total_money_loss_or_won = sum(gambling_results_by_day.values())
	if total_money_loss_or_won > 0:
		print("You WON by ", total_money_loss_or_won)
	else:
		print("You Loss by ", total_money_loss_or_won)
	print_monthly_report()


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


def simulate_gambling_for_a_month():
	simulate_gambling(30)


#driving code
simulate_gambling_for_a_month()
