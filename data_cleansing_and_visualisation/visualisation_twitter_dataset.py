import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

twitter_df = pd.read_csv("files/Exercise Visualisasi Chapter 3 Topic 2.csv", index_col=0, encoding="unicode_escape")

twitter_df["TextLength"] = twitter_df["Text Tweet"].apply(len)

# Hitung banyak data pada setiap kalimat, lalu visualisasikan dengan menggunakan tipe Bar Chart
# Visualisasikan banyaknya sentiment menggunakan Pie Chart

sns.barplot(twitter_df, x="Text Tweet", y="TextLength")

plt.show()

sentiment = twitter_df.groupby(["Sentiment"]).sum()

print(sentiment)