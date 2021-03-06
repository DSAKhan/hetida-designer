import pandas as pd
from .nth_root import main


def test_numeric():
    assert main(data=8, n=3)["root"] == 2


def test_series_numeric():
    assert main(
        data=pd.Series(
            {
                "2019-08-01T15:20:12": 4,
                "2019-08-01T15:44:12": None,
                "2019-08-03T16:20:15": 16,
                "2019-08-05T12:00:34": 0.25,
            }
        ),
        n=2,
    )["root"].equals(
        pd.Series(
            {
                "2019-08-01T15:20:12": 2,
                "2019-08-01T15:44:12": None,
                "2019-08-03T16:20:15": 4,
                "2019-08-05T12:00:34": 0.5,
            }
        )
    )


def test_df_numeric():
    assert main(
        data=pd.DataFrame(
            {
                "a": {
                    "2019-08-01T15:20:12": 4,
                    "2019-08-01T15:44:12": 9,
                    "2019-08-03T16:20:15": 0,
                    "2019-08-05T12:00:34": 1,
                },
                "b": {
                    "2019-08-01T15:20:12": 625,
                    "2019-08-01T15:44:12": None,
                    "2019-08-03T16:20:15": 0.25,
                    "2019-08-05T12:00:34": 4,
                },
            }
        ),
        n=2,
    )["root"].equals(
        pd.DataFrame(
            {
                "a": {
                    "2019-08-01T15:20:12": 2.0,
                    "2019-08-01T15:44:12": 3.0,
                    "2019-08-03T16:20:15": 0.0,
                    "2019-08-05T12:00:34": 1.0,
                },
                "b": {
                    "2019-08-01T15:20:12": 25.0,
                    "2019-08-01T15:44:12": None,
                    "2019-08-03T16:20:15": 0.5,
                    "2019-08-05T12:00:34": 2.0,
                },
            }
        )
    )


def test_series_empty_numeric():
    assert main(data=pd.Series(dtype=float), n=2)["root"].empty


def test_numeric_empty_series():
    assert main(n=pd.Series(dtype=float), data=2)["root"].empty
