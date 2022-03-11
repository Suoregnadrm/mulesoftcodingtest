import pyodbc

conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Interesting_Movies.db")
if(conn == False):
	print("Error while connecting!")
else:
	print("Database connected successfully!")

conn.commit()
conn.close()