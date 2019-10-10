import sqlite3
vt=sqlite3.connect("world.db")
im=vt.cursor()

print("1- Nufusu 100 milyonun uzerinde olan ulkeler")
result=im.execute("""SELECT name,Population FROM country WHERE Population>100000000;""")
# print(result.fetchall())
for i in list(result.fetchall()):
    print(i)
print(" 2- Isminin sonunda “land” kelimesi gecen ulkeler")
result=im.execute("""SELECT name FROM country WHERE name LIKE '%land';""")
for i in list(result.fetchall()):
    print(i)

print(" 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler ")
result=im.execute("""SELECT name,Population FROM city where Population BETWEEN 500000 AND 1000000;""")
for i in list(result.fetchall()):
    print(i)

print(" 4- Avrupa (“Europe”) kitasinda bulunan ulkeler")
result=im.execute("""SELECT name,Continent FROM country where Continent='Europe';""")
for i in list(result.fetchall()):
    print(i)

print("5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.")
result=im.execute("""SELECT name,SurfaceArea FROM country ORDER BY SurfaceArea DESC;""")
for i in list(result.fetchall()):
    print(i)

print("6- Hollanda’nin (Netherlands) tum sehirleri")
result=im.execute("""SELECT name,CountryCode FROM city WHERE CountryCode='NLD';""")
for i in list(result.fetchall()):
    print(i)

print(" 7- Amsterdam’in nufusu")
result=im.execute("""SELECT name,Population FROM city WHERE name='Amsterdam';""")
for i in list(result.fetchall()):
    print(i)

print("8- Avrupa’nin (Europe) en kalabalik sehri ")
result=im.execute("""SELECT city.CountryCode,city.name,MAX(city.population),country.Continent
FROM city LEFT JOIN country ON city.CountryCode=country.Code
WHERE country.Continent='Europe';""")
for i in list(result.fetchall()):
    print(i)

print("9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi")
result=im.execute("""SELECT name,max(SurfaceArea),Continent FROM country WHERE Continent='Africa';""")
for i in list(result.fetchall()):
    print(i)

print(" 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke ")
result=im.execute("""SELECT name,Continent,SurfaceArea FROM country WHERE Continent='Asia' ORDER BY SurfaceArea DESC LIMIT 10;""")
for i in list(result.fetchall()):
    print(i)

print("11- Yuzolcumu en kucuk olan ulke")
result=im.execute("""SELECT name, MIN(SurfaceArea) FROM country;""")
for i in list(result.fetchall()):
    print(i)

print(" 12- En kalabalik 10 sehir .")
result=im.execute("""SELECT name,Population FROM city ORDER BY Population DESC LIMIT 10;""")
for i in list(result.fetchall()):
    print(i)

print(" 13- Dunyanin nufusu ")
result=im.execute("""SELECT sum(Population) FROM country;""")
for i in list(result.fetchall()):
    print(i)

vt.commit()
vt.close()