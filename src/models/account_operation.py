import re
from datetime import datetime


class Operation:
    def __init__(self, id, state, date, operationAmount, description, from_, to):
        self.id = id
        self.state = state
        self.date = date
        self.operation_amount = operationAmount
        self.description = description
        self.from_ = from_
        self.to = to

    def __str__(self):
        encode_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        encode_from = self.encode_from_to(self.from_)
        encode_to = self.encode_from_to(self.to)
        amount = '{:,.2f}'.format(float(self.operation_amount['amount'])).replace(',', '')
        currency = self.operation_amount['currency']['name']
        return f"{encode_date} {self.description}\n{encode_from} -> {encode_to}\n{amount} {currency}"

    def encode_from_to(self, value: str) -> str:
        """
        Метод кодирует номер карты и номер счёта.
        :param value:Номер карты или счёта.
        :return:Изменённые номер карты и номер счёта.
        """
        data = value.split()
        number_card = data[-1]
        if value.startswith('Счет'):
            data[-1] = '**' + data[-1][-4:]
            return ' '.join(data)

        hidden_number = number_card[0:6] + '******' + number_card[-4:]
        result = ' '.join(re.findall('(.{%s}|.+$)' % 4, hidden_number))
        data[-1] = result
        return ' '.join(data)

    def get_info_operation(self) -> str:
        """
        Метод возвращает строковое представление объекта операции.
        :return:
        """
        return Operation.__str__(self)
