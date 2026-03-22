#If Statement
# Example 1:

age = 25
print("Start")
if age >= 18:
  print("You are eligible to vote.")
  print("Come to Vote.")

print("End")


#Example 2

age=25
if age >= 18:
    print("You are eligible to vote.")
    print("You can Vote")
print("Ok Done!!!")

#If-Else Statement
a = 100
b = 20
if a > b:
    max = a
    print("If block")
    print("If block")
    print("If block")
else:
    max = b
    print("else block")
    print("else block")
    print("else block")

print("Max is",max)

# Example 2

marks = 45
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Example 3:

marks = 80

if marks >= 75:
    print("Pass")
    print("Goto Next Class")
else:
    print("Fail")
    print("Sit in same Class")

print("All Done")

#Example
maths=95
science=85
social = 93

if maths >= 90 and (science >=90 or science >=90):
    print("You are eligible for award")
else:
    print("You not are eligible for award")

#if-elif-else statement

# Example 1:

marks = 90

if marks >= 90:
    print("Grade - A")
elif marks >= 80:
    print("Grade - B")
elif marks >= 70:
    print("Grade - C")
elif marks >= 60:
    print("Grade - D")
else:
    print("Grade - E")


#Ternary Operator
a=500
b=200
maxx = a if a > b else b
print("Max is",maxx)

# Example 2
num =16
res = "Even" if num%2==0 else "Odd"
print(res)

#Example 3
amount = 3000
discount= "You can discount" if num > 2500 else "No discount"
print(discount)

#Example 3
num = -5
result = "+ve" if num > 0 else "-ve"
print(result)

# Nested If
maths = 85
science = 85
social = 93

if maths >= 90:
    if science >= 90 or social >= 90:
        print("You are eligible for award")
    else:
        print("You not are eligible for award")
else:
    print("You are not eligible for any award")


#match case ( Python Version - 3.10)
httpCode = 800

match httpCode:
    case 200:
        print("Ok")
    case 404:
        print("Status File Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("unknown status code")

# Example 2 – Multiple Value Matching Using |

num = 6

match num:
    case 1 | 3 | 5 | 7 | 9:
        print("Odd Number")
    case 2 | 4 | 6 | 8:
        print("Even Number")

# Example 3 –  Guard Condition (Even / Odd)

num = 9

match num:
    case x if x % 2 == 0:
        print("Even Number")
    case x if x % 2 != 0:
        print("Odd Number")

# Example 4 –  Guard Condition (Positive / Negative / Zero)

num = -10

match num:
    case x if x == 0:
        print("Zero")
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")

# Example 5 – Tuple Pattern Matching

order_status = "cancelled"
payment_status = "paid"

match (order_status, payment_status):
    case ("confirmed", "paid"):
        print("Prepare the order for shipment")
    case ("confirmed", "pending"):
        print("Wait for payment confirmation")
    case ("cancelled", _):
        print("Order is cancelled")
    case _:
        print("Check order details")

