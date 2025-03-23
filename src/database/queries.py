CREATE_CITY_TABLE = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    lon REAL,
    lat REAL,
    country VARCHAR(255),
    name_uk VARCHAR(255),
    name_en VARCHAR(255)
);
'''

CREATE_CITY_INSTANCE = '''
INSERT INTO cities (
    name, lon, lat, country, name_uk, name_en
) VALUES (?, ?, ?, ?, ?, ?)
'''

FIND_CITY_BY_START_NAME_UK = '''
SELECT name FROM cities
WHERE name_uk LIKE ?
'''

FIND_CITY_BY_START_NAME_EN = '''
SELECT name FROM cities
WHERE name_en LIKE ?
'''
