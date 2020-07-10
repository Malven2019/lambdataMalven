# write some code using pytest to test our
# add_state_names_column() works as desired

from pandas import DataFrame

from lambdata.assignment import add_state_names_columns


def test_add_state_names(self):
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())
    # ensure that our test is setup properly
    # self.assertEqual(len(df.columns), 1)
    # self.assertEqual(list(df.columns), ['abbrev'])
    # self.assertEqual(df.iloc[0]['abbrev'], 'CA')

    assert len(df.columns) == 1
    assert list(df.columns) == ['abbrev']
    assert (df.iloc[0]['abbrev'] == 'CA'

    # What code can we write, referencing df to know if
    # our function did what it was supposed to do
    # (adding a column to corresponding state names)
    mapped_df = add_state_names_columns(df)

    # self.assertEqual(len(mapped_df.columns), 2)
    # self.assertEqual(list(mapped_df.columns), ['abbrev', 'name'])
    # self.assertEqual(mapped_df.iloc[0]['abbrev'], 'CA')
    # self.assertEqual(mapped_df.iloc[0]['name'], 'Cali')
    assert len(mapped_df.columns) == 2
    assert list(mapped_df.columns) == ['abbrev', 'name']
    assert mapped_df.iloc[0]['abbrev'] == 'CA'
    assert mapped_df.iloc[0]['name'] == 'Cali'
