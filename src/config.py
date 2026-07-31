import os
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="nozomi.proxy.rlwy.net",
        user="root",
        password="VMDIugKDMGnoadbGVhvWhvfbAWKBzgbn",
        database="railway",
        port=12938
    )
    return connection