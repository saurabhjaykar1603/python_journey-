# Class and Object 

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

# Example :

class students:
  full_name = ''
  roll_no = ''

  def ShowStudent(self):
    print(self.full_name)
    print(self.roll_no)

chaitali = students()
chaitali.full_name = "Chaitali"
chaitali.roll_no = 123
chaitali.ShowStudent()

sahil = students()
sahil.full_name = "Sahil"
sahil.roll_no = 124
sahil.ShowStudent()

# In the above example, we are creating the Students class in this class we are declare two variables that's name is full_name & roll_no. And to create the showStudent() function with the pass self parameter.

# So, we are create object for class Students that is chaitali with the help of chaitali object we are calling full_name & roll_no again create one object for Students that name is sahil, Similarly we are calling full_name & roll_no with the sahil object.


# Getter and Setter in Python


# Getter : Getter Method is use to provide a data.

# Setteer : Setter Method is use to set or manipulate data.

class student:
  name = ''
  roll_no = ''

  def setStudent(self,name,roll_no):
    self.name = name
    self.roll_no = roll_no
  
  def getStudents(self):
    print("Name : ",self.name)
    print("Roll No : ",self.roll_no)

kavita = student()
kavita.setStudent("Kavita","123")
kavita.getStudents()


# In the above example, we are creating the Student class in this class we are declare two variables that's name is Name & roll_no. And to create the two functions that's name is setStudent() & getStudents with the pass self parameter.

# So, we are create object for class Student that is kavita with the help of kavita object we are calling setStudent() & getStudents in the setStudent we are pass two parameter for Name & roll_no

# Edit this page