import sqlite3
con = sqlite3.connect("world.db")
im = con.cursor()
print("1- Nufusu 100 milyonun uzerinde olan ulkeler : ")
im.execute("""SELECT Name
            FROM country
            WHERE 100000000 < Population

""")


veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3
print("2- Isminin sonunda “land” kelimesi gecen ulkeler:")
im.execute("""SELECT Name
            From city
            WHERE Name LIKE '%land'
""")

veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3

print("3- 500 bin ile 1 milyon arasinda nufusu olan sehirler: ")
im.execute("""SELECT Name
            From city
            WHERE 500000<Population<1000000

""")

veriler = im.fetchall()
print(veriler)
con.commit()
###########################################################################################################3
print("4-Avrupa ('Europe') kitasinda bulunan ulkelerin tamami ")
im.execute("""SELECT Name
            From country
            WHERE Continent LIKE '%Europe%'
""")
veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3

print("5-Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.")
im.execute("""SELECT Name
           From country
            ORDER BY SurfaceArea
""")
veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3

print("6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz. ")
im.execute("""SELECT Name
            FROM city
            WHERE CountryCode = 'NLD'""")

veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3

print("7- Amsterdam’in nufusu:")

im.execute("""SELECT Population
            FROM city
            WHERE Name = "Amsterdam"
""")
veriler = im.fetchall()
print(veriler)
con.commit()

###########################################################################################################3

print("8-Avrupa’nin (Europe) en kalabalik sehri")

im.execute("""SELECT City.Name,City.Population
            FROM city
            INNER JOIN Country country
            ON city.CountryCode = Country.Code
            WHERE Country.Continent = 'Europe'
            ORDER BY city.Population DESC
            """)
veriler = im.fetchone()
print(veriler)
con.commit()

###########################################################################################################3

print("9-Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi:")

im.execute("""SELECT  Name
            FROM country
            WHERE Continent = 'Africa'
            Order By SurfaceArea DESC

""")

veriler = im.fetchone()
print(veriler)
con.commit()

###########################################################################################################3

print("10-Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke:")

im.execute("""SELECT  Name
            FROM country
            WHERE Continent = 'Asia'
            Order By SurfaceArea DESC """)

veriler = im.fetchmany(10)
print(veriler)
con.commit()




###########################################################################################################3

print("11-Yuzolcumu en kucuk olan ulke: ")

im.execute("""SELECT Name
            FROM country
            Order By SurfaceArea
""")

veriler = im.fetchone()
print(veriler)
con.commit()


###########################################################################################################3

print("12-En kalabalik 10 sehir:")

im.execute("""SELECT Name
            FROM city
            Order By Population DESC
""")


veriler = im.fetchmany(10)
print(veriler)
con.commit()

###########################################################################################################3

print("13-Dunyanin nufusunu hesaplayiniz")

im.execute("""SELECT SUM(Population)
            FROM country;
""")

veriler = im.fetchone()
print(veriler)
con.commit()

###########################################################################################################3
