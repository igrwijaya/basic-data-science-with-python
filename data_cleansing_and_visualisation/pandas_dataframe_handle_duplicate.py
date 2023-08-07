import sqlite3
import pandas as pd

data = {
    'apples': [3,3,0,1],
    'gold': [3,2,0,1],
    'oranges': [3,1,7,2]
}


# Import
purchase_df = pd.DataFrame(data)
print(purchase_df)

print(purchase_df.drop_duplicates())