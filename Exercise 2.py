#Assignment 2.1

name = input("What is your name ")
print("Hello, " + name + "!")

#Assignment 2.2
import math

radius = float(input("Give me the radius "))
print(f"The area is {math.pi * radius ** 2:.2f}")

#Assignment 2.3

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle"))
print(f"the perimeter of the rectangle is: {(2*length)+(2*width)}")
print(f"the area of the rectangle is: {length*width}")

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
print(f"The total is {kg_Sum} kilograms and {gram_sums:.2f} grams")

#Assignment 2.6
import random

print(f"Random number is {random.randint(0, 999):03d}")
print(f"Random number is {random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}")
