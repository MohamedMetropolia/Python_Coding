import random

# print("I am a Princess")
# print("You are a Princess")
# print("This text was written by a Princess")

# print(2+3)
# print(6+7*2)

# sur_name = input("What is your surname? ")
# print("Hello " + sur_name)
"""""
first_name = "Mohamed "
sur_name = "el Allati"
full_name = first_name + "" + sur_name
print(full_name)
"""""
"""""
name = input("What is your name?")
print(name)
name = name + " el Allati"
print(name)
"""""

"""""
number1 = 10
number2 = "10"
print(number1)
print(number2)
"""""

"""""
number = 10
print(number / 2)
"""""
"""""
number = 10
print("This is the number" + " " + str(number))
"""""

"""""
number = 1/53
print(f"This is the result {number:.2f}")
#print(f"The number is", number)
"""""

"""""
weight = float(input("weight in pounds:"))
print(f" The Weight in kilograms {weight * 0.453:.2f}")

#kilograms = weight * 0.453592
#print(f"The weight in kilograms is {kilograms:.2f}")

weight = float(input("weight in kilograms"))
print(f"Weight in pounds is {weight * 2.20:.2f}")
"""""

"""""
#Assignment 2.1

name = input("What is your name")
print("Hello, " + name + "!")
"""""

"""""
#Assignment 2.2
import math

radius = float(input("Give me the radius "))
print(f"The area is {math.pi * radius ** 2:.2f}")
"""""
"""""
#Assignment 2.3

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle"))
print(f"tge perimeter of the rectangle is: {(2*length)+(2*width)}")
print(f"tge area of the rectangle is: {length*width}")

#Assignment 2.4

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))
number3 = float(input("Enter a third number: "))
sum = number1+number2+number3
print(f"The sum of your numbers is {sum}")
print(f"The product of your numbers is {number1*number2*number3}")
print(f"The average of your numbers is {sum/3}")

#Assignment 2.5
Talent = float(input("How many talents? "))
Pound = float(input("How many pounds? "))
Lot = float(input("How many lots? "))
Talent_kg = (Talent*8.512)
Pound_kg = (Pound*0.4256)
Lots_kg = (Lot*0.0133)
kg_Sum = int((Talent_kg+Pound_kg+Lots_kg))
gram_sums = ((Talent_kg+Pound_kg+Lots_kg-kg_Sum)*1000)
print(f"The total is {kg_Sum} kilograms and {gram_sums:.4f} grams")

#Assignment 2.6
import random

print(f"Random number is {random.randint(0, 999):03d}")
print(f"Random number is {random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}")
"""""
"""""
rounds = int(input("How many greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good morning")
    finished_rounds = finished_rounds + 1
"""""
"""""
n = 1
while n <= 1000:
    if n % 3 == 0:
        print(f"This is a line {n:d}")
    n = n + 2
"""""
"""""
n = 1
largest = 0
smallest = 99999999
while n < 1000:
    user = print(input("Enter a number: "))
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
    elif n == 5 :
        break
"""""
"""""
number = int(input("Enter a number: "))
fact = number
if number <= 0:
    print("Thanks and bye")

else:
    for i in range(1, number):
        fact = fact * i

print(f"The factorial of {number} is {fact}")
"""""

sum = 0
numberOfDice = int(input("Input the number of dice: "))
for dice in range(1, numberOfDice+1):
    dice = random.randint(1, 6)
    print(dice)
    sum = sum + dice

print(f"The total sum is {sum}")



