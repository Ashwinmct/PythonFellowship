class Human:
	def eat(self):
		print("Human is eating")


class Boy(Human):
	#over ridden method
	def eat(self):
		print("Boy is eating")


#driver code
boy = Boy()
boy.eat()