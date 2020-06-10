import random

PAY_PER_HOUR = 200
FULL_DAY_PRESENT = 2
HALF_A_DAY_PRESENT = 1
ABSENT_FOR_THE_DAY = 0


def calculate_employee_wage_of_the_day():
	working_hours = 0
	attendance_status = random.choice([FULL_DAY_PRESENT, HALF_A_DAY_PRESENT, ABSENT_FOR_THE_DAY])
	if(attendance_status is FULL_DAY_PRESENT):
		working_hours = 8
	elif (attendance_status is HALF_A_DAY_PRESENT):
		working_hours = 4
	return working_hours*PAY_PER_HOUR


print("Employee salary is = ", calculate_employee_wage_of_the_day())
