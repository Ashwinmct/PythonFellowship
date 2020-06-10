import random

PAY_PER_HOUR = 200
FULL_DAY_PRESENT = 2
HALF_A_DAY_PRESENT = 1
ABSENT_FOR_THE_DAY = 0
total_salary = 0

def calculate_employee_wage_of_the_day(days):
	global total_salary
	working_hours = {ABSENT_FOR_THE_DAY: 0, HALF_A_DAY_PRESENT: 4, FULL_DAY_PRESENT: 8}
	for day in range(days):
		attendance_status = random.choice([FULL_DAY_PRESENT, HALF_A_DAY_PRESENT, ABSENT_FOR_THE_DAY])
		total_salary+=PAY_PER_HOUR*working_hours.get(attendance_status)
	return total_salary


print("Employee salary for 30 days is = ", calculate_employee_wage_of_the_day(30))
