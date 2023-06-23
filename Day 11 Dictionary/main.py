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