print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

#Checking string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Slicing Strings
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5]) #till 5th not included

b = "Hello, World!"
print(b[2:]) #from 2nd to end

"""
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2]) #result: "orl" (-2nd is not included)



#Modifying Strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

#removing whitespaces from start/end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items.
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, I am " + age #wrong
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.

#with indexes
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #quantity - 0, itemno - 1, price - 2

#escape char
txt = "We are the so-called "Vikings" from the north." #wrong

txt = "We are the so-called \"Vikings\" from the north." #correct

#Exercises
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
