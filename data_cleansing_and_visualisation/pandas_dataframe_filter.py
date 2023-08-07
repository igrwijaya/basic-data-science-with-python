import sqlite3
import pandas as pd

conn = sqlite3.connect('files/sqlite3.db')

tweets_df = pd.read_sql_query('select * from tweets', conn)

# FILTER COLUMN
df_filter_column = tweets_df[['username', 'retweet_count']]
print(df_filter_column.head())
# output:
#           username retweet_count
# 0  kembarannyaimas             0
# 1     Rian170363Az             0
# 2         ayu_yude             0
# 3         cak_iwan             0
# 4        vayakikin             0

# FILTER VALUES
df_filter_value = tweets_df[tweets_df['username'].isin(['cak_iwan', 'ayu_yude'])]
print(df_filter_value)
# output:
#    username                                               text retweet_count
# 2  ayu_yude  RT @jokowi: Semenjak dari awal, saya mengingat...             0
# 3  cak_iwan  RT @septian: Sekadar mengingatkan: hasil uji k...             0


# FILTER VALUES CAST
df_filter_value_cast = tweets_df[tweets_df['retweet_count'].astype(int) == 0]
print(df_filter_value_cast)
# output:
#              username  ... retweet_count
# 0     kembarannyaimas  ...             0
# 1        Rian170363Az  ...             0
# 2            ayu_yude  ...             0
# 3            cak_iwan  ...             0
# 4           vayakikin  ...             0
# ...               ...  ...           ...
# 5634    endanghidayat  ...             0
# 5635  Akun_Purwokerto  ...             0
# 5636          AA_Gum_  ...             0
# 5637  BaksoAc10516490  ...             0
# 5638     indraanurdin  ...             0

