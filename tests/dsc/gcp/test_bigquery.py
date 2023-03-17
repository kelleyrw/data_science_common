# Standard library imports
import unittest
from os import getenv

# Third party imports
from dotenv import load_dotenv

# DSC imports
from dsc.gcp.bigquery import RunBigQuery, create_bq_engine
from dsc.util.db import RunQuery

load_dotenv(verbose=True, dotenv_path=".envrc")

only_if_credentials_available = unittest.skipIf(
    getenv("GCP_CREDENTIALS") is None
    or getenv("GCP_TEST_PROJECT") is None
    or getenv("GCP_TEST_DATASET") is None,
    "no gcp credentials specified",
)


# TODO: add credentials for CI/CD
class TestBigQuery(unittest.TestCase):
    project = getenv("GCP_TEST_PROJECT")
    dataset = getenv("GCP_TEST_DATASET")

    @only_if_credentials_available
    def test_create_bq_engine(self) -> None:
        engine = create_bq_engine(
            project=self.project,
            dataset=self.dataset,
        )
        run_sql = RunQuery(engine)
        run_sql("select 1 as foo", verbose=True, display=True)

    @only_if_credentials_available
    def test_RunBigQuery(self) -> None:
        with self.subTest("defaults"):
            run_sql = RunBigQuery()
            run_sql("select 1 as foo", verbose=True, display=True)

        with self.subTest("progress bar"):
            run_sql = RunBigQuery()
            run_sql(
                "select 1 as foo", verbose=True, display=True, display_progress_bar=True
            )

        with self.subTest("project"):
            run_sql = RunBigQuery(project=self.project)
            run_sql("select 1 as foo", verbose=True, display=True)

        with self.subTest("multi-query"):
            ds = self.dataset
            run_sql = RunBigQuery()
            try:
                run_sql(
                    f"""\
                create or replace table {ds}.foo (
                    f1 int64
                );

                insert into {ds}.foo
                select 1
                union all
                select 2
                ;

                select * from {ds}.foo
                ;
                """,
                    verbose=True,
                    display=True,
                )
            finally:
                run_sql(f"drop table if exists {ds}.foo", verbose=True)


if __name__ == "__main__":
    unittest.main()
