#print() Function in Python

#print() with one Argument
print("Hello Guys")
print("Welcome to ABC Academy !!!")
print("#$*")

#print() with Multiple Arguments
print("Hello", "Python", "3.14")

#Using sep (Separator) in print()
print("Hello", "Python", "3.13", sep="\t")

#Using end Parameter
print("Hello")
print("Guys !!!")

print("Hello", end=" ")
print("Guys!!!")

print("Hello", end="\t")
print("Guys!!!")

#Printing Variables
course = "Machine Learning"
trainer = "Srinivas"
exp = 20

print("Course:", course)
print("Trainer:", trainer)
print("Experience:", exp, "years")

print("Course:", course, "Trainer:", trainer, "Experience:", exp, "years")

#Printing Using f-strings (Recommended)
a=10
b=20
c=a+b

print("Sum of ",a, " and ",b ," is ", c)
print(f"Sum of {a} and {b} is {c}")

course = "Machine Learning"
trainer = "Srinivas"
exp = 20

print(f"Course: {course}, Trainer: {trainer}, Experience: {exp} years")

#Printing Special Characters
print("Hello\nGuys")
print("Hello\tGuys")