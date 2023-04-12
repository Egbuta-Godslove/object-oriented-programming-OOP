class student:
	def __init__(self, name,marks):
		self.name = name
		self.marks = marks

	def result(self):
		if self.marks >= 500:
			return 'pass'
		else:
			return 'fail'

s1 = student('james',570)
s2 = student('sarah',470)
s3 = student('paul',770)
s4 = student('felix',270)
s5 = student('peter',57)
s6 = student('samuel',870)

student_objects = {s1, s2, s3, s4, s5, s6}

passStudents = []
failStudents = []
students_results = {}
for x in student_objects:
	if x.result() == 'pass':
		passStudents.append(x.name)
		students_results['Pass students'] = passStudents
	else:
		failStudents.append(x.name)
		students_results['Fail students'] = failStudents

print(students_results)
