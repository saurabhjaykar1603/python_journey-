# Properties Of Tuple
# Ordered :
# Tuples are an ordered sequences of items, just like lists.

# Unchangeable :
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates :
# tuples are indexed, they can have items with the same value.

# Manipulation of Tuple Example
fastfood = ("Vadapav","Pizza","Burger","Dosa","PaniPuri")
listfastfood = list(fastfood)
listfastfood[1] = "Edli"
fastfood = tuple(listfastfood)
print(fastfood)