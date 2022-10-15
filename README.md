# Exercises

These are the exercise questions of my Python course. I will be slowly updating this page as I progress through my studies and learn new things.


[2. Variables and interactive programs](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#2-variables-and-interactive-programs)

[3. Conditional structures (if)](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#3-conditional-structures-if)

[4. While loops (while)](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#4-while-loops-while)

[5. List structures and iterative loops (for)](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#5-list-structures-and-iterative-loops-for)

[6. Functions](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#6-functions)

[7. Tuple, set, and dictionary](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#7-tuple-set-and-dictionary)

[8. Using relational databases](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#8-using-relational-databases)

[9. Fun_Game Project](https://github.com/MohamedMetropolia/Python_Coding/edit/main/README.md#9-fun_game-project)

## 2. Variables and interactive programs

1. Write a program that asks your name and then greets you by your name: Examples:
   - If you enter Viivi as your name, the program will greet you with `Hello, Viivi!`.
   - If you enter Ahmed as your name, the program will greet you with `Hello, Ahmed!`.
 
2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of 
the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). 
The program converts the input to full kilograms and grams and outputs the result to the user:
   - One talent is 20 pounds.
   - One pound is 32 lots.
   - One lot is 13,3 grams.

Example output:
```monospace
Enter talents:
3

Enter pounds:
9

Enter lots:
13.5

The weight in modern units:
29 kilograms and 545.95 grams.
```

6. Write a program that draws two random combinations of numbers for a combination lock:
   - a 3-digit code where each number is between 0 and 9.
   - a 4-digit code where each number is between 1 and 6.

## 3. Conditional structures (if)

1. Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs 
to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. 
A zander must be 42 centimeters or longer to meet the size limit.

2. Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.
You must use an if/elif/else structure in your solution.
   - LUX: upper-deck cabin with a balcony.
   - A: above the car deck, equipped with a window.
   - B: windowless cabin above the car deck.
   - C: windowless cabin below the car deck.

   If the user enters an invalid cabin class, the program outputs an error message `Invalid cabin class`.

3. Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
   - A normal hemoglobin value for adult females is between 117-155 g/l.
   - A normal hemoglobin value for adult males is between 134-167 g/l.
   
4. Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are 
also divisible by 400.

## 4. While loops (while)

1. Write a program that uses a `while` loop to print out all numbers divisible by three in the range of 1-1000.

2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

3. Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program
prints out the smallest and largest number from the numbers it received.

4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until
they guess the right number. After each guess the program prints out a text: `Too high`, `Too low` or `Correct`. 
Notice that the computer must not change the number between guesses.

5. Write a program that asks the user for a username and password. If either or both are incorrect, the program 
ask the user to enter the username and password again. This continues until the login information is correct or
wrong credentials have been entered five times. If the information is correct, the program prints out `Welcome`.
After five failed attempts the program prints out `Access denied`. The correct username is **python** and password 
**rules**.

6. Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit
circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B
is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now 
(-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction
of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of 
square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value 
of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number
of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total 
number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that
asks the user how many random points to generate, and then calculates the approximate value of pi using the method 
explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to
test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

## 5. List structures and iterative loops (for)

1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the 
the sum of the numbers. Use a `for` loop.

2. Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the 
program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted 
list items by using the `sort` method with the `reverse=True` argument.

3. Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are 
number that are only divisible by one or the number itself.
   - For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
   - On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.

4. Write a program that asks the user to enter the names of five cities one by on (use a `for` loop for reading the names)
and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line,
in the same order they were read as input. Use a `for` loop for asking the names and a `for/in` loop to iterate through the
list.

## 6. Functions

1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
Write a main program that rolls the dice until the result is 6. The main program should print out the result of 
each roll.

2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified 
function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that
the dice rolling in the main program continues until the program gets the maximum number on the dice, which 
is asked from the user at the beginning.

3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to
litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue until the user inputs a negative
value.

4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in
the list. For testing, write a main program where you create a list, call the function, and print out the value it
returned.

5. Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
the same as the original list except that all uneven numbers have been removed. For testing, write a main program 
where you create a list, call the function, and then print out both the original as well as the cut-down list.

6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of
the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for
money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices. 

## 7. Tuple, set, and dictionary

1. Write a program that asks the user for a number of a month and then prints out the corresponding season (`spring`, 
`summer`, `autumn`, `winter`). Save the seasons as strings into a tuple in your program. We can define each season to
last three months, December being the first month of winter.

2. Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out `New name` or
`Existing name` depending on whether the name was entered for the first time. Finally, the program lists out the input names
one by one, one below another in any order. Use the set data structure to store the names.

3. Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch
the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter
the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO
code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can
choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each
airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

## 8. Using relational databases

>Some users have faced surprising problems with the latest driver version 8.0.30.
>If you encounter an error message saying `mysql.connector.errors.ProgrammingError: Character set 'utf8' unsupported`,
>you can solve this by reverting to version 8.0.29:
> In PyCharm, select View/Tool Windows/Python Packages.
>Search for the mysql-connector-python package. Remove the installation of version 8.0.30 by right-clicking
> the three dots on the right and selecting Delete.
> Change the version from "Latest" to  "8.0.29" and click Install.


1. Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding
airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

2. Write a program that asks the user to enter the area code (for example `FI`) and prints out the airports located in that country
ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

3. Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two
airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using 
the `geopy` library:  https://geopy.readthedocs.io/en/stable/. Install the library by selecting **View / Tool Windows / Python Packages**
in your PyCharm IDE, write `geopy` into the search field and finish the installation.

## 9. Fun_Game Project
