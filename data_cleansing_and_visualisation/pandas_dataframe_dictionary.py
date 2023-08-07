import pandas as pd
import re

# Todo with Pandas:
# Dataframe = table
# import csv, json, sql to dataframe
# export dataframe to csv or json
# searching in dataframe
# fix duplicate and missing values

data = {
    'apples': [3,2,0,1],
    'oranges': [0,3,7,2]
}


# Import
purchase_df = pd.DataFrame(data)
print(purchase_df)
# output:
#    apples  oranges
# 0       3        0
# 1       2        3
# 2       0        7
# 3       1        2

# Export
purchase_df.to_csv("files/export/dict.csv")