import pandas as pd

df_csv = pd.read_csv("files/IMDB-Movie-Data.csv")

print('DataFrame with CSV:')
print(df_csv)
# output:
#      Rank                    Title  ... Revenue (Millions) Metascore
# 0       1  Guardians of the Galaxy  ...             333.13      76.0
# 1       2               Prometheus  ...             126.46      65.0
# 2       3                    Split  ...             138.12      62.0
# 3       4                     Sing  ...             270.32      59.0
# 4       5            Suicide Squad  ...             325.02      40.0
# ..    ...                      ...  ...                ...       ...
# 995   996     Secret in Their Eyes  ...                NaN      45.0
# 996   997          Hostel: Part II  ...              17.54      46.0
# 997   998   Step Up 2: The Streets  ...              58.01      50.0
# 998   999             Search Party  ...                NaN      22.0
# 999  1000               Nine Lives  ...              19.64      11.0

# Checking nullable values
nullableValues = df_csv.isnull().sum()
print(nullableValues)
# output:
# Rank                    0
# Title                   0
# Genre                   0
# Description             0
# Director                0
# Actors                  0
# Year                    0
# Runtime (Minutes)       0
# Rating                  0
# Votes                   0
# Revenue (Millions)    128 <- there are 128 rows, the value of column Revenue is null
# Metascore              64 <- there are 64 rows, the value of column Metascore is null
# dtype: int64

# Delete nullable rows
df_deleted_null = df_csv.dropna()
print(df_deleted_null.isnull().sum())

print(df_csv[df_csv['Metascore'].isnull()])