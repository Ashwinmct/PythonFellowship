from abc import abstractmethod, ABC

class Polygon(ABC):
	def number_of_sides(self):
		pass

class Triangle(Polygon):
	def number_of_sides(self):
		print("3 sides")

class Hexagon(Polygon):
	def number_of_sides(self):
		print("6 sides")


#driver code
Hexagon().number_of_sides()
Triangle().number_of_sides()