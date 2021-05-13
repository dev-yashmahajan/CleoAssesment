class School(object):

  def __init__(self):
    self.students = []
    self.teachers = []
    self.courses = []

  def setStudents(self, students):
    self.students.append(students)

  def setTeachers(self, teachers):
    self.teachers.append(teachers)
  
  def setCourses(self, course):
    self.courses.append(course)

  def getStudents(self):
    return self.students

  def getTeachers(self):
    return self.teachers
  
  def getCourses(self):
    return self.courses


  def getTeacherForCourse(self, course):

    teachersforcourse = []

    for teacher in self.teachers:
      if course in teacher.getCourses():
        teachersforcourse.append(teacher.getName())

    return teachersforcourse
  

  def getStudentGrade(self, student, course):

    courseList = student.getCourses()
    if course in courseList:
      return courseList[course].getGrade()
    else:
      return "Student has not taken this course"


  def getGradePointAvergae(self, student, year, semester):
    courseList = student.getCourses()
    noofcourses = 0
    totalgrade = 0

    for course in courseList:
      if course.year == year and course.semester == semester:
        noofcourses += 1
        totalgrade += course.getGrade()


    return totalgrade / noofcourses



    def getStudentCoursesAndGrades(self, student, year, semester):
      courseList = student.getCourses()
      result = []

      for course in courseList:
        if course.year == year and course.semester == semester:
          result.append(course)

      return result


class Students(object):

  def __init__(self, name):
    self.name = name
    self.courses = []

  def assignCourses(self, course):
    self.courses.append(course)

  def getCourses(self):
    return self.courses

  def getName(self):
    return self.name


class Teacher(object):
  
  def __init__(self, name):
    self.name = name
    self.courses = []

  def assignCourses(self, course):
    self.courses.append(course)

  def getCourses(self):
    return self.courses

  def getName(self):
    return self.name
  

class Courses(object):

  def __init__(self, id, year, semester):
    self.id = id
    self.year = year
    self.semester = semester
    self.grade = 0
    self.students = []
  
  def addStudents(self, student):
    self.students.append(student)

  def getStudents(self):
    return self.students

  def getGrade(self):
    return self.grade

  def setGrade(self, grade):
    self.grade = grade
  

