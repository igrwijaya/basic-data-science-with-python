import sqlite3
import pandas as pd

pd.options.display.width = 0

conn = sqlite3.connect("data/chinook.db")

sql_df = pd.read_sql_query("select * from invoices ORDER BY InvoiceDate DESC", conn)
print(sql_df)

#chinook_df = pd.read_sql_query("select * from customers where Country='Norway' ", conn)
#chinook_df = pd.read_sql_query("select * from customers where Fax IS NULL ", conn)
# chinook_df = pd.read_sql_query("select * from customers where Fax IS NULL and State IS NULL", conn)
# print(chinook_df)