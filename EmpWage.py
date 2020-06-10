import random

PAY_PER_HOUR = 200
FULL_DAY_PRESENT = 2
HALF_A_DAY_PRESENT = 1
ABSENT_FOR_THE_DAY = 0


def calculate_employee_wage_of_the_day():
	working_hours = {ABSENT_FOR_THE_DAY: 0, HALF_A_DAY_PRESENT: 4, FULL_DAY_PRESENT: 8}
	attendance_status = random.choice([FULL_DAY_PRESENT, HALF_A_DAY_PRESENT, ABSENT_FOR_THE_DAY])
	return PAY_PER_HOUR*working_hours.get(attendance_status)


print("Employee salary is = ", calculate_employee_wage_of_the_day())
