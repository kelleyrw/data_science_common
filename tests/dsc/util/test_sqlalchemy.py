# Third party imports
from sqlalchemy import Column, Integer, create_engine, select
from sqlalchemy.ext.declarative import declarative_base

# DSC imports
from dsc.util.sqlalchemy import compiled_query, print_compiled_query

base = declarative_base()


class Foo(base):  # type: ignore
    __tablename__ = "foo"

    c1 = Column(Integer, primary_key=True)


def test_compiled_query() -> None:
    engine = create_engine("sqlite://")
    expr = select(Foo).limit(3)
    expr_str = compiled_query(engine, expr)
    print(expr_str)


def test_print_compiled_query() -> None:
    engine = create_engine("sqlite://")
    expr = select(Foo).limit(3)
    print_compiled_query(engine, expr)
