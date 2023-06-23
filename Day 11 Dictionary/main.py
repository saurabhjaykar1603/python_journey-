# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs.
phoneBook = {
    "Dolly" : "1234567890",
    "Anu" : "9876543210",
    "Avinash" : "21323422222",
    "Pooja" : "878975457"
}
print(phoneBook)

# Example by using get() method :

# The code defines a dictionary named phoneBook which contains key-value pairs where each key represents a name and each value represents a phone number. The code then prints in a formatting way the value associated with the key "Anu" using a dictionary.

phoneBook = {
    "Dolly" : "1234567890",
    "Anu" : "9876543210",
    "Avinash" : "21323422222",
    "Pooja" : "878975457"
}
print(phoneBook.get("Avinash"))

# Example by using get() method with the help of input:

# following code use by Google Collab 
# https://colab.research.google.com/drive/12DXICRgOye0tdsMbC_sNxE9jc52AQCP7?usp=sharing


# fruitsNameToImage = {
#     'Apple' : '🍎',
#     'Graphs' : '🍇',
#     'Banana' : '🍌',
#     'Orange' : '🍊',
#     'Cherry' : '🍒'
# }
# fruitKey = input("Enter fruit Name : ")
# image =fruitsNameToImage.get(fruitKey)
# print("{} Looks Like {}".format(fruitKey,image))



# The code defines a dictionary named courses which contains key-value pairs where each key represents the name of a course and each value represents its price. The code then uses the keys() method of the courses dictionary to retrieve a list of all the keys in the dictionary.
courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses.keys())

# The code defines a dictionary named courses which contains key-value pairs where each key represents the name of a course and each value represents its price. The code then uses the values() method of the courses dictionary to retrieve a list of all the values in the dictionary.
print(courses.values())


# Adding New Key 

# The code defines a dictionary named courses which contains key-value pairs where each key represents the name of a course and each value represents its price. In the above example, we can add a new course and the new course is Java and print a directory in next time.

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses)
courses["Java"] = "499"
print(courses)


# Update Key :

# The code defines a dictionary named courses which contains key-value pairs where each key represents the name of a course and each value represents its price. In the above example, we can update a Python value and print a directory in next line.

courses ={
    "C" :"499",
    "C++" :"499",
    "Python" :"499",
    "DSA" :"999",
    "ICP" :"999",
    "ICGP" :"10,000"
}
print(courses)
courses["Python"] = "999"
print(courses)