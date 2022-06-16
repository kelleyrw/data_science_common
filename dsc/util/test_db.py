from sqlalchemy import create_engine

from dsc.util.db import RunQuery
from dsc.util.pd import print_dataframe


def test_RunQuery():
    engine = create_engine("sqlite://", connect_args={"timeout": 5})
    run_sql = RunQuery(engine)
    print_dataframe(run_sql("select 1 as foo"))
    run_sql("select 1 as foo", verbose=True)
    run_sql("select 1 as Foo", verbose=True, display=True)
