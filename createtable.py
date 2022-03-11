import pyodbc

conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Interesting_Movies.db")

conn.execute("""CREATE TABLE Movies(
	Name text,
	Actor text,
	Actress text,
	Director text,
	Release_Year int);""")

conn.commit()
conn.close()