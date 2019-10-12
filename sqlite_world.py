import sqlite3
veritabani=sqlite3.connect( "C:\\payton\\17.Hafta-Odevler\\world.db" )
imlec=veritabani.cursor()

print("1- Nufusu 100 milyonun uzerinde olan ulkeler")
sonuc=imlec.execute( """SELECT name,Population
                     FROM country WHERE Population>100000000;
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#*************************************************************************
print(" 2- Isminin sonunda “land” kelimesi gecen ulkeler")
sonuc=imlec.execute( """SELECT name FROM country
                     WHERE name LIKE '%land';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print(" 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler ")
sonuc=imlec.execute( """SELECT name,Population FROM city
                     where Population BETWEEN 500000 AND 1000000;
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print(" 4- Avrupa (“Europe”) kitasinda bulunan ulkeler")
sonuc=imlec.execute( """SELECT name,Continent FROM country
                     where Continent='Europe';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print("5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.")
sonuc=imlec.execute( """SELECT name,SurfaceArea FROM country
                     ORDER BY SurfaceArea DESC;
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print("6- Hollanda’nin (Netherlands) tum sehirleri")
sonuc=imlec.execute( """SELECT name,CountryCode FROM city
                     WHERE CountryCode='NLD';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print(" 7- Amsterdam’in nufusu")
sonuc=imlec.execute( """SELECT name,Population FROM city
                     WHERE name='Amsterdam';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print("8- Avrupa’nin (Europe) en kalabalik sehri ")
sonuc=imlec.execute( """SELECT city.CountryCode,city.name,
                     MAX(city.population),country.Continent
                     FROM city LEFT JOIN country
                     ON city.CountryCode=country.Code
                     WHERE country.Continent='Europe';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print("9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi")
sonuc=imlec.execute( """SELECT name,max(SurfaceArea),Continent
                     FROM country WHERE Continent='Africa';
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print(" 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke ")
sonuc=imlec.execute( """SELECT name,Continent,SurfaceArea
                     FROM country WHERE Continent='Asia'
                     ORDER BY SurfaceArea DESC LIMIT 10;
                 """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print("11- Yuzolcumu en kucuk olan ulke")
sonuc=imlec.execute( """SELECT name, MIN(SurfaceArea) FROM country;""" )
for i in list( sonuc.fetchall() ):
    print(*i)
#****************************************************************************
print(" 12- En kalabalik 10 sehir .")
sonuc=imlec.execute( """SELECT name,Population
                     FROM city ORDER BY Population
                     DESC LIMIT 10;
                  """ )
print(*(i for i in list( sonuc.fetchall() )),sep='\n')
#****************************************************************************
print(" 13- Dunyanin nufusu ")
sonuc=imlec.execute( """SELECT sum(Population) FROM country;""" )
print(*sonuc)
#****************************************************************************
veritabani.commit()
veritabani.close()
