import json
import os
from account_transactions.src.exceptions import FileNotFoundException
from account_transactions.src.models.account_operation import Operation


class Data:
    def __init__(self, filename: str):
        self.filename = filename

    def get_data(self) -> list[dict]:
        """
        Метод считывает данные из json файла.
        :return: Возвращает список словарей из json файла.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        raise FileNotFoundException()

    def get_operations(self, operations: list[dict]) -> list[Operation]:
        data_list: list[Operation] = []
        for operation in operations:
            if 'from' in operation:
                operation['from_'] = operation.pop('from')
                data_list.append(Operation(**operation))
        return data_list

    def get_five_operations(self, operations: list[dict]) -> list[Operation]:
        operations = self.get_operations(operations)
        length = 5 if len(operations) > 5 else len(operations)
        return sorted(operations,
                      key=lambda operation_data: (operation_data.state, operation_data.date),
                      reverse=True)[:length]

    def get_result(self, data: list[dict]) -> bool:
        five_operations: list[Operation] = self.get_five_operations(data)
        for operation in five_operations:
            print(f'{operation.get_info_operation()}\n')
        return True
