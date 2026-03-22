#A) for Loop

#Example 1:

# print the numbers from 0 to 4
for x in range(5):
    print(x)

# Example 2:

# print the numbers from 1 to 5
for x in range(1,6):
    print(x)

# Example 3:
# print the elements of list

mylist = [10,20,30,40,50]

for x in mylist:
    print(x,end="\t")

# Example 4:

# print the elements of set

myset = {10,20,30,40,50}

for x in myset:
  print(x,end="\t")

# Example 5:
# print each character of string

mystr = "Python"

for ch in mystr:
    print(ch)

#B) while Loop

# Print numbers from 1 to 5
i = 1

while i <= 5:
    print(i)
    i = i + 1

# Example 2:

# Print numbers from 5 to 1
i = 5

while i >= 1:
    print(i)
    i = i - 1

#Looping Statements with else
for i in range(1,6):
    print(i)
else:
    print("Loop finished successfully!")

# Example 2: for loop with else (With break)

for i in range(1,6):
    print(i)
    if i == 3:
        break
else:
    print("Loop finished successfully!")

# Example 3: while loop with else (No break)

x = 1

while x <= 5:
    print(x)
    x += 1
else:
    print("While loop completed!")

# Example 4: while loop with else (With break)

x = 1

while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1
else:
    print("While loop completed!")


#4.7. Loop Control Statements
# Example 1

for i in range(5):
    break
    print(i)

# Example 2

for i in range(5):
    if i == 3:
        break
    print(i)

#B) continue Statement
# Example 1
for i in range(5):
    continue
    print(i)

print("Done")

# Example 2
for i in range(5):
    if i == 3:
        continue
    print(i)

#C) pass Statement
# Example 1
for i in range(5):
    pass
    print(i)

# Example 2
for i in range(5):
    if i == 3:
        pass
    print(i)

#Exploring the range() Function
# 1. range(stop) → Starts from 0

for i in range(5):
    print(i)

# 2. range(start, stop) → Custom Start

for i in range(2, 6):
    print(i)

# 3. range(start, stop, step) → Custom Step

for i in range(1, 10, 2):
    print(i)

# 4. Using range() with Negative Step (Reverse Order)

for i in range(5, 0, -1):
    print(i)

# 5. Using range() with for Loop and else

for i in range(3):
    print(i)
else:
    print("Loop completed!")


# Important Note:
# Q) What is the retur type of range() function?
# Ans: range object

x = range(5)
print(type(x))

print(x)

# To convert into a list:
print(list(range(5)))   # [0, 1, 2, 3, 4]

#4.9. Exploring Nested Loops in Python
# Example 1: Iterating Through a Matrix

matrix = [
    [10, 20, 30],
    ["a", "b", "c"],
    [70, 80, 90]
]

for mylist in matrix:
    # Prints elements of each list
    for x in mylist:
        print(x, end="\t")

    # Move to next line after each row
    print()

# Example 2: Printing Star Pattern

rows = 10

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="  ")

    print()

# Example 3: Printing Number Pattern

rows = 10

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
