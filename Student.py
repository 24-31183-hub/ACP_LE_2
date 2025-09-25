class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):                 # initialize student attributes
        self.id_name = (student_id, student_name)                                                   # tuple for student id and student name
        self.email = email                                                                          # student email
        self.grades = grades                                                                        # student grades
        self.courses = courses                                                                      # student courses




    def __str__(self):
        return f"Student ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
        # sample = Student1 = Student(1, "Alice", "alice@example.com", {"Math": "A", "Science": "B"}, ["Math", "Science"])
        # result = Student ID: 1, Name: Alice, Email: alice@example.com, Grades: {'Math': 'A', 'Science': 'B'}, Courses: ['Math', 'Science']




class StudentRecords:
    def __init__(self):
        self.students = []                                                                          # list to hold student records
    
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)                     # create a new student object
        self.students.append(new_student)                                                          # add the new student to the list
        # append the new student to the list
        print("Student added successfully.")
    



    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:       # loop through the list of students
            if student.id_name[0] == student_id:                                                        # check if the student id matches
                if email is not None: # update if provided
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                print("Student updated successfully.")
                return
        print("Student not found.")
    



    def delete_student(self, student_id): # delete a student by id
        for student in self.students: # loop through the list of students
            if student.id_name[0] == student_id: 
                self.students.remove(student)
                # removed student from the list
                print("Student deleted successfully.")
                return
        print("Student not found.")
    



    def enroll_course(self, student_id, course): # enroll a student in a course
        for student in self.students:   # loop through the list of students
            if student.id_name[0] == student_id:
                if course not in student.courses:
                    student.courses.append(course)
                    # append the course to the student's course list
                    print(f"Student {student_id} enrolled in course {course}.")
                else:
                    print(f"Student {student_id} is already enrolled in course {course}.")
                return
        print("Not found.")
    
    
    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return student  # show student details
        return "Student not found."
