import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_funcs import show_data_overview

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# READ IN DATA
harvest_df = pd.read_csv("harvest_2020.csv")
planting_df = pd.read_csv("planting_2020.csv")

# DATA OVERVIEW
print(show_data_overview(harvest_df))
print(show_data_overview(planting_df))

# DATA ANALYSIS
# vegetables = harvest_df["vegetable"].unique()
# veg_weights = harvest_df.groupby(["vegetable", "variety"])["weight"].median().reset_index()
#
# sns.histplot(harvest_df["weight"])
# plt.show()

# for vegetable in vegetables:
#     print(veg_weights.loc[veg_weights["vegetable"] == vegetable])

# tomatoes = veg_weights.loc[veg_weights["vegetable"] == "tomatoes"]
# print(tomatoes.sort_values("weight", ascending=False))



# print(sorted(vegetables))
# tomatoes_df = harvest_df.loc[harvest_df["vegetable"] == "tomatoes"]
# print(tomatoes_df["variety"].unique())
# print(tomatoes_df)

# sns.barplot(x="vegetable", y="weight", data=veg_weights)
# # plt.bar("vegetable", "weight")
# plt.savefig("barplot_veg")

