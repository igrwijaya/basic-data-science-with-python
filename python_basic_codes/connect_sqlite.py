import sqlite3
import pandas as pd

conn = sqlite3.connect("data/binar_academy.db")

print("Opened database successfully")

conn.execute('''DROP TABLE users;''')
conn.execute(''' CREATE TABLE users(username varchar(255), email varchar(255)); ''')
conn.execute(''' INSERT INTO users(username, email) VALUES('igrwijaya', 'igrwijaya@test.com') ''')
conn.execute('''UPDATE users set username='Wijaya' where email='igrwijaya@test.com'; ''')

sql_df = pd.read_sql_query('select * from users', conn)
print(sql_df)