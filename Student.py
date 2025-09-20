class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):                 # initialize student attributes
        self.id_name = (student_id, student_name)                                                   # tuple for student id and student name
        self.email = email                                                                          # student email
        self.grades = grades if grades is not None else {}                                          # student grades
        self.courses = courses if courses is not None else []                                       # student courses

    def __str__(self):
        return f"Student ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
        # sample = Student1 = Student(1, "Alice", "alice@example.com", {"Math": "A", "Science": "B"}, ["Math", "Science"])
        # result = Student ID: 1, Name: Alice, Email: alice@example.com, Grades: {'Math': 'A', 'Science': 'B'}, Courses: ['Math', 'Science']
    
    
