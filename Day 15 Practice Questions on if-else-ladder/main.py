# Example: Write a program to take input for marks of 5 subject and display the grade.

# 💡 HINT : Per=(total/500)*100

# If the percentage greater than 90 “Grade: A” is printed.
# If the percentage greater than 80 “Grade: B” is printed.
# If the percentage greater than 70 “Grade: C” is printed.
# If the percentage greater than 60 “Grade: D” is printed.
# otherwise , Fail is Printed.

marathi,hindi,english,math,science = input("Enter marks of 5 subject :").split()
sum = int(marathi) + int(hindi) + int(english) + int(math) + int(science)
per = (sum/500)*100
print("Percentage :",per)

if per>=90:
  print("Grade A")
elif per>=80:
  print("Grade B")
elif per>=70:
  print("Grade C")
elif per>=60:
  print("Grade D")
else:
  print("FAIL")

#   statement using condtional operators
marathi,hindi,english,math,science= input("Enter Marks of 5 Subject : ").split()
sum=int(marathi)+int(hindi)+int(english)+int(math)+int(science)
per=(sum/500)*100
print("Percentage :",per,"%")
if per>=60 and per<70:
  print("Grade D")
elif per>=70 and per<80:
  print("Grade C")
elif per>=80 and per<90:
  print("Grade B")
elif per>=90 and per<=100:
  print("Grade A")
else:
  print("FAIl")

# https://colab.research.google.com/drive/1KKgI3-QqDnRHLD3eF1eMeRC6N9u2wSnG?usp=sharing