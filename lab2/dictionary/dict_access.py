#access item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#get()
x = thisdict.get("model")

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change - dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change - dict_keys(['brand', 'model', 'year', 'color'])




#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change - dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change - dict_values(['Ford', 'Mustang', 2020])





#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
"""
dict_items(
    [
        ('brand', 'Ford'),
        ('model', 'Mustang'),
        ('year', 1964)
    ]
)
"""


#Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



#Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



#Check if key exists
#To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")