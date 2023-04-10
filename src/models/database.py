import json
from account_transactions.src.models.account_operation import Operation


class Data:
    def __init__(self, filename: str):
        self.filename = filename

    def get_data(self) -> list[dict]:
        """
        Метод считывает данные из json файла.
        :return: Возвращает список словарей из json файла.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_operations(self, operations: list[dict]) -> list[Operation]:
        """
        Метод распаковывает список словарей.
        :param operations: Список словарей, содержащих информацию об операциях.
        :return: Список объектов класса Operation.
        """
        data_list: list[Operation] = []
        for operation in operations:
            if 'from' in operation:
                operation['from_'] = operation.pop('from')
                data_list.append(Operation(**operation))
        return data_list

    def get_five_operations(self, operations: list[dict]) -> list[Operation]:
        """
        Метод сортирует операции по дате.
        :param operations: Список словарей, содержащих информацию об операциях.
        :return: Список пяти операций отсортированных по дате.
        """
        operations = self.get_operations(operations)
        length = 5 if len(operations) > 5 else len(operations)
        return sorted(operations,
                      key=lambda operation_data: (operation_data.state, operation_data.date),
                      reverse=True)[:length]

    def get_result(self, data: list[dict]) -> bool:
        """
        Метод выводит информацию о пяти последних операциях и возвращает True.
        :param data:Список словарей, содержащих информацию об операциях.
        :return:True.
        """
        five_operations: list[Operation] = self.get_five_operations(data)
        for operation in five_operations:
            print(f'{operation.get_info_operation()}\n')
        return True
