
# import pymysql

# conn = pymysql.connect(
#     host="localhost",
#     user="harsh",          # new user
#     password="strongpassword",
#     database="learnsql"
# )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM students;")
# print(cursor.fetchall())
# conn.close()
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="harsh",          # or root if you switched
    password="your_password",
    database="learnsql"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
print("Connected to:", cursor.fetchone())
conn.close()
