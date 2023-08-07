import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv("files/pokemon.csv", index_col=0, encoding="unicode_escape")

sns.lmplot(data=pokemon_df, x="Attack", y="Defense", fit_reg=True, hue="Generation")

# HEATMAP
selectedPokemonColumns_df = pokemon_df[["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]]
correlation = selectedPokemonColumns_df.corr()

sns.heatmap(correlation)

# HISTOGRAM
sns.histplot(pokemon_df["Attack"])

# BAR CHART
sns.countplot(data=pokemon_df, x="Type 1")
plt.xticks(rotation=-45)
plt.show()