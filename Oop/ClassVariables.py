class Student:

    year = 2024
    no_of_students = 0

    def __init__(self, name):
        self.name = name
        Student.no_of_students += 1

student1 = Student("midhun")
# student2 = Student("midhun")
# student1 = Student("midhun")
# student2 = Student("midhun")
# student1 = Student("midhun")
# student2 = Student("midhun")
# student1 = Student("midhun")
# student2 = Student("midhun")
# student1 = Student("midhun")
# student2 = Student("midhun")
# student1 = Student("midhun")
# student2 = Student("midhun")

print(f"My graduating class of {Student.year} has {Student.no_of_students}")