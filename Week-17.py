import sqlite3
vt = sqlite3.connect('world.db')
cur = vt.cursor()

#---------------------------------------------------------------------------------------------------

print("---»  Q1) Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?\n")

cur.execute("Select name, population from country "
            "where population > 100000000 order by population desc")
print(cur.fetchall())
cur.execute("Select count (name) from country "
            "where population > 100000000 order by population desc")
print(cur.fetchall())


#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q2) Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?\n")

cur.execute("Select name from country where name LIKE '%land' order by name asc")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------
print("\n\n---»  Q3) 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?\n")

cur.execute("Select name, population from city "
            "where population  between 500000 and 1000000 order by population desc")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q4) Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.\n")
cur.execute("Select name from country "
            "where continent='Europe' order by name asc")
print(cur.fetchall())

cur.execute("Select COUNT (name) from country "
            "where continent='Europe' order by name asc")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q5) Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.\n")

cur.execute("Select name, SurfaceArea from country order by surfacearea desc")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q6) Hollanda’nin (Netherlands) tum sehirlerini bulunuz.\n")

cur.execute("Select name from city where countrycode='NLD' order by name asc")
print(cur.fetchall())

cur.execute("Select count (name) from city where countrycode='NLD' order by name asc")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q7) Amsterdam’in nufusu kactir?\n")

cur.execute("Select population from city where name='Amsterdam'")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q8) Avrupa’nin (Europe) en kalabalik sehri hangisidir?\n")

cur.execute("Select name, MAX (population) from country where continent='Europe'")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q9) Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?\n")

cur.execute("Select name, MAX (surfacearea) from country where continent='Africa'")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q10) Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?\n")

cur.execute("Select name, surfacearea from country where continent='Asia' order by surfacearea desc limit 10")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q11) Yuzolcumu en kucuk olan ulkeyi bulunuz.\n")

cur.execute("Select name, MIN (SurfaceArea) from country")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q12) En kalabalik 10 sehri bulunuz.\n")

cur.execute("Select name, population from city order by population desc limit 10")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------

print("\n\n---»  Q13) Dunyanin nufusunu hesaplayiniz.\n")

cur.execute("Select SUM (population) from country")
print(cur.fetchall())

#---------------------------------------------------------------------------------------------------






