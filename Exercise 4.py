import math
import random
"""""

# Assignment 4.1

n = 1
while n <= 1000:
    if n % 3 == 0:
        print(f"This is line {n:d}")
    n = n + 1

# Assignment 4.2

finished_runs = 0
while finished_runs >= 0:
    inch_value = int(input('Enter the value in inches: '))
    cm_value = 2.54 * inch_value
    if inch_value < 0:
        print("Invalid value!")
        break
    else:
        print('{}″ = {}cm'.format(inch_value, cm_value))
        finished_runs = finished_runs + 1

# Assignment 4.3

print("Press 'Enter' to print the results")
largest = -99999999
smallest = 99999999
while True:
    try:
        n = (input("Enter a number "))
        if n == "":
            break
        n = int(n)
        largest = n if largest < n or largest == -99999999 else largest
        smallest = n if smallest > n or smallest == 99999999 else smallest
    except:
        print("Invalid input")
        continue
print(f"Largest number is {largest}")
print(f"Smallest number is {smallest}")
"""""
# Assignment 4.4

guess = int(input("Guess a number between 1 to 10: "))
secret = random.randint(1, 10)

finished_rounds = 0
while finished_rounds >= 0:
    if guess < secret:
        print("Too low")
        guess = int(input("Guess again: "))
    elif guess > secret:
        print("Too high")
        guess = int(input("Guess again: "))
    #elif guess == secret:
    else:
        print("You guessed the number!")
        break
finished_rounds = finished_rounds + 1

# Assignment 4.5
username = "python"
password = "rules"

finished_laps = 0
while finished_laps < 5:
    user = input("Enter your username: ")
    passw = input("Enter your password: ")

    if user != username and passw != password:
        print("Sorry, your username and password are incorrect.")

    if user != username and passw == password:
        print("Sorry, your username is incorrect.")

    if user == username and passw != password:
        print("Sorry, your password is incorrect")

    elif user == username and passw == password:
        print("You've successfully logged in.")
        print(f"Welcome {user}")
        break

    finished_laps = finished_laps + 1
if finished_laps >= 5:
    print("You've entered your credentials wrong too many times!")

# Assignment 4.6

N = int(input("Enter the amount of random points you want to generate: "))
n = 0
for i in range(N):
    x = random.uniform(-1., 1.)
    y = random.uniform(-1., 1.)

    if x**2 + y**2 < 1.:
        n = n + 1
pi = 4.*n/N
print(f"Pi is {pi}, error {math.pi - pi}")

