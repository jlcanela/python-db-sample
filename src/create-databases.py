import mysql.connector
conn = mysql.connector.connect(user="root",passwd="MYSQL_ROOT_PASSWORD", auth_plugin="mysql_native_password")

c = conn.cursor()
c.execute('DROP DATABASE logging')
c.execute('CREATE DATABASE logging')
c.execute('SHOW DATABASES')
print(c.fetchall())

