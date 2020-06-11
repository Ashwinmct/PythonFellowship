import random
import operator

stake = 100
winning_status = 1
gambling_results_by_day = {}


def gamble(gambling_amount, dead_line, goal):
	money = gambling_amount
	while goal > money > dead_line:
		gamble_status = random.choice([0, 1])
		money = money+1 if gamble_status else money - 1
	return money


def print_monthly_report(operation, status, func):
	day_wise_details = dict(filter(lambda day: operation(day[1], 0), gambling_results_by_day.items()))
	print("Total days you %s : %d, Days you %s are " % (status, len(day_wise_details), status), day_wise_details)
	print("Day you %s mostly " % status, func(gambling_results_by_day.items(), key=operator.itemgetter(1))[0])


def print_monthly_result():
	total_money_loss_or_won = sum(gambling_results_by_day.values())
	if total_money_loss_or_won > 0:
		print("You WON by ", total_money_loss_or_won)
	else:
		print('You LOST by ', total_money_loss_or_won)
	print_monthly_report(operator.__gt__, "won", max)
	print_monthly_report(operator.__le__, "lost", min)


def simulate_gambling(days):
	global gambling_results_by_day
	money = stake
	for day in range(days):
		money_before_gamble = money
		money_hi_limit = 1.5 * money
		money_low_limit = 0.5 * money
		money = gamble(money_before_gamble, money_low_limit, money_hi_limit)
		gambling_results_by_day[day + 1] = money - money_before_gamble
	print_monthly_result()
	if sum(gambling_results_by_day.values()) > 0:
		return simulate_gambling_for_month()


def simulate_gambling_for_month():
	simulate_gambling(30)


#driving code
simulate_gambling_for_month()
