#!/usr/bin/env python3
"""
Main file
"""

print("BEFORE")
get_db = __import__('filtered_logger').get_db
print("AFTER")
db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
