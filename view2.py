import pyodbc

conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Interesting_Movies.db")

cursor = conn.execute(("SELECT Name FROM Movies WHERE Actor='Keanu Reaves'"))
view = cursor.fetchall()
for i in view:
	print(i)

conn.close()