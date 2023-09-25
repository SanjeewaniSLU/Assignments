import mysql.connector
from geopy.distance import geodesic
#1
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='pass_word',
    autocommit=True
)
def getICAOcodeairport(ident):
    sql = "SELECT name,municipality FROM airport"
    sql += " WHERE ident='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name: {row[0]} and municipality is {row[1]} .")
    return


ident = input("Enter the ICAO: ")
getICAOcodeairport(ident)

#2

def getICAOcodeairport(iso_country):
    sql = "SELECT name FROM airport "
    sql += " WHERE iso_country='" + iso_country + "'"+"Order by type"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport name: {row[0]} ")
    return

iso_country = input("Enter the Area code: ")
getICAOcodeairport(iso_country)

#3

def distance1(ident):
    sql = "select latitude_deg,longitude_deg from airport "
    sql += "where ident='"+ident+"'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location1 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is:{row[0]} and longitude is:{row[1]}")
    return location1
ident1 = input("Enter the ICAO code: ")
distance1(ident1)

def distance2(ident):
    sql = "select latitude_deg,longitude_deg from airport "
    sql += "where ident='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location2 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is:{row[0]} and longitude is:{row[1]}")
    return location2


ident2 = input("Enter the ICAO code: ")
distance2(ident2)

result1 = distance1(ident1)
result2 = distance2(ident2)

print(f"The distance is :" ,geodesic(result1, result2).km)
