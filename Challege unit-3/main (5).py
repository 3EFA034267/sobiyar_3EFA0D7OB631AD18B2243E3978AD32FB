class Student:
    def __init__(self,name,roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students


students = [
   Student("sobiyarp8", "R817", 8.5),
   Student("KL rahul", "R818", 8.7),
   Student("jadeja R", "R819", 8.8),
  Student("hashini R", "R820", 8.3),
]

Sorted_Students = sort_students(students)
for student in Sorted_Students:
        print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                        student.roll_number,student.cgpa))
              