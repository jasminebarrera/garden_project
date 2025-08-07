import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from eda_funcs import missing_data_overview, get_col_dtypes

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

### IMPORT AND INSPECT DATA
# Read in the data
harvesting_data = pd.read_csv('../garden_data/harvest_2020.csv')

### BASIC EDA
## Harvest data
#
# # Get quick look at data
# print(harvesting_data.head(10))
#
# # Get data shape
# print(harvesting_data.shape)
#
# # Get data types
# print(harvesting_data.dtypes)
#
# # Check specific data types of columns
# get_col_dtypes(harvesting_data)
#
# # Look over missing data
# print(missing_data_overview(harvesting_data))
#
# Note: no missing data for this dataset.

### PREPARE AND TRANSFORM DATA
## Harvesting dataset

# Rename columns
harvesting_df = harvesting_data.rename(columns={'vegetable': 'crop'})

# Change data types
harvesting_df['date'] = pd.to_datetime(harvesting_df['date']).dt.date

# Check changes
# print(harvesting_df.head(5))
# print(get_col_dtypes(harvesting_df))
# print(missing_data_overview(harvesting_df))

## Add clean datasets to csv for further reporting
# harvesting_df.to_csv('/home/jasmine/Documents/data/harvesting_2020_clean.csv', encoding='utf-8', index=False)

### Analyzing data characteristics
# sns.histplot(spending_df['price'])
# plt.show()



### IN-DEPTH EDA

