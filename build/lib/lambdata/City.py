#my_lambdata/assignment.py

from pandas import DataFrame

# TODO: helper function from Assignment
# State abbreviation - Full name and vice versa
# FL - Florida etc


def add_state_names_columns(my_df):
    """
    Add a column of corresponding state names to a DataFrame
    Params(my_df) a DataFrame with a column called 'abbrev' that has state abbreviations
    Return a copy of the original DataFrame but with an extra column
    """
    new_df = my_df.copy()
    names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn'}
    # see this link; https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    new_df['name'] = new_df['abbrev'].map(names_map)

    return new_df
    #new_df


if __name__ == "__main__":
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

mapped_df = add_state_names_columns(df)
print(mapped_df.head())
