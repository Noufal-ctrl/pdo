import sqlite3
import random

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Table Creation
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    action TEXT
)
""")

users = ["A", "B", "C", "D"]
actions = ["click", "purchase"]

# Inserting 50 records
for _ in range(50):
    user = random.choice(users)
    action = random.choice(actions)
    cursor.execute("INSERT INTO transactions (user, action) VALUES (?, ?)", (user, action))

conn.commit()

print("Inserted 50 records (OLTP)")


cursor.execute("SELECT COUNT(*) FROM transactions WHERE action='purchase'")
total_purchases = cursor.fetchone()[0]

print("Total Purchases:", total_purchases)

cursor.execute("""
SELECT user, COUNT(*) as cnt
FROM transactions
GROUP BY user
ORDER BY cnt DESC
LIMIT 1
""")

top_user = cursor.fetchone()

print("Top Active User:", top_user[0], "with", top_user[1], "actions")

conn.close()

##########            OUTPUT              ##########
Inserted 50 records (OLTP)
Total Purchases: 22
Top Active User: A with 18 actions
