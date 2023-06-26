def identify_and_remove_duplicated_data(df):
    if df.duplicated().sum() > 0:
        # identify duplicated data
        print("# of duplicated rows:", df.duplicated().sum())

        # drop the duplicated rows, and only keep first apperance
        df_cleaned = df.drop_duplicates(keep='first')

        print("shape of data before removing duplicated data", df.shape)
        print("shape of data after duplicated data", df_cleaned.shape)
    else:
        print("No duplicated data found")
        df_cleaned = df

    return df_cleaned