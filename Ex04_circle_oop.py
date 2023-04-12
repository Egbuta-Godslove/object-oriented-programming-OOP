class Circle:
	pi = 3.14

	def __init__(self, radius):
		self.radius = radius
		
	def circle_circumference(self):
		value_of_circle_circumference = 2*Circle.pi*self.radius
		return value_of_circle_circumference 
	def Circle_area(self):
		area = Circle.pi * self.radius**2
		return area

c1 = Circle(23)
c2 = Circle(24)
print(c1.circle_circumference())
print(c2.Circle_area())
