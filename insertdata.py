import pyodbc

conn = pyodbc.connect("Driver=SQLite3 ODBC Driver;Database=Interesting_Movies.db")

conn.execute("""INSERT INTO Movies VALUES ('Sholay','Dharmendra,Amitabh Bachchan','Hema Malini','Ramesh Sippy',1975),
	('Spectre','Daniel Craig','Lea Seydoux','Sam Mendes',2015),
	('John Wick','Keanu Reaves','Bridget Moynahan','Chad Stahelski',2014),
	('The Matrix Resurrections','Keanu Reaves','Jessica Henwick','Lana Wachowski',2021),
	('Spider-Man: No Way Home','Tom Holland,Tobey Maguire,Andrew Garfield','Zendaya','Jon Watts',2021),
	('3 Idiots','Amir Khan','Kareena Kapoor','Rajkumar Hirani',2009);
	""")

conn.commit()
conn.close()