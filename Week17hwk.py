# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
import sqlite3

db = sqlite3.connect('C:\\Users\\Beyza\\Desktop\\17.Hafta-Odevler\\world.db') #databasee bagalndi

im = db.cursor() #burada imlec olusturmusum
sql = """SELECT name FROM country WHERE population > 100000000"""
im.execute(sql)
records = im.fetchall()
print("Total rows are:  ", len(records))
for row in records:
    print("Name: ", row[0])


# # 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
print("______________________________________________________________________________________")

sql2 = """SELECT name FROM country WHERE name LIKE '%land'"""
im.execute(sql2)

records2 = im.fetchall()
for row in records2:
    print("Name: ", row[0])

# # 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
print("______________________________________________________________________________________")

sql3 = """SELECT name FROM city WHERE population >500000 AND Population < 1000000"""
im.execute(sql3)
records3 = im.fetchall()
for row in records3:
    print("Name: ", row[0])

# # 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
print("______________________________________________________________________________________")

im.execute("""SELECT name FROM country WHERE Continent = 'Europe'""")
records4 = im.fetchall()

for row in records4:
    print("Name: ", row[0])


# # 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
print("______________________________________________________________________________________")
im.execute("""SELECT name, Surfacearea FROM Country ORDER BY Surfacearea DESC""")
records5 = im.fetchall()

for row in records5:
    print("Name: ", row[0], "Surface: ", row[1])

# # 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
print("______________________________________________________________________________________")
im.execute("""SELECT name FROM city WHERE countrycode = 'NLD'""")
records6 = im.fetchall()
for row in records6:
    print("Name: ", row[0])

# # 7- Amsterdam’in nufusu kactir?
print("______________________________________________________________________________________")
im.execute("""SELECT population FROM city WHERE name = 'Amsterdam'""")
records7 = im.fetchall()
for row in records7:
    print("Population: ", row[0])


# # 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
print("______________________________________________________________________________________")

im.execute("""SELECT city.name FROM city inner join country  on country.code = city.CountryCode where
country.Continent = 'Europe'
order by city.Population desc LIMIT 1""")
records8 = im.fetchall()
for row in records8:
    print("Cityname: ", row[0])


# # 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
print("______________________________________________________________________________________")

im.execute("""SELECT name FROM country WHERE continent = 'Africa' order by SurfaceArea desc LIMIT 1""")
records9 = im.fetchall()
for row in records9:
    print("Name: ", row[0])

# # 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
print("______________________________________________________________________________________")
im.execute("""SELECT name, Surfacearea FROM country WHERE continent = 'Asia' ORDER BY Surfacearea DESC LIMIT 10""")  #once where kosulunu sonra siralayi yaz

records10 = im.fetchall()
for row in records10:
    print("CountryName: ", row[0], "Surfacearea: ", row[1])


# # 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
print("______________________________________________________________________________________")
im.execute("""SELECT min(SurfaceArea),name  FROM Country""")
records11 = im.fetchall()
for row in records11:
    print("Smallestsurfacearea: ", row[0])



# # 12- En kalabalik 10 sehri bulunuz.
print("______________________________________________________________________________________")
im.execute("""SELECT name FROM city ORDER BY population DESC LIMIT 10""")
records12 = im.fetchall()
count = 1
for row in records12:

    print(count, ". Mostcrowdedcities: ", row[0])
    count +=1

# # 13- Dunyanin nufusunu hesaplayiniz.
print("______________________________________________________________________________________")

im.execute("""SELECT sum(population) FROM Country""")
records13 = im.fetchall()
for row in records13:
    print("Dunyanin nufusu: ", row[0])
    
im.close()
