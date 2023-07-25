import pathlib
import pandas as pd

_DATASETS_DIR = pathlib.Path(__file__).resolve().parent / 'datasets'


def main():
    customers = pd.read_csv(_DATASETS_DIR / 'customers.csv')

    print('Uncompressed: \n')
    print(130 * '-')
    print(customers.memory_usage(deep=True))
    print(customers.dtypes)

    customers_cp = customers.copy()
    customers_cp['customer_city'] = customers_cp['customer_city']\
        .astype('category')
    customers_cp['customer_state'] = customers_cp['customer_state']\
        .astype('category')

    print(130 * '-')
    print('Compressed: \n', customers_cp.memory_usage(deep=True))
    print(customers_cp.dtypes)


if __name__ == "__main__":
    main()
