import sqlite3
db=sqlite3.connect("C:\\Users\\Samsung\\Desktop\\17.Hafta-Odevler\\world.db")
im=db.cursor()

im.execute("""
                SELECT Name
                FROM Country
                WHERE Population > 100000000

            """)

veri=im.fetchall()
print(veri)


print("______________________________________________________")             
im.execute("""
                SELECT Name
                FROM Country
                WHERE Name LIKE '%land'
            """)

veri=im.fetchall()
print(veri)

print("______________________________________________________") 

im.execute("""
                SELECT Name
                FROM City
                WHERE Population > 500000 and Population <1000000
            """)

veri=im.fetchall()
print(veri)


print("______________________________________________________") 

im.execute("""
                SELECT Name
                FROM Country
                WHERE Continent=="Europe"
            """)

veri=im.fetchall()
print(veri)


print("______________________________________________________") 
im.execute("""
                SELECT Name
                FROM Country
                ORDER BY SurfaceArea DESC

            """)

veri=im.fetchall()
print(veri)

print("______________________________________________________") 

im.execute( """
                SELECT Name
                FROM City
                WHERE CountryCode=="NLD"
            """)

veri=im.fetchall()
print(veri)

print("______________________________________________________") 
im.execute("""
                SELECT Population
                FROM City
                WHERE Name=="Amsterdam"
            """)

veri=im.fetchall()
print(veri)

print("______________________________________________________") 
im.execute("""
                SELECT City.Name
                FROM city INNER JOIN country
                ON Country.code==City.CountryCode
                WHERE country.Continent=="Europe"
                ORDER BY city.Population DESC
                LIMIT 1
            """)

veri=im.fetchall()
print(veri)
print("______________________________________________________")

im.execute("""
            SELECT Name
            FROM Country
            WHERE Continent=='Europe'
            ORDER BY Country.SurfaceArea DESC
            LIMIT 1
            
            """)
veri=im.fetchall()
print(veri)
print("______________________________________________________")

im.execute("""
            SELECT Name
            FROM Country
            WHERE Continent=='Asia'
            ORDER BY Country.SurfaceArea DESC
            LIMIT 10

            """)
veri=im.fetchall()
print(veri)
print("______________________________________________________")

im.execute("""
            SELECT Name
            FROM Country
            ORDER BY SurfaceArea
            LIMIT 1

            """)

veri=im.fetchall()
print(veri)
print("______________________________________________________")

im.execute("""
            SELECT Name
            FROM City
            ORDER BY Population
            LIMIT 10
            
            """)

veri=im.fetchall()
print(veri)
print("______________________________________________________")

im.execute("""
            SELECT sum(Population)
            FROM Country

            """)

veri=im.fetchall()
print(veri)
print("______________________________________________________")

          
db.close()

                


