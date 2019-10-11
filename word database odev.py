import sqlite3 as sql

data = sql.connect("world.db")
curs = data.cursor()


def datatable_name(): # Database deki tablo isimlerini listeliyor
    ab = curs.execute("""SELECT name FROM SQLITE_MASTER WHERE type = 'table' AND name NOT LIKE "sqlite_%" """)
    for i in ab:
        print(i)

def table_column(table_name): # ismi girilen tablonun kolon isimlerini gosteriyor
    names =  curs.execute("""SELECT * FROM {} """.format(table_name))
    a= names.description
    for i in a:
        print(i[0]," ", end="")

def table_list(table_name): # ismi girilen tablonun icerigini listeliyor
    c = curs.execute("""SELECT * FROM {}""".format(table_name))
    for a in c:
        print(a)

def PopGreater100():  # Nufusu 100 milyondan fazla olan ulkeler
    country_name = list(curs.execute("""SELECT Name FROM country WHERE Population>100000000 """))
    for i in range(len(country_name)):
        print(i+1,"-) ", country_name[i][0])

def LandInCountryName():   #Isminin sonunda “land” kelimesi gecen ulkeler
    country_name = list(curs.execute("""SELECT Name FROM country WHERE name LIKE "%land" """))
    for i in range(len(country_name)):
        print(i + 1, "-) ", country_name[i][0])

def CityBetween500_1000():
    city_name = list(curs.execute("""SELECT Name FROM city WHERE Population BETWEEN 500000 AND 1000000  """))
    for i in range(len(city_name)):
        print(i + 1, "-) ", city_name[i][0])

def CountryEuropa():
    country_name = list(curs.execute("""SELECT Name FROM country WHERE Continent="Europe" """))
    for i in range(len(country_name)):
        print(i + 1, "-) ", country_name[i][0])

def CountrySurfaceArea():  # Tum ulkelerin yuzolcumune gore kucukten buyuge dogru siralanmasi
    country_name = list(curs.execute("""SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea ASC """))
    for i in range(len(country_name)):
        print("{}-) {} : {}".format(i+1,str(country_name[i][0]).ljust(45), str(country_name[i][1]).rjust(20) ))

def CityOfNederland():  # Hollandanin tum sehirleri
    city_name = list(curs.execute("""SELECT Name FROM city WHERE CountryCode = "NLD" """))
    for i in range(len(city_name)):
        print("{}-) {} ".format(i+1,str(city_name[i][0]).ljust(30) ))

def PopulationOfAmsterdam(): #Amsterdamin Nufusu
    amsterdam_population = list(curs.execute("""SELECT Population FROM city WHERE Name = "Amsterdam" """))
    print("Amsterdam'in Nufusu : ", amsterdam_population[0][0] )

def CrowdedCityofEuropa(): #Avrupanin en kalabalik sehri
    crowded_city = list(curs.execute("""SELECT country.Code, country.Continent, city.Name, max(city.Population) FROM country, city WHERE country.Code = city.CountryCode AND Continent="Europe" """))
    for i in crowded_city:
        print(i)

def BiggestCountryofAfrica(): #Afrika kitasinin yuzolcumu en buyuk olan ulkesi
    biggest_country = list(curs.execute("""SELECT Name, max(SurfaceArea) FROM country WHERE Continent="Africa" """))
    print(1, "-) ", biggest_country[0][0], "   ", biggest_country[0][1])

def BigTenCountryofAsia(): #Asya kitasinda yuzolcumu en buyuk olan 10 ulke
    ten_country = list(curs.execute("""SELECT Name, SurfaceArea FROM country WHERE Continent="Asia" ORDER BY SurfaceArea DESC LIMIT 10 """))
    for i in range(len(ten_country)):
        print(i + 1, "-) ", str(ten_country[i][0]).ljust(25), "   ", str(ten_country[i][1]).rjust(15))

def SmallestCountry(): #Yuzolcumu en kucuk olan ulke
    smallest_country = list(curs.execute("""SELECT Name, min(SurfaceArea) FROM country """))
    print(1, "-) ", smallest_country[0][0], "   ", smallest_country[0][1])

def CrowdedTenCity(): #En kalabalik 10 sehir
    ten_city = list(curs.execute("""SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 10 """))
    for i in range(len(ten_city)):
        print(i + 1, "-) ", str(ten_city[i][0]).ljust(25), "   ", str(ten_city[i][1]).rjust(15))

def PopulationOfWorld(): # Dunyanin Toplam Nufusu
    world = list(curs.execute("""SELECT sum(Population) FROM country """))
    print("World Population : ", world[0][0])



print("\n NUFUSU 100 MILYONDAN FAZLA OLAN ULKELER \n")
PopGreater100()

print("\n ISMININ SONUNDA 'LAND' KELIMESI GECEN ULKELER \n")
LandInCountryName()

print("\n NUFUSU 500 BIN ILE 1 MILYON ARASINDA OLAN SEHIRLER\n")
CityBetween500_1000()

print("\n AVRUPA KITASINDA OLAN ULKELERIN ISIMLERI\n")
CountryEuropa()

print("\n TUM ULKELERIN YUZOLCUMUNE GORE KUCUKTEN BUYUGE SIRALANMIS LISTESI\n")
CountrySurfaceArea()

print("\n HOLLANDANIN TUM SEHIRLERININ ISIM LISTESI\n")
CityOfNederland()

print("\n AMSTERDAM'IN NUFUSU\n")
PopulationOfAmsterdam()

print("\n AVRUPANIN EN KALABALIK SEHRI\n")
CrowdedCityofEuropa()

print("\n AFRIKA KITASININ YUZOLCUMU EN BUYUK OLAN ULKESI\n")
BiggestCountryofAfrica()

print("\n ASYA KITASINDA YUZOLCUMU EN BUYUK OLAN ILK 10 ULKE\n")
# BigTenCountryofAsia()

print("\n YUZOLCUMU EN KUCUK OLAN ULKE\n")
SmallestCountry()

print("\n EN KALABALIK 10 SEHIR \n")
CrowdedTenCity()

print("\n DUNYANIN TOPLAM NUFUSU\n")
PopulationOfWorld()





# datatable_name()
# table_column("country")
# table_list("country")