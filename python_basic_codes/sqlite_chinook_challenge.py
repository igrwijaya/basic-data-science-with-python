#1. Ambil semua list playlist name secara unique kecuali TV Shows, tampilkan datanya sesuai abjad.
#2. Coba tampilkan total pembayaran invoice dari masing-masing customer selama tahun 2010 sampai 2014
#3. Dari jawaban nomor 2, coba filter hanya data customer yang total invoice nya diatas 35$ saja
#4. Ambil data customer id, email, address, country, dan tambahkan 1 column sebagai flagging untuk menunjukkan apakah country asal customer tersebut dari ‘USA’ atau ‘Not USA’. Nama column nya adalah is_usa
#5. Ambil data customer id, first name, last name, phone, dan address hanya jika si customer tersebut pernah punya invoice.

import sqlite3
import pandas as pd

pd.options.display.width = 0

conn = sqlite3.connect("data/chinook.db")

## ANSWER 1
print("ANSWER 1 -----------------------------------------")
playlist_df = pd.read_sql_query("SELECT DISTINCT Name FROM playlists WHERE Name != 'TV Shows' ORDER BY Name ASC", conn)
print(playlist_df)
print("-----------------------------------------\n")

## ANSWER 2
print("ANSWER 2 -----------------------------------------")
invoiceQuery = "SELECT CustomerId, SUM(Total) FROM invoices WHERE InvoiceDate BETWEEN '2010-01-01' AND '2014-12-31' GROUP BY CustomerId"
invoice_df = pd.read_sql_query(invoiceQuery, conn)
print(invoice_df)
print("-----------------------------------------\n")

## ANSWER 3
print("ANSWER 3 -----------------------------------------")
invoice_35_df = pd.read_sql_query(invoiceQuery + " HAVING SUM(Total) > 35", conn)
print(invoice_35_df)
print("-----------------------------------------\n")

## ANSWER 4
print("ANSWER 4 -----------------------------------------")
customer_df = pd.read_sql_query("SELECT CustomerId, Email, Address, Country, CASE WHEN Country = 'USA' THEN 'USA' ELSE 'NOT USA' END AS is_usa FROM customers ", conn)
print(customer_df)
print("-----------------------------------------\n")

## ANSWER 5
print("ANSWER 5 -----------------------------------------")
customer_inv_df = pd.read_sql_query("SELECT CustomerId, FirstName, LastName, Phone, Address FROM customers WHERE EXISTS(SELECT InvoiceId FROM invoices WHERE invoices.CustomerId = customers.CustomerId)", conn)
print(customer_inv_df)