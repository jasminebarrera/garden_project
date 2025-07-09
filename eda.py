import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_funcs import show_data_overview, show_vegetable_overview, show_n_by_col

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# READ IN DATA
harvest_df = pd.read_csv("harvest_2020.csv")

# DATA OVERVIEW
# print(show_data_overview(harvest_df))
# print(harvest_df[harvest_df["vegetable"] == "apple"])

#####################################
# IN-DEPTH EDA
#####################################
## Harvest Frequency by Vegetable
# harvest_count_df = harvest_df.groupby(["vegetable"])["date"].count().reset_index().rename(columns= {'date':'harvest frequency'})
# show_n_by_col(harvest_count_df, "harvest frequency", 10, 5)

## Vegetable Productivity by Harvest Weight
harvest_weight_sum_df = harvest_df.groupby(["vegetable"])["weight"].sum().reset_index().rename(columns= {'weight':'total weight'})
show_n_by_col(harvest_weight_sum_df, "total weight", 5, 5)

# sorted_harvest_df_top = harvest_weight_sum_df.sort_values(by=["total weight"], ascending=False)[0:5]
# sorted_harvest_df_bottom = grouped_harvest_df.sort_values(by=["total weight"], ascending=True)[0:5]

# sns.catplot(data=, x="vegetable", y="total weight", kind='bar', errorbar=None, legend_out=False)
# plt.xticks(rotation=25)
# plt.show()
# plt.clf()
# plt.close()
#
# sns.catplot(data=sorted_harvest_df_bottom, x="vegetable", y="total weight", kind='bar', errorbar=None, legend_out=False)
# plt.xticks(rotation=25)
# plt.show()
# plt.clf()
# plt.close()

## Vegetable Variety Productivity by Harvest Weight
# unique_vegetables = harvest_df["vegetable"].unique() #.astype(str).tolist()
# veg_dict = dict.fromkeys(unique_vegetables)
#
# for vegetable in unique_vegetables:
#     veg_list = harvest_df.loc[harvest_df["vegetable"] == vegetable]
#     grouped_veg_var = veg_list.groupby(["variety"])["weight"].sum().reset_index().rename(columns= {'weight':'total weight'})
#     veg_dict[vegetable] = grouped_veg_var.sort_values(by=["total weight"], ascending=False)[0:5]
#
# print(unique_vegetables)
# show_vegetable_overview(veg_dict)