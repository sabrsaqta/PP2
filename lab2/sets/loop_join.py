thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


"""
Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
"""
#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #random set of elements from set1 and set2


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Note: Both union() and update() will exclude any duplicate items.

"""
Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) #apple

#The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) #apple






"""Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) #{'google', 'banana', 'microsoft', 'cherry'}

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets. 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z) #{2, 'google', 'cherry', 'banana'}
