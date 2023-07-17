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