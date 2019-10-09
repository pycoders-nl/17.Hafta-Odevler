import sqlite3 as sql


def DB_connector():
    conn = sql.connect("world.db")
    cur = conn.cursor()

    cur.execute('SELECT Name FROM country WHERE Population > 100000000')
    print("\n1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?\n", cur.fetchall())
    cur.execute('SELECT Name FROM country WHERE Name like "%land"')
    print("\n2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?\n", cur.fetchall())

    cur.execute('SELECT Name FROM city WHERE Population > 500000 AND Population < 1000000')
    print("\n3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?\n", cur.fetchall())

    cur.execute("SELECT Name FROM country WHERE Continent == 'Europe'")
    print("\n4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.\n", cur.fetchall())

    cur.execute("\nSELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC")
    print("\n5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.\n", cur.fetchall())

    cur.execute("SELECT Name FROM city WHERE CountryCode == 'NLD' ORDER BY Name ASC")
    print("\n6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.\n", cur.fetchall())

    cur.execute("SELECT Population FROM city WHERE Name == 'Amsterdam'")
    print("\n7- Amsterdam’in nufusu kactir?\n", cur.fetchall())

    cur.execute("SELECT city.Name, max(city.Population) FROM city "
                "INNER JOIN country on city.CountryCode = country.Code "
                "WHERE Continent == 'Europe'")
    print("\n8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?\n", cur.fetchall())

    cur.execute("SELECT Name, max(Population) FROM country WHERE Continent = 'Africa'")
    print("\n9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?\n", cur.fetchall())

    cur.execute("SELECT Name, Population FROM country WHERE Continent = 'Asia' ORDER BY Population DESC LIMIT 10")
    print("\n10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?\n", cur.fetchall())

    cur.execute("SELECT Name, min(Population) FROM country")
    print("\n11- Yuzolcumu en kucuk olan ulkeyi bulunuz.\n", cur.fetchall())

    cur.execute("SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 10")
    print("\n12- En kalabalik 10 sehri bulunuz.\n", cur.fetchall())

    cur.execute("SELECT sum(Population) FROM country")
    print("\n13- Dunyanin nufusunu hesaplayiniz.\n", cur.fetchall())



DB_connector()
