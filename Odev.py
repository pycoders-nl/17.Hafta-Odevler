import sqlite3 as sql
db = sql.connect('world.db')
print('Database baglandi..')

print("------------------------------------------")

im = db.cursor()


# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?

im.execute("""
            SELECT Name
            FROM country
            WHERE Population > 100000000
""")
veriler = im.fetchall()
print("1. Nufusu 100 milyonun uzerinde olan ulkeler:")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?

im.execute("""
            SELECT Name
            FROM country
            WHERE Name LIKE '%land%' 
""")
veriler = im.fetchall()
print("2. Isminin sonunda “land” kelimesi gecen ulkeler;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?

im.execute("""
            SELECT Name, Population
            FROM country
            WHERE Population > 500000 and Population <1000000
""")
veriler = im.fetchall()
print("3. 500 bin ile 1 milyon arasinda nufusu olan sehirler;")
for i in veriler:
    print(i[0],' - ',i[1])

print("------------------------------------------")

# 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.

im.execute("""
            SELECT Name
            FROM country
            WHERE Continent == "Europe"
""")
veriler = im.fetchall()
print("4. Avrupa (“Europe”) kitasinda bulunan ulkelerin tamami ;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.

im.execute("""
            SELECT Name
            FROM country
            ORDER BY SurfaceArea DESC
""")
veriler = im.fetchall()
print("5. Yuzolcumleri buyukten kucuge tum ulkeler ;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.

im.execute("""
            SELECT Name
            FROM city
            WHERE CountryCode == "NLD"
            ORDER BY Name
""")
veriler = im.fetchall()
print("6. Hollanda’nin (Netherlands) tum sehirleri ;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 7- Amsterdam’in nufusu kactir?

im.execute("""
            SELECT Population
            FROM city
            WHERE CountryCode == "NLD" and Name == "Amsterdam"            
""")

veriler = im.fetchall()
print("7. Amsterdamin nufusu {} dir".format(veriler[0][0]))

print("------------------------------------------")

# 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?

im.execute("""
            SELECT city.Name,city.Population
            FROM city city
            INNER JOIN country country
            ON city.CountryCode = country.Code
            WHERE country.Continent == "Europe"
            ORDER BY city.Population DESC                       
""")

veriler = im.fetchall()
print("8. Avrupa’nin en kalabalik sehri {}. Nufusu {}.".format(veriler[0][0], veriler[0][1]))

print("------------------------------------------")

# 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?

im.execute("""
            SELECT Name
            FROM country
            WHERE Continent == "Africa"
            ORDER BY SurfaceArea DESC                      
""")

veriler = im.fetchall()
print("9. Afrika kitasinin yuzolcumu en buyuk ulkesi: {}".format(veriler[0][0]))

print("------------------------------------------")

# 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?

im.execute("""
            SELECT Name
            FROM country
            WHERE Continent == "Asia"
            ORDER BY SurfaceArea DESC 
            LIMIT 10                       
""")

veriler = im.fetchall()
print("10. Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke ;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.

im.execute("""
            SELECT Name,SurfaceArea
            FROM country
            ORDER BY SurfaceArea                       
""")

veriler = im.fetchall()
print("11. Yuzolcumu en kucuk olan ulke: {}. Yuzolcumu: {} km2.".format(veriler[0][0],veriler[0][1]))


print("------------------------------------------")

# 12- En kalabalik 10 sehri bulunuz.

im.execute("""
            SELECT Name,Population
            FROM city
            ORDER BY Population DESC
            LIMIT 10                       
""")

veriler = im.fetchall()
print("12. En kalabalik 10 sehir ;")
for i in veriler:
    print(i[0])

print("------------------------------------------")

# 13- Dunyanin nufusunu hesaplayiniz.

im.execute("""
            SELECT SUM(Population)
            FROM country
                             
""")

veriler = im.fetchall()
print("13. Dunyanin nufusu: {}".format(veriler[0][0]))
