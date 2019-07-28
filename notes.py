"""
This file contains all the necessary links, resources...
blogs.....................

All i needed and used, and the bookmarks, notes ect
will be added into the file.
"""

# declaration of the tables I created.
"""
CREATE TABLE IF NOT EXISTS Wilaya(
	code varchar(50),
	name varchar(50),
	
	PRIMARY KEY code
);

CREATE TABLE IF NOT EXISTS Category(
	name varchar(50),
	
	PRIMARY KEY name
);

CREATE TABLE IF NOT EXISTS Phone(
	number varchar(50),
	category varchar(50),
	wilaya varchar(50),
	
	PRIMARY KEY number,
	FOREIGN KEY (wilaya) REFERENCES Wilaya(code),
	FOREIGN KEY (category) REFERENCES Category(name)
);
"""



"""

	
"""