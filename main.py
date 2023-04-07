from account_transactions.settings import OPERATIONS
from account_transactions.src.exceptions import FileNotFoundException
from account_transactions.src.models.database import Data


def main():
    data = []
    database = Data(OPERATIONS)
    try:
        data = database.get_data()
    except FileNotFoundException as e:
        print(e.message)
    if data:
        database.get_result(data)


if __name__ == '__main__':
    main()
