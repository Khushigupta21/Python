class Faculty:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.courses = []  # List of courses taught by this faculty

    def add_course(self, course):
        self.courses.append(course)
        if self not in course.faculty:
            course.faculty.append(self)

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.faculty = []  # List of faculty teaching this course

# Example usage
faculty1 = Faculty(name="Dr. Smith", department="Computer Science")
faculty2 = Faculty(name="Dr. Johnson", department="Mathematics")

course1 = Course(course_name="Data Structures", course_code="CS101")
course2 = Course(course_name="Algorithms", course_code="CS102")

# Establishing relationships
faculty1.add_course(course1)
faculty2.add_course(course1)
faculty1.add_course(course2)

# Displaying relationships
print(f"{faculty1.name} teaches the following courses: {[course.course_name for course in faculty1.courses]}")
print(f"{course1.course_name} is taught by: {[faculty.name for faculty in course1.faculty]}")
