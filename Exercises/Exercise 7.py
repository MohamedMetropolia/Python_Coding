# Assignment 7.1
"""
Winter = [12, 1, 2]
Spring = [3, 4, 5]
Summer = [6, 7, 8]
Autumn = [9, 10, 11]
month_list = (Winter, Spring, Summer, Autumn)
month = int(input("Please enter the number of a month: "))

if month in month_list[0]:
    season = "winter"
elif month in month_list[1]:
    season = "Spring"
elif month in month_list[2]:
    season = "Summer"
elif month in month_list[3]:
    season = "Autumn"
else:
    print("That is not a month!")

print(f"The season is {season}")
"""
"""
name = input("Enter a name: ")
name_list = set()
while name != "":
    for x in name:
        name_list.add(name)
        name = input("Enter a name: ")
        if name in name_list:
            print("existing name")
        elif name == "":
            break
        else:
            print("New name!")
            name_list.add(name)

print(name_list)
"""
# Assignment 7.3

question = input("Type 'New' to enter a new airport. "
                 "Type 'Fetch' to fetch the information of an existing airport. "
                 "Type 'Exit' to exit ")

airport = {}
while True:
    if question == "New".lower():
        name = input("Enter the name of the airport: ")
        icao = input("Enter the corresponding ICAO code: ")
        airport[icao] = name

        def add_airport(airport: list, name: str, icao: str):
            link = {"name": name, "icao": icao}
            airport.append(link)
            add_airport(airport, name, icao)
        question = input("Type 'New' to enter a new airport. "
                         "Type 'Fetch' to fetch the information of an existing airport. "
                         "Type 'Exit' to exit ")

    elif question == "Fetch".lower():
        print(airport)
        search = input("Enter the ICAO code of the airport you want to search: ")
        if search in airport:
            print(airport[search])
        question = input("Type 'New' to enter a new airport. "
                         "Type 'Fetch' to fetch the information of an existing airport. "
                         "Type 'Exit' to exit ")

    elif question == "Exit".lower():
        print("Bye!")
        break

