"""
This file contains all the necessary links, resources...
blogs.....................

All i needed and used, and the bookmarks, notes ect
will be added into the file.
"""

# declaration of the tables I created.
"""
CREATE TABLE IF NOT EXISTS wilaya(
	code varchar(50) PRIMARY KEY,
	name varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS category(
	name varchar(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS phone(
	number varchar(50) PRIMARY KEY,
	category varchar(50) NOT NULL,
	wilaya varchar(50) NOT NULL,
	
	FOREIGN KEY (wilaya) REFERENCES Wilaya(code),
	FOREIGN KEY (category) REFERENCES Category(name)
);
"""



"""
query = " INSERT INTO wilaya(code,name) VALUES(?,?)"
print("QUERY PREPARED:: ", db.prepareQuery(query))
for wl in range(1, 49):
	print(db.insertRow([str(wl), wilaya[wl - 1]]))

query = " INSERT INTO category(name) VALUES(?)"
print("QUERY PREPARED:: ", db.prepareQuery(query))
for cat in category:
	print(db.insertRow([cat]))

	query = " INSERT INTO phone(number,category,wilaya) VALUES(?,?,?)"

	print("DATA BASE OPENED:: ", db.connect())
	print("QUERY PREPARED:: ", db.prepareQuery(query))
	print("\n")
	
	file = open("data.txt", "r")
	while True:
		data = file.readline()

		if data == "":
			break
		else:
			data = data[1:-2].split(",")
			to_insert = [data[-1]]
			to_insert += data[:-1] 
			print(to_insert, db.insertRow(to_insert))
"""