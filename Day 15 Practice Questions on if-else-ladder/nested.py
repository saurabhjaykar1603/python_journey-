# Nested if
# A nested if is a flow control statement that’s the target of another if-statement. By nested-if statements, we mean to use an if-statement inside another if-statement.
# if condition-1:
# if condition-2:
#   if condition-n:
#     statement-1
#     statement-2

#     statement-n

jee = 110
hsc = 50

if hsc>60:
  print("Congrats you clear HSC")
  if jee>120:
    print("Admmision Granted ")
  else:
    print("Sorry you did not cleared JEE")
else:
  print("Sorry You need to imporoved your HSC Score")

#   Sorry You need to imporoved your HSC Score

# # The code checks if a student has cleared their HSC with a score greater than 60. If they have, it checks if their JEE score is greater than 120. If it is, the program prints "Admission Granted". If the HSC score is less than or equal to 60, the program prints "Sorry You need to imporoved your HSC Score". If the JEE score is less than or equal to 120, the program prints "Sorry you did not cleared JEE".