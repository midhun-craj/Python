class Student: 
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @staticmethod
    def is_a_valid_position(position):
        positions = ["teacher", "student", "principal", "staff"]
        return position in positions

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_gpa / cls.count

student1 = Student("spongebob", 3)
student2 = Student("sandy", 4)
student3 = Student("patrick", 2) 

print(student1.get_info())
print(Student.is_a_valid_position("student"))
print(Student.get_average_gpa())