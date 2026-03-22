#input() Function in

#Taking User Input
name = input("Enter your name: ")
print("Hello ", name)

#Taking Numeric Input
# First Value
mystr = input("Enter First Value")
a = int(mystr)
print(a)

# Second Value
b = int(input("Enter Second Value"))
print(b)

sum = a+b

print("Sum is ",sum)
print(f"Sum is {sum}")

price = float(input("Enter the price: "))

print("The price is:", price)
print(f"The price is: {price}")

#Taking Multiple Inputs (Using split())
mystr1, mystr2 = input("Enter two numbers separated by space: ").split()

a=int(mystr1)
b=int(mystr2)

a,b = int(mystr1),int(mystr2) # Convert to integers

print("Sum:", a + b)
print(f"Sum: {a + b}")

x, y = input("Enter two values separated by a comma: ").split(",")

print("First:", x, "Second:", y)
print(f"First: {x}, Second: {y}")