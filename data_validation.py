
#data validation function
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print("No data loaded")
        return False 

    # Primary Key Check
    if pd.Series(df['PRIMARY_KEY_COLUMN']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")

    # Check for nulls
    if df.isnull().values.any():
        raise Exception("Null values found")

    #you can add any validation you want

    return True



if __name__ == "__main__":

    # EXTRACCION PROCESS

    # Validate
    if check_if_valid_data(YOUR_DF):
        print("Data valid, proceed to Load stage")


    #LOAD STAGE