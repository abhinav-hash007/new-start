# import mysql.connector
# from mysql.connector import Error

# try:
#     # Connect to MariaDB/MySQL
#     connection = mysql.connector.connect(
#         host='localhost',
# #         user='root',
# #         password='your_password',  # 🔒 Replace with your actual root password
# #         database='test_db'         # 🧪 Replace with an existing database name
# #     )

# #     if connection.is_connected():
# #         print("✅ Python successfully connected to MySQL!")
# #         cursor = connection.cursor()
# #         cursor.execute("SELECT DATABASE();")
# #         db_name = cursor.fetchone()[0]
# #         print(f"📦 Current database: {db_name}")

# # except Error as e:
# #     print("❌ Error while connecting to MySQL:", e)

# # finally:
# #     if 'connection' in locals() and connection.is_connected():
# #         cursor.close()
# #         connection.close()
# #         print("🔒 MySQL connection closed.")
# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='your_secure_password',  # match the one you just set
#         database='test_db'
#     )

#     if connection.is_connected():
#         print("✅ Connected to MySQL!")
#         cursor = connection.cursor()
#         cursor.execute("SELECT DATABASE();")
#         print("📦 Current database:", cursor.fetchone()[0])

# except Error as e:
#     print("❌ Connection error:", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("🔒 Connection closed.")
import mysql connector 
a = ("tiger is something")
b = ("tiger is sonething")
c = ("tiger is something")
d = ("")