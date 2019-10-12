import sqlite3 as sql
vt = sql.connect("C:\\Users\\Gebruiker\\Desktop\\Phyton\\Onyedinci_hafta_odev\\world.db")
im = vt.cursor()

# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
im.execute("SELECT name FROM COUNTRY WHERE POPULATION > 100000000")
print(im.fetchall())

# 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
im.execute("SELECT name FROM COUNTRY WHERE name like '%land'")
print(im.fetchall())

# 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
im.execute('SELECT name FROM city where Population between "500000"and "1000000"')
print(im.fetchall())

# 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
im.execute('SELECT name FROM country where Continent="Europe"')
print(im.fetchall())

# 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
im.execute('SELECT name, SurfaceArea FROM country order by SurfaceArea asc')# sonuna desc yazarsak buyukten kucuge siralar
print(im.fetchall())

# 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
im.execute('SELECT name,CountryCode from city where CountryCode="NLD"')
print(im.fetchall())

# 7- Amsterdam’in nufusu kactir?
im.execute('SELECT * from city where name="Amsterdam"')
print(im.fetchall())

# 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
im.execute('SELECT * from country where Continent="Europe" order by Population desc LIMIT 1')
print(im.fetchall())

# 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
im.execute('SELECT * from country where Continent="Africa" order by SurfaceArea desc LIMIT 1')
print(im.fetchall())

# 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
im.execute('SELECT * from country where Continent="Asia" order by SurfaceArea desc LIMIT 10')
print(im.fetchall())

# 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
im.execute('SELECT * from country order by SurfaceArea asc LIMIT 1')
print(im.fetchall())

# 12- En kalabalik 10 sehri bulunuz.
im.execute('SELECT * from city order by Population desc LIMIT 10')
print(im.fetchall())

# 13- Dunyanin nufusunu hesaplayiniz.
im.execute('SELECT sum(Population) as "Toplam Nufus" from country ')
print(im.fetchall())