# Third party imports
import pandas as pd

# DSC imports
from dsc.util.pd import print_dataframe, tabulate_dataframe


def test_tabluate():
    df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    tabulate_dataframe(df)


def test_print_dataframe():
    df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    print_dataframe(df)
