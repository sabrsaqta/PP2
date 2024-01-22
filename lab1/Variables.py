#Variables
x = 5
y = "Hello, World!"

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#legal examples
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal examples
2myvar = "John"
my-var = "John"
my var = "John"

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#assigning multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#Error
x = 5
y = "John"
print(x + y)

x = 5
y = "John"
print(x, y)

#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Global and local
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#changing global variable inside function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Exercises
carname = 'Volvo'
x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x+y
print(z)

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"

def myfunc():
  global x
  x = "fantastic"

