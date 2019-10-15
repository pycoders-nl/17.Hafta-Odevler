import sqlite3
vt=sqlite3.connect('world.db')
im=vt.cursor()

print("1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?")
im.execute('select * from country where Population > 100000000')
sonuc=im.fetchall()
for i in sonuc:
  print(i)


print("2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?")
im.execute('select * from country where Name like "%land"')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?")
im.execute('select * from  city where Population between 500000 and 1000000')
sonuc=im.fetchall()
for i in sonuc:
  print(i)


print("4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.")
im.execute('select * from country where Continent="Europe"')
sonuc=im.fetchall()
for i in sonuc:
  print(i)


print("5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.")
im.execute('select * from country order by SurfaceArea DESC')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.")
im.execute('select Name from city where CountryCode="NLD"')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("7- Amsterdam’in nufusu kactir?")
im.execute('select Name, Population from city where Name= "Amsterdam"')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?")
im.execute('select Max(city.Population), city.Name from city,country where country.Continent="Europe" and country.Code= city.CountryCode')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?")
im.execute('select name, max(SurfaceArea) from country where Continent="Africa"')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?")
im.execute('select * from country where Continent="Asia" order by SurfaceArea DESC limit 10')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("11- Yuzolcumu en kucuk olan ulkeyi bulunuz.")
im.execute('select * from country order by SurfaceArea limit 1 ')
sonuc=im.fetchall()
print(sonuc)

print("12- En kalabalik 10 sehri bulunuz.")
im.execute('select * from city order by Population DESC Limit 10')
sonuc=im.fetchall()
for i in sonuc:
  print(i)

print("13- Dunyanin nufusunu hesaplayiniz.")
im.execute('select sum(Population) as DunyaninNufusu from country ')
sonuc=im.fetchall()
print(sonuc)

vt.commit()
vt.close()