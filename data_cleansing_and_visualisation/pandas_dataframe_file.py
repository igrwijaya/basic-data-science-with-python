import pandas as pd

df = pd.read_json("files/purchases.json")
print('DataFrame with JSON:')
print(df)
# output:
# DataFrame with JSON:
#        apples  oranges
# June         3        0
# Robert       2        3
# Lily         0        7
# David        1        2
#

df_csv = pd.read_csv("files/purchases.csv")

print('DataFrame with CSV:')
print(df_csv)
# output:
# DataFrame with CSV:
#  Unnamed: 0  apples  oranges
# 0       June       3        0
# 1     Robert       2        3
# 2       Lily       0        7
# 3      David       1        2

df_csv_0_col = pd.read_csv("files/purchases.csv", index_col=0, delimiter=',')

print('DataFrame with CSV v2:')
print(df_csv_0_col)
# output:
# DataFrame with CSV v2:
#        apples  oranges
# June         3        0
# Robert       2        3
# Lily         0        7
# David        1        2

# Export
df_csv_0_col.to_json("files/export/purchases.json")