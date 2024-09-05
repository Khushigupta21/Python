# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Derived Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the base class
        self.student_id = student_id

    def get_student_info(self):
        return f"{self.get_info()}, Student ID: {self.student_id}"

# Example usage
student = Student(name="Alice", age=20, student_id="S12345")
print(student.get_student_info())  # Output: Name: Alice, Age: 20, Student ID: S12345
