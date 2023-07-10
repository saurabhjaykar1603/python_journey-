# while loop in python
# while loop is used to repeat a specific block of code an unknown no of time
# syntax

# while condition :
#     body of while 

# example 
i = 0
while i<5:
    print(i)
    i = i+1

# write a program to count the number of digit present in a number
num = int(input("Enter Any Number : "))
count = 0
while num>0:
    num = num //10
    count = count +1
print("Total Digit :", count)

# fellow use google colab link 
# https://colab.research.google.com/drive/1skxDSTMO_UIenfMJMJpXTvd7A5WBXTOo?usp=sharing



