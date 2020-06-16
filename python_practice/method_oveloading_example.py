
def add(data_type, *args):
	answer = '' if data_type == str else 0
	for arg in args:
		answer += arg
	return answer

#driver code
print(add(str,"ash","win"))
print(add(float,1,0.4,6))