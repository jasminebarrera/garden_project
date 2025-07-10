import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from my_funcs import show_data_overview, show_crop_overview, show_n_by_col

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# READ IN DATA
harvest_df = pd.read_csv("harvest_2020.csv")
harvest_df = harvest_df.rename(columns= {'vegetable': 'crop'})

# DATA OVERVIEW
# print(show_data_overview(harvest_df))

#####################################
# IN-DEPTH EDA
#####################################
## Harvest Frequency by Crop
# harvest_count_df = harvest_df.groupby(["crop"])["date"].count().reset_index().rename(columns= {'date':'harvest frequency'})
# top_n_freq, bottom_n_freq = show_n_by_col(harvest_count_df, "harvest frequency", 10, 5)

## Crop Yields by Harvest Weight
harvest_weight_sum_df = harvest_df.groupby(["crop"])["weight"].sum().reset_index().rename(columns= {'weight':'total weight'})
top_n_weight, bottom_n_weight = show_n_by_col(harvest_weight_sum_df, "total weight", 1, 1)

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

## Crop Variety Productivity by Harvest Weight
# unique_crops = harvest_df["crop"].unique() #.astype(str).tolist()
# crop_dict = dict.fromkeys(unique_crops)
#
# for crop in unique_crops:
#     crop_list = harvest_df.loc[harvest_df["crop"] == crop]
#     grouped_crop_var = crop_list.groupby(["variety"])["weight"].sum().reset_index().rename(columns= {'weight':'total weight'})
#     crop_dict[crop] = grouped_crop_var.sort_values(by=["total weight"], ascending=False)[0:5]
#
# print(unique_crops)
# show_crop_overview(crop_dict)