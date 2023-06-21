# Sets :
# A set in Python is an unordered collection of unique items. It is a data type that acts like a mathematical set. It is defined by enclosing the items within curly braces {} and each item seperated by (,).

# Properties of Sets

# Unorderd :
# Unordered means that the items in a set are not stored in any particular order.

mycolors = {'sky','pink','yellow','green'}
print(mycolors)

# Unindexed :
# Unindexed means that the items in a set you can not access that items by position or index.

mycolor = {'sky','pink','yellow','green','green'}
print(mycolor)


# Unique values :
# Unique values means that the items in a set cannot contain duplicate items. If you try to add a duplicate items to a set, it will be ignored
mycolor = {'orange','sky','pink','sky','green','sky','sky'}
print(mycolor)

# Adding values to Sets
# add() method : The add() method is used to adds an element to the set. But position is not decide because set are unorderd.

mycolors = {'orange','sky','pink','sky','green'}
print("Before adding Value : ",mycolors)
mycolors.add('white')
print("After adding Value : ",mycolors)

# Remove Elements to Sets
# Hard Removal => In this case we used remove() method and it is used to remove element from the set.
# mycolors = {'orange','sky','pink','sky','green'}
# print("Brfore remove : ",mycolors)
# mycolors.remove('blue')
# print("After remove :",mycolors)

# Soft Removal => In this case we used discard() method.
mycolors = {'orange','sky','pink','sky','green'}
print("Brfore discard : ",mycolors)
mycolors.discard('blue')
print("After discard :",mycolors)

# Union of Sets
# The union() method returns a set that contains all items from the original set, and all items from the specified set.

colorList1 = {'sky','blue','white','black'}
colorList2 = {'yellow','green','red','sky'}
allElements = colorList1.union(colorList2)
print(allElements)

# Intersection of Sets
# The intersection() method returns a set that contains the similarity between two or more sets.
colorList1 = {'sky','blue','white','black'}
colorList2 = {'yellow','green','red','sky','black'}
sameElements = colorList1.intersection(colorList2)
print(sameElements)