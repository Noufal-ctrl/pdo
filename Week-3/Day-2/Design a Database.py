import sqlite3

con=sqlite3.connect("food_delivery.db")
cursor=con.cursor()
#User Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    city TEXT
) 
""")
#Restaurants Table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS Restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    rating REAL
)
""")

#Orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    restaurant_id INTEGER,
    amount REAL,
    city TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(restaurant_id) REFERENCES Restaurants(restaurant_id)
)
""")

cursor.executemany("""
INSERT INTO Users (name, email, phone, city)
VALUES (?, ?, ?, ?)
""",[
    ("Noufal", "noufal@gmail.com", "9876543210", "Chennai"),
    ("Rahul", "rahul@gmail.com", "9123456780", "Bangalore"),
    ("Aisha", "aisha@gmail.com", "9988776655", "Chennai")
])
cursor.executemany("""
INSERT INTO Restaurants (name, location, rating)
VALUES (?, ?, ?)
""", [
    ("Pizza Hub", "Chennai", 4.5),
    ("Burger Point", "Bangalore", 4.2),
    ("Dosa Corner", "Chennai", 4.7)
])
cursor.executemany("""
INSERT INTO Orders (user_id, restaurant_id, amount, city)
VALUES (?, ?, ?, ?)
""", [
    (1, 1, 250, "Chennai"),
    (2, 2, 300, "Bangalore"),
    (1, 3, 150, "Chennai"),
    (3, 1, 400, "Chennai")
])

con.commit()
print("Db Setup Completed")
con.close()

##########                    OUTPUT                  ###########
Db Setup Completed
###----->>>>>Db created is uploaded
