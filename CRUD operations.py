import sqlite3

# CRUD operations


# # create database
conn = sqlite3.connect("students")
cursor = conn.cursor()



# # 2. create table
cursor.execute("""
	CREATE TABLE students (
		first_name TEXT,
		middle_name TEXT,
		surname TEXT,
		class INTEGER
	);
	""")
conn.commit()



# # 3. describe table schema
cursor.execute("PRAGMA table_info(students)")




# # 4. update table schema - by adding attribute
cursor.execute("""
	ALTER TABLE students
	ADD section TEXT
	""")



# # 5. drop table
cursor.execute("DROP TABLE students")			



# # 6. insert data
# # single data
cursor.execute("INSERT INTO students VALUES ('sai', 'eswar', 'somaraju', 9, 'A');")

# # multiple data
items = [
	('sai', 'roop', 'somaraju', 10,'A'),
	('sai', 'deepak', 'balija', 8, 'A'),
	('sandeep', 'sharma', 'vanga', 8, 'B')
]
cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?)", items)




# # 7. update data
cursor.execute("""UPDATE students 
	SET section='C' 
	WHERE first_name='sandeep'
	""")



# # 8. delete data
cursor.execute("DELETE from students WHERE class=8")




# # 9. Query data
# get one item
cursor.execute("SELECT rowid, * FROM students")
print(cursor.fetchone())

# # get all items
items = cursor.execute("SELECT rowid, * FROM students")
for row in items:
	print(row)



conn.commit()
conn.close()



