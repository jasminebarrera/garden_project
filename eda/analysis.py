import pandas as pd
import eda_funcs as edaf

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

### IMPORT AND INSPECT DATA
# Load the data
spending_df = pd.read_csv("../garden_data/spending_2020.csv")
planting_df = pd.read_csv("../garden_data/planting_2020.csv")
harvesting_df = pd.read_csv("../garden_data/harvest_2020.csv")

## Spending data
# Get data shape
print(spending_df.shape)

# Get data types
print(spending_df.dtypes)

# Look over missing data
print(spending_df.isnull().sum().sum())
print(spending_df.isnull().sum())

# ## Planting data
# print(planting_df.shape)
#
#
# ## Harvesting data
# print(harvesting_df.shape)














# Get data shape
# df_dict = {
#     "spending_2020": spending_df,
#     "planting_2020": planting_df,
#     "harvest_2020": harvesting_df
# }
#
# for df_name, df in df_dict.items():
#     row_count = df.shape[0]
#     column_count = df.shape[1]
#
#     print(f"{df_name} dataset:\n"
#           f"{row_count} rows and {column_count} columns.\n")

# Check for missing values
# missing_bool_series = pd.isnull(spending_df["eggplant_item_number"])
# missing_eggplant_item_num_data = spending_df[missing_bool_series]
# print(missing_eggplant_item_num_data)
#
# nmv_bool_series = pd.notnull(planting_df["notes"])
# nmv_data = planting_df[nmv_bool_series]
# print(nmv_data)
#
# spending_cols_missing = spending_df.columns[spending_df.isnull().any()].tolist()
# print(spending_cols_missing)
#
# planting_cols_missing = planting_df.columns[planting_df.isnull().any()].tolist()
# print(planting_cols_missing)

# print(len(spending_df))
# print(spending_df.isnull().sum())
# print(spending_df.isnull().sum()/len(spending_df)*100)

# edaf.get_missing_val_cols(spending_df)