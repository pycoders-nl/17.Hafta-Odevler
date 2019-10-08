import sqlite3
 
db = sqlite3.connect("world.db")

cr = db.cursor()

ans = cr.execute("SELECT name FROM country WHERE population > 100000000")
print("1-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country WHERE name like '%land'")
print("2-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM city WHERE Population BETWEEN 500000 and 1000000")
print("3-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country WHERE Continent = 'Europe'")
print("4-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country ORDER BY SurfaceArea DESC")
print("5-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM city WHERE CountryCode = 'NLD'")
print("6-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT Population FROM city WHERE name = 'Amsterdam'")
print("7-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT city.name FROM city INNER JOIN country on city.CountryCode = country.Code WHERE Continent = 'Europe' ORDER BY city.Population DESC LIMIT 1")
print("8-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country WHERE Continent = 'Africa' ORDER BY SurfaceArea DESC LIMIT 1")
print("9-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 10")
print("10-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM country ORDER BY SurfaceArea LIMIT 1")
print("11-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT name FROM city ORDER BY Population DESC LIMIT 10")
print("12-\n", ans.fetchall(), "\n")

ans = cr.execute("SELECT sum(population) FROM country ")
print("13-\n", ans.fetchall(), "\n")

