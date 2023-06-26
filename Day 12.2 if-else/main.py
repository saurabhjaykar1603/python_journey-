
# Indentation

# Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

# conditional Statement 
# 1 if statement 

a = 20
b = 20
if a == b:
    print("a is equal to b")
    
# 2 if else statement :

a = 10
b = 20
if a == b:
    print("a is equal to b")
else :
    print("b is unequal to a")
    
a = 50
b = 30
if a > b:
  print("a is greater than b")
else:
 print("b is greater than a")
        
YourAge = 18
RequireAge = 18

if YourAge>=RequireAge:
  print("Your eligible for voting")
else:
  print("Your not eligible for voting")


#  Write a program to check whether entered number is even ir odd by using if-else statements.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

    # https://colab.research.google.com/drive/1xltjEzbwh9_C8A65LI_s3cWvt2eY4icD#scrollTo=dbgjLGfhySqU&line=2&uniqifier=1