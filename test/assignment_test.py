# write some code using unittest to test our
# add_state_names_columns assignment

import unittest
from pandas import DataFrame

from lambdata.assignment import add_state_names_columns


class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
        df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
        print(df.head())
        breakpoint()
        mapped_df = add_state_names_columns(df)
        print(mapped_df.head())


if __name__ == '__main__':
    unittest.main()  # Invoking all our class test methods
