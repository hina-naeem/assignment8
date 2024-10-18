from typing import List

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}"

class Teacher(Human):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_details(self):
        details = f"Department: {self.name}\n"
        details += "Students:\n"
        for student in self.students:
            details += f"  - {student.get_details()}\n"
        details += "Teachers:\n"
        for teacher in self.teachers:
            details += f"  - {teacher.get_details()}\n"
        return details

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_details(self):
        details = f"University: {self.name}\n"
        for department in self.departments:
            details += department.get_details() + "\n"
        return details

# Example usage
if __name__ == "__main__":
    # Create university
    uni = University("Home University")

    # Create departments
    cs_department = Department("Computer Science")
    ee_department = Department("Electrical Engineering")

    # Create students and teachers
    student1 = Student("Zainab", 20, "S123")
    student2 = Student("Fatima", 22, "S456")
    student3 = Student("Maryam", 20, "S999")
    teacher1 = Teacher("Dr. Khadija", 45, "T789")
    teacher2 = Teacher("Dr. Hafsa", 50, "T101")

    # Add students and teachers to departments
    cs_department.add_student(student1)
    cs_department.add_student(student3)
    cs_department.add_teacher(teacher1)
    ee_department.add_student(student2)
    ee_department.add_student(student3)
    ee_department.add_teacher(teacher2)

    # Add departments to university
    uni.add_department(cs_department)
    uni.add_department(ee_department)

    # Print university details
    print(uni.get_details())



# class Human:
#     def __init__(self):
#         self.name = name
#         self.fatherName = fathername
#         self.age = age
#         self.gender = gender
# class Teacher(Human):
#     def __init__(self,qualification,teachingExperience,name,fatherName,age,gender):
#         self.qualification = qualification
#         self.teachingExperience= teachingExperience
#         super().__init__(name,fatherName,age,gender)
# class Student(Human):
#     def __init__(self,qualification,name,fatherName,age,gender):
#         self.qualification = qualification
#         super().__init__(name,fatherName,age,gender)
# class University(Teacher,Student):
#     def __init__(self, qualification, teachingExperience, name, fatherName, age, gender):
#         Teacher().__init__(qualification, teachingExperience, name, fatherName, age, gender)
#         Student().__init__(qualification,name,fatherName,age,gender)


# teachers ={
#         "name":"Ali",
#         "fathersName":"Muhammad Zaid",
#         "age":35,
#         "gender":"male",
#         "qualification":"Masters in Mathematics",
#         "teachingExperience":"3 years"
#         }
# students={
#         "name":"Ali Ahmad",
#         "fathersName":"Muhammad Ahmad",
#         "age":18,
#         "gender":"male",
#         "qualification":"FSc(med)"
# }
# university={
#         "courses" :["Bachelor in Software Engineering", "Bachelor in Computer Science", "Bachelor in Mathematics", "Bachelor in Business Management"],
#          "timings":["9 am to 2 pm","4 pm to 9 pm"],
#         "shifts":["morning","evening"]
        
# }
# class universityStudents(University):
#     def __init__(self, qualification, teachingExperience, name, fatherName, age, gender):
#         super().__init__(qualification, teachingExperience, name, fatherName, age, gender)