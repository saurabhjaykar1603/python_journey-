# Arbitrary Arguments
# Python Arbitrary Arguments allows a function to accept any number of positional arguments i.e. arguments that are non-keyword arguments, variable-length argument list.

def greeting(* student):
    print(student)
    print(student[0])
    print(student[1])
    print(student[2])
    
greeting("Harshal","Tushar","Ganesh")

# another example
def greetings(* students):
    for i in students:
        print("Hello", i)
greetings("Harshal","Tushar","Ganesh")


# Default Arguments 
def greeting(name = "Saurabh"):
    print("Hello",name,"How are You ?")
greeting()

# another example

def fruits(fruit1, fruit2="mango", fruit3="banana"):
    print(fruit1)
    print(fruit2)
    print(fruit3)
fruits("apple")