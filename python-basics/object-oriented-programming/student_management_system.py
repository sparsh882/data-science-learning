class studentmanager():
  def __init__(self):
    self.dic = {}
    self.menu()
    

  def menu(self):
    print("""\nSTUDENT MANAGER APP
    PRESS 
    1. ADD STUDENT
    2.VIEW STUDENTS
    3.CHECK STUDENT
    4.EXIT""")
    INPUT = input("Please! Enter your Input :")
    if INPUT == '1':
      self.info()
    elif INPUT == '2':
      self.view_student()
    elif INPUT == '3':
      self.check_student()
    elif INPUT == '4':
      print("Thank You for using STUDENT MANAGER APP")
    else :
      print("Invalid Input")
      self.menu
    


  def info(self):
    name = input("Enter student's Name:")
    marks = input("Enter student's Marks:")
    self.dic[name] = marks
    print(f"{name} added successfully with {marks} marks")
    self.menu()

  def view_student(self):
    if not self.dic:
      print("No Students found")
    else:
      print("\n All Students:")
      for name,marks in self.dic.items():
        print(f"{name} : {marks}")
    self.menu()

  def check_student(self):
        name = input("Enter student name to check: ")
        if name in self.dic:
            print(f"{name} has {self.dic[name]} marks")
        else:
            print("Student not found")
        
        self.menu()



s1 = studentmanager()
