import matplotlib.pyplot as plt
import seaborn as sns

def show_data_overview(df):
    # df.attrs['name']
    num_rows = df.shape[0]
    num_columns = df.shape[1]
    df_head = df.head()
    stat_summary = df.describe(include="all")

    overview_message = (f"\nThere are {num_rows} rows and {num_columns} columns in the dataframe."
                        f"\n\nHere is a quick view of the data in the dataframe:\n{df_head}"
                        f"\n\nAnd here are the summary statistics:\n{stat_summary}\n\n\n")

    return overview_message

def show_crop_overview(my_dict):
    crop_choice = input("What crop are you interested in?\n")
    crop_variety_info = my_dict[crop_choice]
    
    return crop_variety_info

def is_plural(var):
    var_is_plural = False

    if var > 1:
        var_is_plural = True

    return var_is_plural

def show_n_by_col(df, column: str, top_n: int, bottom_n: int):
    top_n = top_n
    bottom_n = bottom_n

    top_is_plural = is_plural(top_n)
    bottom_is_plural = is_plural(bottom_n)

    top_n_vals = df.sort_values(by=[column], ascending=False)[0:top_n]
    bottom_n_vals = df.sort_values(by=[column], ascending=True)[0:bottom_n]

    if top_is_plural:
        print(f"\nTop {top_n} Harvested Crops:\n", top_n_vals, "\n")
    else:
        print(f"\nMost Harvested Crop:\n", top_n_vals, "\n")

    if bottom_is_plural:
        print(f"\nBottom {bottom_n} Harvested Crops:\n", bottom_n_vals, "\n")
    else:
        print(f"\nLeast Harvested Crop:\n", bottom_n_vals, "\n")

    return top_n_vals, bottom_n_vals


### Unnecessary...
# class GroupSortedDf:
#     def __init__(self, df, x, by_col, y):
#         self.df = df
#         self.x = x
#         self.by_col = by_col
#         self.y = y
#
#         self.grouped_df = None
#         self.sorted_group_df = None
#
#
#     def get_group_df(self):
#         grouped_df = self.df.groupby([self.x])[self.by_col].sum().reset_index().rename(columns={self.by_col: self.y})
#
#         return grouped_df
#
#     def get_sorted_df(self, n):
#         top_n = self.grouped_df.sort_values(by=[self.y], ascending=False)[0:n]
#
#         return top_n
#
#     def get_grouped_sorted_top_n(self, n):
#         grouped_df = self.get_group_df()
#         top_n = self.get_sorted_df(n)
#