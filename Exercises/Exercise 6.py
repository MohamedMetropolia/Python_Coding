import random
import math

"""
# Assignment 6.1


def main():
    x = 0
    while True:
        min_dice = 1
        max_dice = 6
        roll = random.randint(min_dice, max_dice)
        x += 1
        print(f"Dice #{x} = {roll}")
        if roll == 6:
            print("You have rolled a six!")
            break


main()

# Assignment 6.2
sides = int(input("How many sides on a dice? "))
dice = int(input("What is the number you want to roll: "))


def main(sides):
    x = 0
    while True:
        min_dice = 1
        max_dice = sides
        if dice >= sides:
            print("Your die doesn't have that many sides")
            break
        roll = random.randint(min_dice, max_dice)
        x += 1
        print(f"Dice #{x} = {roll}")
        if roll == dice:
            print(f"You have rolled {dice} on a {sides}-sided die!")
            break


main(sides)


# Assignment 6.3


def conversions():
    liters_per_gallon = 3.785411784
    finished_laps = 0
    while finished_laps >= 0:
        volume = int(input("Enter the volume in gallons: "))
        conversion = volume * liters_per_gallon
        if volume < 0:
            print("Invalid value!")
            break
        else:
            print(f"{volume} gallons is {conversion:.3f} liters ")


conversions()

# Assignment 6.4

number_list = []


def sum_of_list(number_list):
    number_list.append([1, 4, 2, 8, 4, 9, 5])
    total = 0
    for i in number_list:
        total += i
    return total


print(sum(number_list))

# Assignment 6.5

num_list = []
even_num = []

add_num = input("Please enter a number to add to the list: ")
while add_num != "":
    num_list.append(int(add_num))
    add_num = input("Please enter a number to add to the list: ")
    if add_num == "":
        print(f"The original numbers are: {num_list} ")
        break

def num_for_list(original):
    for x in original[:]:
        if x % 2 != 0:
            original.remove(x)
    even_num.append(original)
    print(f"The even numbers are: {even_num}")
    return

def s_of_list(integers):
    print(f"The sum is: {sum(integers)}")
    return

num_for_list(num_list)
s_of_list(num_list)
"""
# Assignment 6.6

dia_pizza = float(input("What is the diameter of the first pizza in cm? "))
price_pizza = float(input("What was the price of the first pizza? "))
dia_pizza2 = float(input("What is the diameter of the second pizza in cm? "))
price_pizza2 = float(input("What was the price of the second pizza? "))

def first_pizza(diameter, price):
    radius1 = (diameter / 100) / 2
    pizza_time = (radius1 ** 2) * math.pi
    final = price / pizza_time
    return final
def second_pizza(diameter1, price2):
    radius2 = (diameter1 / 100) / 2
    pizza_time2 = (radius2 ** 2) * math.pi
    s_p = price2 / pizza_time2
    return s_p

if first_pizza(dia_pizza, price_pizza) < second_pizza(dia_pizza2, price_pizza2):
    print("The first pizza is cheaper")
elif first_pizza(dia_pizza2, price_pizza) > second_pizza(dia_pizza2, price_pizza2):
    print("The second pizza is cheaper")
else:
    print("They are both the same price")

first_pizza(dia_pizza, price_pizza)
print(f"The price per square meter is {first_pizza(dia_pizza, price_pizza):.2f} euros")
second_pizza(dia_pizza2, price_pizza2)
print(f"The price per square meter is {second_pizza(dia_pizza2, price_pizza2):.2f} euros")

