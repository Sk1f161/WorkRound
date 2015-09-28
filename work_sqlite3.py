#!/usr/bin/env python3
import sqlite3


conn = sqlite3.connect('9d4683fd8f36e708773b5778fa4d4aca.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM container'):
    print(row)
