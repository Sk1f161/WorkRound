#!/usr/bin/env python3

import mysql.connector

cnx = mysql.connector.connect(user='root', password='34c13165d07017d909f8', host='127.0.0.1', database='keystone')
cursor = cnx.cursor()
f = open('res_endr9','r').read()
add_token = ('INSERT' + f)

cursor.execute(add_token)
cnx.commit()
cursor.close()
cnx.close()
