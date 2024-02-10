thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #apple blackcurrant watermelon orange kiwi mango

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #apple blackcurrant watermelon cherry

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #apple watermelon

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #watermelon takes index 2 - apple banana watermelon cherry


#Add items to list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")                       #ADD at index - insert(index, element)
print(thislist)                                    #ADD in the end - append()
                                                   #ADD iterable - extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #list1 + list2

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #extend() method can also add tuples, sets, dictionaries


#Remove items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:                                #REMOVE item - remove()
thislist = ["apple", "banana", "cherry"]                                          #REMOVE by index - pop()
del thislist[0]                                                                   #REMOVE by index/entire list - del list[i]/del list
print(thislist)                                                                   #CLEAR list - clear()

thislist = ["apple", "banana", "cherry"]
del thislist #deletes entire list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #make list clear



