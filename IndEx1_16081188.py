"""
Provide Python code to create a SQLite database and insert sample data.
Your solution may make use of either Python with sqlite3 OR Python with sqlalchemy.
The structure of the database must be as follows:

Database name: rain

Table names: user, forecast, city

Columns for user table: user_id (INTEGER PRIMARY KEY), username (TEXT NOT NULL), email (TEXT NOT NULL)

Columns for city table: city_id (INTEGER PRIMARY KEY), city (TEXT NOT NULL)

Columns for forecast table: forecast_id (INTEGER PRIMARY KEY), city_id (integer, Foreign Key), user_id (integer, Foreign Key), forecast_datetime (text not null), forecast (text not null), comment (text)

Insert the following records into each table:
    [user: user_id, username, email]
        1, weatherman, jo@bloggs.com
        2, itrains, itrains@alot.co.uk
        3, sunny, sunny_grl@sunshine.co.uk
    [city: city_id, city]
        1, London
        2, Manchester
        3, Birmingham
        4, Edinburgh
        5, Belfast
        6, Cardiff
    [forecast: forecast_id, city_id, user_id, forecast_datetime, forecast, comment]
        1, 2, 2, 2020-01-27 09:00:00, Moderate rain, It is really likely to rain today, sorry folks
        2, 6, 1, 2020-01-27 09:00:00, Heavy rain, Don't leave home without full waterproofs today!
        3, 1, 3, 2020-01-27 09:00:00, No rain, No umbrella required.

Note: SQLite does not have a datetime data type, use text and enter dates as YYYY-MM-DD HH:MM:SS
"""
import sqlite3

# Step 1: Create a connection object that represents the database
conn = sqlite3.connect('rain_sqlite.db')

# Step 2: Create a cursor object
c = conn.cursor()

# Step 3: Create tables
c.execute('''
          CREATE TABLE user
          (user_id INTEGER PRIMARY KEY,
          username TEXT NOT NULL, 
          email TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE city
          (city_id INTEGER PRIMARY KEY,
          city TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE forecast
          (forecast_id INTEGER PRIMARY KEY,
          city_id INTEGER,
          user_id INTEGER,
          forecast_datetime TEXT NOT NULL, 
          forecast TEXT NOT NULL,
          comment TEXT,
          FOREIGN KEY(city_id) REFERENCES city(city_id),
          FOREIGN KEY(user_id) REFERENCES user(user_id))
          ''')


# Insert data using values from variables
# Insert multiple rows cursor.executemany()
sql = "INSERT INTO user (username, email) VALUES (?, ?)"
values = [('weatherman', 'jo@bloggs.com'),
          ('itrains', 'itrains@alot.co.uk'),
          ('sunny', 'sunny_grl@sunshine.co.uk')]
c.executemany(sql, values)

sql = "INSERT INTO city (city) VALUES (?)"
values = [('London',),
          ('Manchester',),
          ('Birmingham',),
          ('Edinburgh',),
          ('Belfast',),
          ('Cardiff',)]
c.executemany(sql, values)


sql = "INSERT INTO forecast (forecast_id, city_id, user_id, forecast_datetime, forecast, comment) VALUES (?, ?, ?, ?, ?, ?)"
values = [(1, 2, 2, '2020-01-27 09:00:00', 'Moderate rain', 'It is really likely to rain today sorry folks'),
          (2, 6, 1, '2020-01-27 09:00:00', 'Heavy rain', "Dont leave home without full waterproofs today!"),
          (3, 1, 3, '2020-01-27 09:00:00', 'No rain', 'No umbrella required.')]
c.executemany(sql, values)

# Step 5: Save (commit) the changes
conn.commit()

# Step 6 (optional): Close the connection if you are done with it
conn.close()