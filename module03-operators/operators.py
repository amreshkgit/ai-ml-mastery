a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Arithmetic Operators - Special Cases
print(10 / 0)

# Negative Exponents
print(2 ** -3)

#Using Floats
print(5.5 + 2.3) # 7.8
print(9.7 // 2)  # 4.0
print(9.5 % 2.5) # 2.0

#Using Arithmetic Operators with Strings
print("Hello " * 5)
print("5" * "Hello ")
print(3 * "JLC " * 2 * "Hello")

str1="Hello"
str2=" JLC"
print(str1+str2)

a=5
b=2
# print("JLC " * a//b) #

print("JLC " * (a//b))

#Precedence - Arithmetic Operators

# 1) **
# 2) +x, -x
# 3) *, /, //, %
# 4) +, -

print(10 - 2 * 3)                  # 4
print(10 // 3)                    # 3
print(10 // 3 * 2)                 # 6

print(2 + 3 * 4 ** 2)             # 50
print(5 + 2 * 3 ** 2 - 4 // 2)    # 21

print(-3 ** 2)                     # -9
print((-3) ** 2)                   # 9

# Left to Right
print(2 + 3 - 2)  # 5 - 2 = 3

# Right to Left
print(2 ** 3 ** 2)   # 2 ** 9 = 512

print(8 ** 2)

#) Comparing Strings
print("apple" > "banana")
print("abcd">"abcde")  #length difference

# Comparing Boolean Values
print(True == 1)
print(True == 5)

print(False < True)
print(False > -1)

#Precedence - Relational Operators
print(5 + 2 > 3)
print(10 - 4 * 2 > 5)
print(-3 ** 2 < 0)

#Logical Operators - Examples
print(0 and 10)
print(10 and 0)
print(10 and 20)
print("Hi" and "Hello")
print("" and "JLC")
print(0 and False)
print(False and 0)

#. Relational Operators - Examples
a = 10
b = 3

print(a==b)    # Comparing Values
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#1) Comparing Same Data Types
print(10 == 10.0)

#2) Comparing Different Data Types
print("Hello" > 5) # Error

print("A" == 65)

print("65" == 65)

print("A" != 65)

print("65" != 65)

#3) Comparing Strings
print("apple" > "banana")

#4) Comparing Boolean Values
print(True == 1)
print(True == 5)

#Precedence - Relational Operators
print(5 + 2 > 3)
print(10 - 4 * 2 > 5)
print(-3 ** 2 < 0)


#Logical Operators - Examples
a=10
b=5

print(a > 5 and b < 10)
print(a > 15 or b < 10)
print(not True)
print(not False)

#Logical Operators - Special Cases
print(0 and 10)
print(10 and 0)
print(10 and 20)
print("Hi" and "Hello")
print("" and "JLC")
print(0 and False)
print(False and 0)

#Example – Using OR
print(0 or 10)
print(10 or 0)
print(20 or 10)
print("Hi" or "Hello")
print("" or "JLC")

#Example – Using NOT
# Zero and Empty valaues are Flase
print(not 0)
print(not 0.0)
print(not "")
print(not [])

# Non-Zero and Non-Empty valaues are True
print(not 99)
print(not -99)
print(not 9.9)
print(not -9.9)
print(not "Hello")
print(not [1,2,3])

#Precedence - Logical Operators
print(not True or True and True)
print((not True or True) and True)
print(not (True or True) and True)

#Assignment Operators - Examples
a=10
print(a)

a = 10
a += 3
print(a)

a = 10
a -= 3
print(a)

a = 10
a *= 3
print(a)

#Assignment Operators - Special Cases
str1 = "Hello"
str1 += " JLC"
print(str1)

# Identity Operators - Examples
a = 10
b = 10
print(a is b)
print(a is not b)

a = 257
b = 257
print(a is b)
print(a is not b)

c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)
print(c is not d)

x = "Hello123456789Hello123456789_"
y = "Hello123456789Hello123456789_"
print(x is y)
print(x is not y)

#Identity vs. Equality (is vs. ==)
#is → Checks if two variables point to the same memory address.
# == → Checks if the values are equal.

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
print(list1 is list2)

# Membership Operators - Examples
# Works with Strings

mystr = "Python is easy and fun!"

print("s" in mystr )
print("is" in mystr )

print("Python" in mystr )
print("java" in mystr ) #F
print("Fun" in mystr ) #F
print("fun" in mystr )

print("-------------")

print("Python" not in mystr ) #F
print("java" not in mystr )
print("Fun" not in mystr )
print("fun" not in mystr ) #F

#  Works with Tuples

mytuple = ("apple", "banana", "cherry")
print("banana" in mytuple)
print("grapes" in mytuple)

print("-------------")

print("banana" not in mytuple)
print("grapes" not in mytuple)
#  Works with Sets

myset  = {"red", "green", "blue"}
print("green" in myset)
print("pink" in myset)

print("-------------")

print("green" not in myset)
print("pink" not in myset)

#  Works with Dictionaries
# Only for Keys, Not Values

mydict = {"name": "Srinivas", "age": 25}

print("name" in mydict)
print("Srinivas" in mydict)

print("-------------")

print("name" not in mydict)
print("Srinivas" not in mydict)

#Bitwise Operators - Examples
# Left Shift (<<)
# Shifts bits left, multiplying by 2^n

a=31
print(a<<1);

a=31
print(a<<2);

# Right Shift (>>)
# Shifts bits right, dividing by 2^n

a=31
print(a>>1);

a=31
print(a>>2);

a=64

print(a<<3); # 64+64 = 128 +128 = 256 + 256 = 512
print(a>>3); # 64/2 = 32/2= 16/2= 8

# Bitwise AND (&)

a = 15
b = 17
print(a & b)

# Bitwise OR (|)

a = 15
b = 17
print(a | b)

# Bitwise XOR (^)

a = 15
b = 17
print(a ^ b)

# Bitwise NOT (~)
a = 15
print(~a);

b = -15
print(~b);

#Precedence - Bitwise Operators
print(10 & 6 | 3)
print(15 | 17 << 1)