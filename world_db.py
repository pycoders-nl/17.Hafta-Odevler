import sqlite3 as sql
data=sql.connect('world.db')
im=data.cursor()

# 1- Nufusu 100 milyonun uzerinde olan ulkeler hangileridir?
im.execute("""SELECT name FROM country WHERE population>100000000""")
result1=im.fetchall()
print('Countries with a population of more than 100 million:')
for i in result1:
    print(result1.index(i) + 1, '-', i[0], sep='')

# 2- Isminin sonunda “land” kelimesi gecen ulkeler hangileridir?
im.execute("""SELECT name FROM country WHERE name LIKE '%land'""")
result2=im.fetchall()
print ('Countries whose name ends with \'land\'')
for i in result2:
    print(result2.index(i) + 1, '-', i[0], sep='')

# 3- 500 bin ile 1 milyon arasinda nufusu olan sehirler hangileridir?
im.execute("""SELECT name FROM city WHERE 500000<=population<=1000000""")
result3=im.fetchall()
print('Cities with population between 500 thousand and 1 million:')
for i in result3:
    print(result3.index(i) + 1, '-', i[0], sep='')


# 4- Avrupa (“Europe”) kitasinda bulunan ulkelerin tamamini bulunuz.
im.execute("""SELECT name FROM country WHERE continent='Europe'""")
result4=im.fetchall()
print('Countries in Europe:')
for i in result4:
    print(result4.index(i) + 1, '-', i[0], sep='')

# 5- Tum ulkeleri yuzolcumleri buyukten kucuge olacak sekilde siralayaniz.
im.execute("""SELECT name FROM country ORDER BY SurfaceArea DESC""")
result5=im.fetchall()
print('Countries sorted by surface area:')
for i in result5:
    print(result5.index(i) + 1, '-', i[0], sep='')

# 6- Hollanda’nin (Netherlands) tum sehirlerini bulunuz.
im.execute("""SELECT name FROM city WHERE countrycode='NLD'""")
result6=im.fetchall()
print('Countries sorted by surface area:')
for i in result6:
    print(result6.index(i) + 1, '-', i[0],sep='')

# 7- Amsterdam’in nufusu kactir?
im.execute("""SELECT population FROM city WHERE name='Amsterdam'""")
print('Amsterdam population =',im.fetchall()[0][0])

# 8- Avrupa’nin (Europe) en kalabalik sehri hangisidir?
im.execute("""SELECT city.name FROM city INNER JOIN country ON city.countrycode=country.code WHERE
Continent='Europe' ORDER BY city.population DESC LIMIT 1""")
print('The most populous city in Europe =',im.fetchone()[0])

# 9- Afrika kitasinin (Africa) yuzolcumu en buyuk ulkesi hangisidir?
im.execute("""SELECT name FROM country  WHERE continent='Africa' ORDER BY SurfaceArea DESC LIMIT 1""")
print('The largest country in Africa =',im.fetchone()[0])

# 10- Asya (Asia) kitasinda yuzolcumune gore en buyuk 10 ulke hangileridir?
im.execute("""SELECT name FROM country WHERE continent='Asia' ORDER BY SurfaceArea DESC LIMIT 10""")
result10=im.fetchall()
print('The largest 10 contry in Asia')
for i in result10:
    print(result10.index(i)+1,'-',i[0],sep='')

# 11- Yuzolcumu en kucuk olan ulkeyi bulunuz.
im.execute("""SELECT name FROM country ORDER BY SurfaceArea LIMIT 1""")
print('The smallest country =',im.fetchone()[0])

# 12- En kalabalik 10 sehri bulunuz.
im.execute("""SELECT name FROM country ORDER BY population DESC LIMIT 10""")
result12=im.fetchall()
for i in result12:
    print(result12.index(i)+1,'-',i[0])

# 13- Dunyanin nufusunu hesaplayiniz.
im.execute("""SELECT SUM(population) FROM country """)
print('The population of The World =',im.fetchone()[0])






#
# print(*list(*im.execute("""SELECT MAX(id) AS id from gorevler """)))
# im.execute("""SELECT count(id) from gorevler WHERE durumId=3""")
# print(im.fetchall()[0][0])