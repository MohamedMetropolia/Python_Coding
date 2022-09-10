"""""
"""""
# Assignment 3.1

length = float(input("What is the length of your zander in centimeters: "))
zander = 42
if length <= 42:
    print("Your zander is not big enough, please release it back into the lake.")
    print(f"Your zander is {zander - length:.0f} centimeters short of the size limit.")
else:
    print("Congrats, your zander meets the size limit!")
"""""
# Assignment 3.2

print("Please choose between the following cabin classes:")
cabinclass = input("LUX, A, B or C class: ")
if (cabinclass == "LUX") or (cabinclass == "lux"):
    print("upper-deck cabin with a balcony.")
elif (cabinclass == "A") or (cabinclass == "a"):
    print("above the car deck, equipped with a window.")
elif (cabinclass == "B") or (cabinclass == "b"):
    print("windowless cabin above the car deck.")
elif (cabinclass == "C") or (cabinclass == "c"):
    print("windowless cabin below the car deck.")
else:
    print("invalid cabin class")

# Assignment 3.3

gender = input("Please enter your biological gender: ")
hemoglobin = int(input("Please enter your hemoglobin value: "))

if (gender == "male") or (gender == "Male"):
    if 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    elif hemoglobin > 167:
        print("Your hemoglobin value is too high.")
    elif hemoglobin < 134:
        print("Your hemoglobin value is too low.")

if (gender == "female") or (gender == "Female"):
    if 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    elif hemoglobin > 155:
        print("Your hemoglobin value is too high.")
    elif hemoglobin < 117:
        print("Your hemoglobin value is too low.")

# Assignment 3.4

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("is a leap year".format(year))

elif (year % 4 == 0) and (year % 100 != 0):
    print("is a leap year".format(year))

else:
    print("is not a leap year".format(year))
"""""
