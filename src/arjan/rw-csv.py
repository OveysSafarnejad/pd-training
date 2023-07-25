import pathlib
from pathlib import Path

import pandas as pd
from pandas import DataFrame


_DATASETS_DIR = pathlib.Path(__file__).resolve().parent / 'datasets'


def read_data(filename: str) -> DataFrame:
    # airports = pd.read_csv(_DATASETS_DIR / filename, skiprows=2)
    airports = pd.read_csv(_DATASETS_DIR / filename)
    # print(airports.info())

    airport_ds = {
        "ident": "string",
    }

    airports = airports.astype(airport_ds)
    # print(airports.info())

    airports['last_updated'] = pd.to_datetime(
        airports['last_updated']
    )
    print(airports.info())

    return airports


def main():

    read_data('airports.csv')
    pass


if __name__ == "__main__":
    main()

