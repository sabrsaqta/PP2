#Access Items
#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

"""
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # cherry

"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#['cherry', 'orange', 'kiwi']
                    #    2         3        4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # apple banana cherry orange (kiwi not included)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #cherry orange kiwi melon mango

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #orange kiwi melon (mango not included)

#Check if Items are in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")




