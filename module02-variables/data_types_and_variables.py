import sys
x = 10
y = 9.6
name = "Srinivas"
flag = True
print(x)
print(type(x))
print(y)
print(type(y))
print(name)
print(type(name))
print(flag)
print(type(flag))

#Valid Variable Names:
my_var = 10
_var = "Hello"
age123 = 25
print(my_var)
print(_var)
print(age123)

#Invalid Variable Names:
#2name = "John"
#my-variable = 5
#class = "Python"

#Multiple Ways to use Variables
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

#Same value for multiple variables
x=y=z=50
print(x)
print(y)
print(z)

#Swwapping two variables
a,b=5,10
print(a)
print(b)
a,b=b,a
print(a)
print(b)

#Deleting a Variable
x=10
print(x)
del x
#print(x)

#How to get size of variable?
a=12345
print("size of a: ",sys.getsizeof(a))
b="hi"
print(sys.getsizeof(b))
x=9.99
print(sys.getsizeof(x))
y=True
print(sys.getsizeof(y))

#How to get the addresses of variables?
a=10
print("address of a:",id(a))
b=10
print("address of b:",id(b))

#Python doesn’t have built-in constant variables,
#but by convention, we use UPPERCASE_NAMES for constants.
#Constants Are Not Truly Constant in Python.

#Exploring int (Integers)
#int data type is used to store whole numbers (positive or negative).
#No size limit (depends on system memory).

a = 10
b = -20
c = 0
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#Exploring float
a = 9.5
b = -2.6
c = 0.0
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#We Can represent very large or very small numbers using scientific notation
num1 = 1.5e5
num2 = 2.5e-4
print(num1)
print(type(num1))
print(num2)
print(type(num2))

#Checking Float Object Reusability
a = 9.5
print(id(a))
b = 9.5
print(id(b))
print(a is b)

#Exploring bool (Booleans)
x = True
y = False
print(x)
print(type(x))
print(y)
print(type(y))

#Checking Boolean Object Reusability
a = True
print(id(a))
b = True
print(id(b))
c = False
print(id(c))
print(a is b)
print(a is c)

#Exploring NoneType (None)
#None represents the absence of a value or a null value in Python.
# It is a built-in constant that is used when a variable has no assigned value.
# None is not the same as 0, False, or an empty string ("").
# Used to indicate missing values or functions with no return value.

#Ex:
x = None
print(x)
print(type(x))

#Checking NoneType Object Reusability

a = None
print(id(a))
b = None
print(id(b))
print(a is b)