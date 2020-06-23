DROP TABLE IF EXISTS drink;
CREATE TABLE drink (
	id INTEGER NOT NULL, 
	title VARCHAR(80), 
	recipe VARCHAR(180) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (title)
);
INSERT INTO drink values (1, 'ttilte', '[{"color": "white", "name": "tr", "parts": 2}]');
