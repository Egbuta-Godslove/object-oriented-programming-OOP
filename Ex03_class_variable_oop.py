class student:
    total_marks = 1000
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.total_marks = student.total_marks



s1 = student('bassy', '23', 1069)
s2 = student('john', '19', 1069)
s3 = student('mary', '22', 1069)
s4 = student('sarah', '29', 1069)
s5 = student('joy', '23', 1069)
s6 = student('adam', '21', 1069)
s7 = student('mike', '27', 1069)

print(s1.total_marks)
