import pandas as pd
import numpy as np
from eda_funcs import missing_data_overview, get_col_dtypes

# SETTINGS
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

### IMPORT AND INSPECT DATA
# Read in the data
spending_data = pd.read_csv('../garden_data/spending_2020.csv')
planting_data = pd.read_csv('../garden_data/planting_2020.csv')
harvesting_data = pd.read_csv('../garden_data/harvest_2020.csv')


### BASIC EDA
# Spending dataset

# Get quick look at data
print(spending_data.head(10))

# Get data shape
print(spending_data.shape)

# Get data types
print(spending_data.dtypes)

# Check specific data types of columns
get_col_dtypes(spending_data)

# Look over missing data
print(spending_data.isnull().sum().sum())
print(spending_data.isnull().sum())

# Look further into missing data
print(spending_data[spending_data['brand'].isnull()])
print(spending_data[spending_data['eggplant_item_number'].isnull()])

# Planting data

# Get quick look at data
print(planting_data.head(10))

# Get data shape
print(planting_data.shape)

# Get data types
print(planting_data.dtypes)

# Check specific data types of columns
get_col_dtypes(planting_data)

# Look over missing data
print(missing_data_overview(planting_data))

# Look further into missing data
print(planting_data[planting_data['number_seeds_planted'].isnull()])
print(planting_data[planting_data['date'].isnull()])
print(planting_data[planting_data['number_seeds_exact'].isnull()])

# Look at non-null record in mostly NaN column
print(planting_data[planting_data['notes'].notnull()])

# Harvest data

# Get quick look at data
print(harvesting_data.head(10))

# Get data shape
print(harvesting_data.shape)

# Get data types
print(harvesting_data.dtypes)

# Check specific data types of columns
get_col_dtypes(harvesting_data)

# Look over missing data
print(missing_data_overview(harvesting_data))

# Note: no missing data for this dataset...

# Look into strawberry harvest data to see help decide what to do about strawberry planting missing values:
print(harvesting_data[harvesting_data['vegetable'] == 'strawberries'])


### PREPARE AND TRANSFORM DATA
## Spending dataset
# Drop columns
spending_to_drop = ['eggplant_item_number', 'price_with_tax']
spending_df = spending_data.drop(spending_to_drop, axis=1)

# Fill in missing values
spending_df['brand'] = spending_df['brand'].replace(np.nan, 'unknown')

# Rename columns
spending_df = spending_df.rename(columns={'vegetable': 'item_name'})

# Fix misspellings
spending_df['variety'] = spending_df['variety'].str.replace("Cinderella's Carraige", "Cinderella's Carriage")

## Planting dataset

# Drop rows
i_tomato = planting_data.loc[planting_data['notes'].notnull()].index
i_strawberry = planting_data.loc[planting_data['date'].isnull()].index

planting_df = planting_data.drop(i_tomato)
planting_df = planting_df.drop(i_strawberry)

# Drop columns
planting_df = planting_df.drop(['notes'], axis=1)

# Rename columns
planting_df = planting_df.rename(columns={'vegetable': 'crop'})

# Change data types
planting_df['number_seeds_planted'] = planting_df['number_seeds_planted'].astype(int)
planting_df['date'] = pd.to_datetime(planting_df['date']).dt.date

# Fix misspellings
planting_df['variety'] = planting_df['variety'].str.replace("Cinderella's Carraige", "Cinderella's Carriage")

## Harvesting dataset

# Rename columns
harvesting_df = harvesting_data.rename(columns={'vegetable': 'crop'})

# Change data types
harvesting_df['date'] = pd.to_datetime(harvesting_df['date']).dt.date

# Fix misspellings
harvesting_df['variety'] = harvesting_df['variety'].str.replace("Cinderella's Carraige", "Cinderella's Carriage")

## Check changes
print(spending_df.head(5))
print(get_col_dtypes(spending_df))
print(missing_data_overview(spending_df))

print(planting_df.head(5))
print(get_col_dtypes(planting_df))
print(missing_data_overview(planting_df))

print(harvesting_df.head(5))
print(get_col_dtypes(harvesting_df))
print(missing_data_overview(harvesting_df))


## Add clean datasets to csv
spending_df.to_csv('../garden_data/spending_2020_clean.csv', encoding='utf-8', index=False)
planting_df.to_csv('../garden_data/planting_2020_clean.csv', encoding='utf-8', index=False)
harvesting_df.to_csv('../garden_data/harvest_2020_clean.csv', encoding='utf-8', index=False)
