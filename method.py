class student:
	def __init__(self, name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

	def result(self):
		if self.marks >= 500:
			return 'pass'
		else:
			return 'fail'

s1 = student('paul', 34, 570)
print(s1.result())
