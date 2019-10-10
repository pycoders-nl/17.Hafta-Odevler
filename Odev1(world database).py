import _sqlite3 as sql
vt = sql.connect('world.db')
im = vt.cursor()

# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
im.execute("SELECT Name FROM country WHERE Population > 100000000")
print(im.fetchall())

# 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
im.execute("SELECT Name From country WHERE Name LIKE '%land'")
print(im.fetchall())

# 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
im.execute("SELECT Name FROM city WHERE Population BETWEEN 500000 AND 1000000")
print(im.fetchall())

# 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
im.execute("SELECT Name FROM country WHERE continent='Europe'")
print(im.fetchall())

# 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
im.execute("SELECT Name FROM country ORDER BY SurfaceArea DESC")
print(im.fetchall())

# 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
im.execute("SELECT Name FROM city WHERE CountryCode='NLD'")
print(im.fetchall())

# 7- Amsterdam’in nufusu kactir?
im.execute("SELECT Name,Population FROM city WHERE name='Amsterdam'")
print(im.fetchall())

# 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
im.execute("SELECT city.Name, MAX(city.population) FROM city INNER JOIN country ON city.CountryCode=country.Code "
           "WHERE country.continent='Europe'")
print(im.fetchall())

# 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
im.execute("SELECT Name, MAX(SurfaceArea) FROM country WHERE continent='Africa'")
print(im.fetchall())

# 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
im.execute("SELECT Name FROM country WHERE continent='Africa' ORDER BY SurfaceArea DESC LIMIT 10")
print(im.fetchall())

# 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
im.execute("SELECT Name,MIN(SurfaceArea) FROM country")
print(im.fetchall())

# 12- En kalabalik 10 sehri bulunuz.
im.execute("SELECT Name FROM country ORDER BY Population DESC LIMIT 10")
print(im.fetchall())

# 13- Dunyanin nufusunu hesaplayiniz.
im.execute("SELECT SUM(Population) FROM country")
print(im.fetchall())
