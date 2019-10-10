print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

import sqlite3 as sql

db = sql.connect("C:\\Users\\gebruiker\\PycharmProjects\\mathchi\\huiswerks\\17.Week\\17.Hafta-Odevler\\world.db")
im = db.cursor()

# 1. Question
for i, j in enumerate(im.execute("""SELECT Name FROM country WHERE Population > 100000000"""), start=1):
    print(i, "~", *j)

# 2. Question
for i, j in enumerate(im.execute("""SELECT Name FROM country WHERE name like '%land'"""), start=1):
    print(i, "~", *j)

# 3. Question
for i, j in enumerate(im.execute("""SELECT Name FROM city WHERE Population > 500000 AND Population < 1000000"""), start=1):
    print(i, "~", *j)

# 4. Question
for i, j in enumerate(im.execute("""SELECT name FROM country WHERE continent == 'Europe'"""), start=1):
    print(i, "~", *j)

# 5. Question
for i, j in enumerate(im.execute("""SELECT name, SurfaceArea FROM country ORDER BY SurfaceArea DESC"""), start=1):
    print(i, "~", *j)

# 6. Question
for i, j in enumerate(im.execute("""SELECT name FROM city WHERE countrycode == 'NLD' ORDER BY name ASC"""), start=1):     # alfabetik siraya gore siralasin
    print(i, "~", *j)

# 7. Question
for i in im.execute("""SELECT population FROM city WHERE name == 'Amsterdam' """):
    print("Amsterdam population: ", *i)

# 8. Question
for i in im.execute("""SELECT city.name, max(city.Population) FROM city INNER JOIN country on city.CountryCode = country.Code WHERE Continent == 'Europe'"""):
    print("In Europe, the biggest population city is\n", *i)

#9. Question
for i in im.execute("""SELECT name, max(country.SurfaceArea) FROM country WHERE Continent = 'Africa'"""):
    print("In Africa, the biggest surface area city: \n", *i)

#10. Question
print("In Asia, 10 the biggest population countries: ")
for i, j in enumerate(im.execute("""SELECT name, SurfaceArea FROM country WHERE Continent = 'Asia' ORDER BY Population DESC LIMIT 10"""), start=1):
    print(i, "~", *j)

#11. Question
for i in im.execute("""SELECT name, MIN(SurfaceArea) FROM country ORDER BY SurfaceArea  """):
    print("The smallest surface area country: ", *i)

#12. Question
print("10 the biggest population cities: ")
for i, j in enumerate(im.execute("""SELECT name, Population FROM city ORDER BY Population DESC LIMIT 10"""), start=1):
    print(i, "~", *j)

#13. Question
for i in im.execute("""SELECT SUM(Population) FROM country """):
    print("In the World, Total population: ", *i)

