import CourseClass as c

course1 = c.Course()

print(course1)

course1.assign_title("Advanced Python")
course1.assign_CRN(125468)
course1.assign_capacity(5)
course1.assign_code("MIS4322")

course2 = c.Course()

course2.assign_title("Database Development")
course2.assign_CRN(985474)
course2.assign_capacity(40)
course2.assign_code("MIS4340")

course_dict = {}

course_dict[course1.get_CRN()] = course1.get_capacity()
course_dict[course2.get_CRN()] = course2.get_capacity()

print(course_dict)