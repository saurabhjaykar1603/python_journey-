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