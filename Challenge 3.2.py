"""
Implement a function called sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object 
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function 
with different input lists of students.
"""

class Student:
   
 def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

 
def sort_students(student_list):
# Sort the list of students in descending order of CGPA
   sorted_students = sorted(student_list,
                            key=lambda     student: student.cgpa, 
              reverse=True)
#Syntax_lambda arg:exp
   return sorted_students


# Example usage:
students = [
    Student("Priya", "A123", 3.7),
    Student("Madhu", "B124", 3.9),
    Student("Divya", "C125", 3.5),
    Student("Gowri", "D126", 3.8),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
 print("Name:{}, Roll_Number:{}, CGPA:{}".                                  format(student.name, 
                                                  student. roll_number, 
              student.cgpa)) 
 