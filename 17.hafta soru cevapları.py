import os
import sqlite3 as sqq
vt=sqq.connect("world.db")
im=vt.cursor()
print("1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?")

im.execute("SELECT name FROM country WHERE (population >'100000000')")
print(im.fetchall())

print("""\n2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?""")
im.execute("""SELECT name FROM country WHERE (name like "%land")""")
print(im.fetchall())

print("\n3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?")
im.execute("""SELECT Name FROM city WHERE (Population>"500000" and Population <"1000000")""")
print(im.fetchall())

print("\n4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.")
im.execute("""SELECT name FROM country WHERE (continent="Europe")""")
print(im.fetchall())

print("\n5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.")
im.execute("""SELECT SurfaceArea, name  FROM country ORDER BY SurfaceArea """)
print(im.fetchall())

print("\n6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.")
im.execute("""SELECT name FROM city WHERE (CountryCode="NLD")""")
print(im.fetchall())

print("\n7- Amsterdam’in nufusu kactir?")

im.execute("""SELECT population FROM city WHERE (name="Amsterdam")""")
print(im.fetchall())

print("\n8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?")
im.execute("""SELECT country.Code, country.Continent, city.Name, max(city.population) FROM country, city WHERE country.Code = city.CountryCode AND (Continent="Europe") """)
print (im.fetchall())

print("\n9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?")
im.execute("""SELECT Name, max(SurfaceArea) FROM country WHERE (Continent="Africa") """)
print (im.fetchall())

print("\n10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?")
im.execute("""SELECT Name, SurfaceArea FROM country WHERE Continent="Asia" ORDER BY SurfaceArea DESC LIMIT 10 """)
print (im.fetchall())

print("\n11- Yuzolcumu en kucuk olan ulkeyi bulunuz.")
im.execute("""SELECT Name, min(SurfaceArea) FROM country """)
print (im.fetchall())

print("\n12- En kalabalik 10 sehri bulunuz.")
im.execute("""SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 10 """)
print (im.fetchall())

print("\n13- Dunyanin nufusunu hesaplayiniz.")
im.execute("""SELECT sum(Population) FROM country """)
print(im.fetchall())
