#Implicit Casting
a = 10
b = 2.5
result = a + b # Converts int to float.
print(result)
print(type(result))

#Explicit Casting
a = 9.25
b = int(a)
print(type(a))
print(type(b))

#float to int
b = int(a)
print(a)
print(type(a))
print(b)
print(type(b))

#string to int
a = "100"
b = int(a)
print(a)
print(type(a))
print(b)
print(type(b))

#boolean to int
a= True
b = int(a)
print(a)
print(type(a))
print(b)
print(type(b))

#Error Cases with int() function
#1. Non-Numeric String to Integer
a="hello123"
#b=int(a)
#2. Float String to Integer
a="9.5"
# b=int(a)
#3. None to Integer
a=None
#b=int(a)