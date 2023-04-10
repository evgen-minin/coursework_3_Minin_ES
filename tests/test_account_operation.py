from src.models.account_operation import Operation


def test_encode_from_to():
    # Тест проверяет, что метод encode_from_to скрывает номер карты
    operation = Operation(1, 'test', '2022-01-01T00:00:00.000000', {'amount': '1000', 'currency': {'name': 'USD'}},
                          'test', 'Счет 1234', 'Карта 1234')
    assert operation.encode_from_to('Счет 1234') == 'Счет **34'
    assert operation.encode_from_to('Карта 1234') == 'Карта ******1234'


def test_get_info_operation():
    # Тест проверяет, что метод get_info_operation возвращает строку в ожидаемом формате
    operation = Operation(1, 'test', '2022-01-01T00:00:00.000000', {'amount': '1000', 'currency': {'name': 'USD'}},
                          'test', 'Счет 1234', 'Карта 1234')
    expected_output = '01.01.2022 test\nСчет **34 -> Карта ******1234\n1,000.00 USD'
    assert operation.get_info_operation() == expected_output
