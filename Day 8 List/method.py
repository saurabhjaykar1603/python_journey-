# Append
# The append() method adds an element to the end of the list.courses = ["c","c++","python","java","icp"]
courses = ["c","c++","python","java","icp"]
print("Before append :",courses)
courses.append("Android Dev")
print("After append :",courses)

# Remove
# The remove() method removes the specified item in the lists.
fruits = ['appple','banana','orange','cherry']
print("Before remove",fruits)
fruits.remove('banana')
print("After remove",fruits)


# Pop
# The pop() method remove the element. It takes a single argument (index).

fruit = ['appple','banana','orange','cherry']
print("Before pop",fruit)
fruit.pop(2)
print("After pop",fruit)

#Delet
#The delete() method delete elements from the specified index.

color = ["red","Green","Blue","orange"]
print("Before delete : ",color)
del color[1]
print("After delete :",color)

# Clear
# The clear() method removes all the elements from the list.

cars = ["Thar", "Honda City","BMW","Skoda","Farari"]
print("Before clear :",cars)
cars.clear()
print("After clear : ",cars)


# Sort
# In Python, the sort() method is used to sort a list in-place, meaning it modifies the original list directly. It arranges the elements of the list in either ascending or descending order, depending on the arguments provided.

# Ascending Order
# To sort the list in ascending order, we simply call the sort() method on the list without passing any arguments or by passing reverse=False explicitly. Here's the

alphabets = ['A','Z','C','V','P','R']
alphabets.sort()
print(alphabets)

# Descending Order
# To sort the list in descending order, we pass reverse=True as an argument to the sort() method. Here's the code:

num = ['1','2','3','5','4']
num.sort(reverse=True)
print(num)