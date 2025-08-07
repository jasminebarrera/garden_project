def get_col_dtypes(df):
    column_list = df.columns.tolist()
    column_type_dict = dict.fromkeys(column_list)

    for key in column_type_dict:
        column_type_dict[key] = type(df.loc[0, key])

    return column_type_dict


def missing_data_overview(df):

    # Look over missing data
    num_missing_records = df.isnull().any(axis=1).sum()
    print(f"\nNumber of records with at least one missing value:\n{num_missing_records}\n")

    print("Number of missing values by column:\n")
    print(df.isnull().sum())
