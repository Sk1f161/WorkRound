#!/usr/bin/env python3

import psycopg2

try:
    conn = psycopg2.connect("dbname='template1' user='postgres' host='localhost' password='Tgutti09'")
except:
    print("No connect")

cur = conn.cursor()

cur.execute("""SELECT * from pg_database""")
rows = cur.fetchall()
print("\nShow databases:\n")
for row in rows:
    print ("   ", row[0])
