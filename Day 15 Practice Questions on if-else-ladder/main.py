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