import sqlite3
import pandas as pd

conn = sqlite3.connect('files/sqlite3.db')

sql_df = pd.read_sql_query('select * from tweets', conn)

print(sql_df)
# output:
#           username  ... retweet_count
# 0  kembarannyaimas  ...             0
# 1     Rian170363Az  ...             0
# 2         ayu_yude  ...             0
# 3         cak_iwan  ...             0
# 4        vayakikin  ...             0

# get top of data (by default with 5 data)
print(sql_df.head())

# get last of data (by default with 5 data)
print(sql_df.tail())
print(sql_df.tail(5))

# read info
print(sql_df.info())
# output:
#RangeIndex: 5639 entries, 0 to 5638
#Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
# 0   username       5639 non-null   object
# 1   text           5639 non-null   object
# 2   retweet_count  5639 non-null   object
# dtypes: object(3)
# memory usage: 132.3+ KB
# None

# read shape (total rows and total column)
print(sql_df.shape)
# output:
# (5639, 3)