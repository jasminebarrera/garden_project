def show_data_overview(df):
    # df.attrs['name']
    num_rows = df.shape[0]
    num_columns = df.shape[1]
    df_head = df.head()
    stat_summary = df.describe(include="all")

    overview_message = (f"There are {num_rows} rows and {num_columns} columns in the dataframe."
                        f"\n\nHere is a quick view of the data in the dataframe:\n{df_head}"
                        f"\n\nAnd here are the summary statistics:\n{stat_summary}\n\n\n")

    return overview_message
