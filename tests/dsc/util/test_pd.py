# Third party imports
import pandas as pd

# DSC imports
from dsc.util.pd import columns_to_snakecase, print_dataframe, tabulate_dataframe


def test_tabluate() -> None:
    df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    tabulate_dataframe(df)


def test_print_dataframe() -> None:
    df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    print_dataframe(df)


def test_columns_to_snakecase() -> None:
    df = pd.DataFrame(data={"FooBar1": [1, 2], "Foo_Bar (Two)": [3, 4]})
    expected = ["foo_bar1", "foo_bar_two"]
    print_dataframe(df)
    df = columns_to_snakecase(df)
    print_dataframe(df)
    assert df.columns.tolist() == expected
