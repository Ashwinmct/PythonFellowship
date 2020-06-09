import random


def check_employee_attendance():
	if(random.randint(0,9) % 2 == 0):
		return "Employee is Present"
	return "Employee is abscent"

print(check_employee_attendance())