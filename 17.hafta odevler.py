print('b.')
import sqlite3
conn = sqlite3.connect('world.db')
cursor = conn.cursor()

# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
for index,item in enumerate(cursor.execute("SELECT Name FROM country WHERE Population > 100000000"),start= 1):
     print(f'{index}-{item}')
#------------------------------------------------------------------------------------------
# 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
for i in cursor.execute('SELECT Name FROM country WHERE Name like "%land"'):
    print(i)
#------------------------------------------------------------------------------------------
# 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
for i in cursor.execute('SELECT Name FROM city WHERE Population > 500000 AND Population < 1000000'):
    print(i)
#------------------------------------------------------------------------------------------
# 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
for i in cursor.execute("SELECT Name FROM country WHERE Continent == 'Europe'"):
    print(i)
#------------------------------------------------------------------------------------------
# 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
for i in cursor.execute("SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC"):
    print(i)
#------------------------------------------------------------------------------------------
# 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
for i in cursor.execute("SELECT Name FROM city WHERE CountryCode == 'NLD' ORDER BY Name ASC"):
    print(i)
# ------------------------------------------------------------------------------------------
# 7- Amsterdam’in nufusu kactir?
for i in cursor.execute("SELECT Population FROM city WHERE Name == 'Amsterdam'"):
    print(f'Amsterdam Population: {i}')
# ------------------------------------------------------------------------------------------
# 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
for i in cursor.execute("SELECT city.Name, max(city.Population) FROM city INNER JOIN country on city.CountryCode = country.Code WHERE Continent == 'Europe'"):
    print(i)
# ------------------------------------------------------------------------------------------
# 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
for i in cursor.execute("SELECT Name, max(SurfaceArea) FROM country WHERE Continent = 'Africa'"):
    print(i)
# ------------------------------------------------------------------------------------------
# 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
for index,item in enumerate(cursor.execute("SELECT Name, SurfaceArea FROM country WHERE Continent = 'Asia' ORDER BY Population DESC LIMIT 10"),start= 1):
     print(f'{index}-{item}')
# ------------------------------------------------------------------------------------------
# 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
print(f'Yuzolcumu en kucuk olan ulke :{list(cursor.execute("SELECT Name, min(SurfaceArea) FROM country"))}')
# ------------------------------------------------------------------------------------------
# 12- En kalabalik 10 sehri bulunuz.
for index,item in enumerate(cursor.execute("SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 10"),start= 1):
    print(f'{index}-{item}')
# ------------------------------------------------------------------------------------------
# 13- Dunyanin nufusunu hesaplayiniz.
print(f'dunya nufus toplami :{list(cursor.execute("SELECT sum(Population) FROM country"))}')