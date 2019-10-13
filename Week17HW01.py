import sqlite3 as sql

wd= sql.connect('C:/Users/Gebruiker/Desktop/SQL/world.db')
im=wd.cursor()

#1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
im.execute("""Select name from country where Population > 100000000""")
veriler = im.fetchall()
print("1. Nufusu 100 milyonun uzerinde olan ulkeler:")
for i in veriler:
    print(i[0])
print("\n")

#2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
im.execute("""Select name from country Where Name Like '%land'""")
veriler2 = im.fetchall()
print("2.Isminin sonu 'land' olan ulkeler:")
for i in veriler2:
    print(i[0])
print("\n")

#3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
im.execute("""select name from city where population between 500000 and 1000000""")
veriler3 = im.fetchall()
print("3.500 bin ile 1 milyon arasinda nufusu olan sehirler:")
for i in veriler3:
    print(i[0])
print("\n")

#4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz
im.execute("""select name,continent from country where continent like 'Europe'""")
veriler4 = im.fetchall()
print("Avrupa (“Europe”) kitasinda bulunan ulkeler:")
for i in veriler4:
    #print(i[0],"Continent is:",i[1])
    print(i[0])
print("\n")

#5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
im.execute("""select name,surfacearea from country order by  surfacearea desc""")
veriler4 = im.fetchall()
print("Tum ulkeleri yuzolcumleri buyukten kucuge:")
for i in veriler4:
    print(i[0],"=",i[1])
print("\n")

#6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
im.execute("""select name from city where countrycode like 'NLD' """)
veriler5 = im.fetchall()
print("Hollanda’nin (Netherlands) tum sehirleri:")
for i in veriler5:
    print(i[0])
print("\n")

#Amsterdam’in nufusu kactir?
im.execute("""select population,name from city where name like 'Amsterdam' """)
veriler6 = im.fetchall()
print("Amsterdam’in nufusu:")
for i in veriler6:
    print(i[0])
print("\n")

#8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
im.execute("""select city.name,city.population from city
            inner join country on city.CountryCode= country.Code
            where continent =='Europe'
            order by city.Population DESC """)
veriler7 = im.fetchmany()
print("Avrupa’nin (Europe) en kalabalik sehri:")
for i in veriler7:
    print(i[0],"=",i[1])
print("\n")

#9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
im.execute("""select name,surfacearea from country
            where continent =='Africa'
            order by surfacearea DESC             
            """)
veriler8 = im.fetchmany()
print("Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi:")
for i in veriler8:
    print(i[0],"=",i[1])
print("\n")

#10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
im.execute("""select name,surfacearea from country
            where continent =='Asia'
            order by surfacearea DESC             
            """)
veriler9 = im.fetchmany(10)
print("Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke:")
key=1
for i in veriler9:
    print(key,"-",i[0],"=",i[1])
    key+=1
print("\n")

#11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
im.execute("""select name,surfacearea from country
            order by surfacearea ASC             
            """)
veriler10 = im.fetchmany()
print("Yuzolcumu en kucuk olan ulke:")
for i in veriler10:
    print(i[0],"=",i[1],'km2')
print("\n")

#12- En kalabalik 10 sehri bulunuz.
im.execute("""select city.name,city.population from city
            inner join country on city.CountryCode= country.Code
            order by city.Population DESC            
            """)
veriler10 = im.fetchmany(10)
print("En kalabalik 10 sehir:")
keys=1
for i in veriler10:
    print(i[0],"=",i[1])
    keys+=1
print("\n")

#13- Dunyanin nufusunu hesaplayiniz.
im.execute("""select sum(population) from country""")
veriler11 = im.fetchall()
print("Dunyanin nufusu:")
for i in veriler11:
    print(i[0])
print("\n")