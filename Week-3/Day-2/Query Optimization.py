import sqlite3
import time

conn = sqlite3.connect("food_delivery.db")
cursor = conn.cursor()

#revenue per city
print("Revenue per city:")
cursor.execute("""
SELECT city, SUM(amount)
FROM Orders
GROUP BY city
""")

for row in cursor.fetchall():
    print(row)

#performance before index
start = time.time()

cursor.execute("""
SELECT city, SUM(amount)
FROM Orders
GROUP BY city
""")

cursor.fetchall()
end = time.time()
print(f"Time WITHOUT index: {end - start:.6f} sec")

#Indexing on city
cursor.execute("CREATE INDEX IF NOT EXISTS idx_city ON Orders(city)")
conn.commit()

#performance after index
start = time.time()

cursor.execute("""
SELECT city, SUM(amount)
FROM Orders
GROUP BY city
""")

cursor.fetchall()
end = time.time()
print(f"Time WITHOUT index: {end - start:.6f} sec")

#Query plan
print("Query Plan:")
cursor.execute("EXPLAIN QUERY PLAN SELECT city, SUM(amount) FROM Orders GROUP BY city")
for row in cursor.fetchall():
    print(row)

conn.close()

############                    OUTPUT                    ############
Revenue per city:
('Bangalore', 300.0)
('Chennai', 800.0)

Time WITHOUT index: 0.000325 sec
Time WITH index: 0.000291 sec

Query Plan:
(7, 0, 0, 'SCAN Orders USING INDEX idx_city')
