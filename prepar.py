def prep_iris(df):
    """
    Takes in the iris dataframe and returns a cleaned dataframe
    Arguments: df - a pandas dataframe with the expected feature name and columns
    Returns: clean_df - a dataframe with cleaning performed on it
    
    """
    #drop columns
    df = df.drop('species_id', 1)
    #renamed species name to species
    df = df.rename(columns={"species_name" : "species"})
    #encoded categorical variables
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=[True, True])
    #concat the table
    df = pd.concat([df, dummy_df], axis=1)

    return df