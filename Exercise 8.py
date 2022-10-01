import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='123456',
         autocommit=True
         )

# Assignment 8.1

def geticao(ident):
    sql = "SELECT ident, name, iso_country, iso_region, municipality FROM airport"
    sql += " WHERE ident='" + ident + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            #print(result)
            print(f"{row[0]}: {row[1]} in {row[4]}, {row[3]}, {row[2]}")
    return

ident = input("Please enter an ICAO code: ")
geticao(ident)


# Assignment 8.2

def airports(country):
    sql = "SELECT ident, type, name, iso_country from airport"
    sql += " WHERE iso_country='" + country + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    result.sort(key=lambda x: x[1])
    for row in result:
        print(f"{row[3]}, {row[1]}, {row[2]}, ICAO code: {row[0]}")
    return

location = input("Please enter a country code: ")
airports(location)


# Assignment 8.3
def search_airport(icao_1, icao_2):
    airports = []
    ab = []
    sql = "SELECT ident, name, iso_country, latitude_deg, longitude_deg from airport"
    #print(sql)
    sql1 = sql + " WHERE ident='" + icao_1 + "'"
    print(sql1)
    sql2 = sql + " WHERE ident='" + icao_2 + "'"
    print(sql2)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    airports.extend(result)
    cursor.execute(sql2)
    result = cursor.fetchall()
    airports.extend(result)
    for x in airports:
        print(f"{x[0]}, {x[2]}, {x[1]}")
        n = (x[3], x[4])
        ab.append(n)
    # print(ab)
    return ab

ICAO_1 = input("Enter the ICAO of the first airport: ")
ICAO_2 = input("Enter the ICAO of the second airport: ")
ab = search_airport(ICAO_1, ICAO_2)
a = ab[0]
b = ab[1]

print(f"The distance between these two airports is {distance.distance(a, b).km:.2f} km")
