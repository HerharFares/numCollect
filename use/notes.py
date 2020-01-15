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
