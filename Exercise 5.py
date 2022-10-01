import random
"""""
"""""

# Assignment 5.1

dice = int(input("How many dice do you want to roll? "))


def roll_dice(num_dice):
    rolls = 0
    for i in range(1, num_dice + 1):
        print(f"Roll #{i} = {(roll := random.randint(1, 6))}")
        rolls += roll
    return rolls


result = roll_dice(dice)
print(f"The total for {dice} rolls is {result}.")


# Assignment 5.2

print("Press 'Enter' to print the results")

number = input("Enter a number: ")
input_List = []

for x in number:
    while number != "":
        number = int(number)
        input_List.append(number)
        number = input("Enter a number: ")
        input_List.sort(reverse=True)

print(input_List[:5])

# Assignment 5.3

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

# Assignment 5.4

city_list = []
city = input("Enter a city: ")
finished_laps = 0

for x in city:
    while finished_laps <= 4:
        while city != "":
            city_list.append(city)
            city = input("Enter a city: ")
            finished_laps = finished_laps + 1
            if finished_laps >= 4:
                break

for x in city_list:
    print(x)

# print('\n'.join(map(str, city_list)))

