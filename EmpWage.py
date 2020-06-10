import random

salary = 0
WORKING_HOURS = 8
PAY_PER_HOUR = 200


def check_employee_attendance():
	if (random.randint(0, 9) % 2 == 0):
		global salary
		salary = WORKING_HOURS * PAY_PER_HOUR
		return "Employee is Present"
	return "Employee is absent"


print(check_employee_attendance())
print("Employee salary is = ", salary)
