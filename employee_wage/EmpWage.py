import random

PAY_PER_HOUR = 200
FULL_DAY_PRESENT = 2
HALF_A_DAY_PRESENT = 1
ABSENT_FOR_THE_DAY = 0
total_salary = 0
total_hours_worked = 0
total_days_worked = 0


def calculate_employee_wage_of_the_day(max_working_days, max_working_hours):
	global total_salary, total_hours_worked, total_days_worked
	total_days_worked = 0
	total_hours_worked = 0
	working_hours_details = {ABSENT_FOR_THE_DAY: 0, HALF_A_DAY_PRESENT: 4, FULL_DAY_PRESENT: 8}
	for day in range(max_working_days):
		if total_hours_worked >= max_working_hours:
			break
		total_days_worked += 1
		attendance_status = random.choice([FULL_DAY_PRESENT, HALF_A_DAY_PRESENT, ABSENT_FOR_THE_DAY])
		current_day_working_hour = working_hours_details.get(attendance_status)
		total_salary += PAY_PER_HOUR*current_day_working_hour
		total_hours_worked += current_day_working_hour



max_working_days = int(input("Enter working days "))
max_working_hours = int(input("Enter working hours "))
calculate_employee_wage_of_the_day(max_working_days, max_working_hours)
print("Total hours worked = ", total_hours_worked,
      "\nTotal days worked = ", total_days_worked,
      "\nTotal salary earned = ", total_salary)