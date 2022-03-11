import pyodbc

conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Interesting_Movies.db")

cursor = conn.execute(("SELECT * FROM Movies"))
view = cursor.fetchall()
for i in view:
	print(i)
	#print(i[0]+ "\t\t" +i[1]+ "\t\t" +i[2]+ "\t\t" +i[3]+ "\t\t" +str(i[4]))

conn.close()