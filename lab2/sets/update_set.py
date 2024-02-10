#Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add set to set using update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#you can add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove items
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Note: If the item to remove does not exist, discard() will NOT raise an error.




"""
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

"""

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#Clear set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#delete set
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

