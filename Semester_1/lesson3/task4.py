import random
from enum import Enum
from typing import Dict, Optional, Union


class InvalidAccountError(Exception):
    """Исключение, возникающее при работе с несуществующим или недопустимым счётом"""

    pass


class InvalidAmountError(Exception):
    """Исключение, возникающее при попытке использовать недопустимую сумму (<= 0)"""

    pass


class InvalidTypeError(Exception):
    """Исключение, возникающее при передаче данных неверного типа"""

    pass


class WithdrawError(Exception):
    """Исключение, возникающее при попытке списания суммы, превышающей баланс"""

    pass


# Диапазон допустимых номеров счетов (5-значные числа)
MIN_ACCOUNT_ID = 10_000
MAX_ACCOUNT_ID = 99_999

# Тип для сумм: допускаются целые и дробные числа
Amount = Union[float, int]


class Message(Enum):
    """Перечисление всех системных сообщений для вывода"""

    INVALID_ACCOUNT = "[WARNING] Недопустимый номер счета: #{}"
    INVALID_AMOUNT = "[ERROR] Минимальная сумма: сумма > 0"
    INVALID_TYPE = "[ERROR] Недопустимый тип данных"
    WITHDRAW_ERROR = "[WARNING] Недостаточно средств на счете"
    TRANSFER_INTO = "======= Перевод между счетами ======="
    TRANSFER_OUT = "======= Перевод ======="
    TRANSFER_INFO = (
        "Счёт отправителя: #{}\n"
        "Сумма: {}\n"
        "Счёт получателя: #{}\n"
        "====================================="
    )
    ACCOUNT_INFO_TITLE = "======= Счета пользователя ======="
    ACCOUNT_INFO = (
        "> Номер счёта: #{}\n - Баланс: {} рублей\n==================================="
    )
    ACCOUNT_CREATE = "[I] Создан счёт: #{}"
    ACCOUNT_NOT_EXISTS = "[WARNING] Счет не существует: #{}. Доступные счета: {}"
    ACCOUNT_SELECT = "[I] Выбран счет: #{}"
    ACCOUNT_CURRENT = "[I] Текущий счет: #{}"
    WITHDRAW = "[I] Списание со счета на {} рублей. "
    DEPOSIT = "[I] Пополнение счета на {} рублей. "
    VIEW_BALANCE = "[I] Баланс счета: {} рублей"


class Balance:
    """Класс для управления балансом счёта с поддержкой арифметических операций"""

    def __init__(self, balance: Amount = 0):
        self._balance: Amount = balance

    def __str__(self) -> str:
        """Возвращает строковое представление баланса"""
        return Message.VIEW_BALANCE.value.format(self._balance)

    def __iadd__(self, amount: Amount) -> "Balance":
        """Оператор += для пополнения баланса"""
        self._balance += amount
        return self

    def __isub__(self, amount: Amount) -> "Balance":
        """Оператор -= для списания средств с баланса"""
        self._balance -= amount
        return self

    def __lt__(self, other) -> bool:
        """Сравнение баланса с другим балансом или числом (<)"""
        if isinstance(other, Balance):
            return self._balance < other._balance
        return self._balance < other

    @property
    def balance(self) -> Amount:
        """Текущее значение баланса"""
        return self._balance


class Account:
    """Представляет банковский счёт с уникальным ID (5-значным числом) и балансом"""

    def __init__(self, account_id: int):
        self.account_id: int = account_id
        self.balance: Balance = Balance()


class Validator:
    """Набор статических методов для валидации входных данных"""

    @staticmethod
    def valid_account(account: int):
        """Проверяет, что номер счёта — целое число в допустимом диапазоне [10000, 99999]"""
        if not isinstance(account, int):
            raise InvalidTypeError(Message.INVALID_TYPE.value)

        if not (MIN_ACCOUNT_ID <= account <= MAX_ACCOUNT_ID):
            raise InvalidAccountError(Message.INVALID_ACCOUNT.value.format(account))

    @staticmethod
    def valid_amount(amount: Amount):
        """Проверяет, что сумма положительна и имеет допустимый тип"""
        if not isinstance(amount, (float, int)):
            raise InvalidTypeError(Message.INVALID_TYPE.value)

        if amount <= 0:
            raise InvalidAmountError(Message.INVALID_AMOUNT.value)

    @staticmethod
    def valid_withdraw(amount: Amount, balance: "Balance"):
        """Проверяет, достаточно ли средств на балансе для списания"""
        if balance < amount:
            raise WithdrawError(Message.WITHDRAW_ERROR.value)

    @staticmethod
    def valid_exist_account(account: int, accounts: Dict[int, Account]):
        """Проверяет, существует ли счёт в коллекции пользователя"""
        if account not in accounts:
            list_accounts = ", ".join(map(str, accounts.keys()))
            raise InvalidAccountError(
                Message.ACCOUNT_NOT_EXISTS.value.format(account, list_accounts)
            )


class UserBank:
    """Управляет счетами одного пользователя: создание, переводы, операции"""

    def __init__(self, name: str = "user"):
        """Инициализирует банковский профиль пользователя с первым счётом"""
        self._name = name
        self._accounts: Dict[int, Account] = {}
        self._current_account: Optional[Account] = None
        self.__initial_account()

    def check_balance(self):
        """Выводит баланс текущего счёта"""
        print(self._current_account.balance)

    def deposit(self, amount: Amount):
        """Пополняет текущий счёт на указанную сумму (> 0)"""
        try:
            Validator.valid_amount(amount)
            self._current_account.balance += amount
            print(Message.DEPOSIT.value.format(amount))
        except (InvalidAmountError, InvalidTypeError) as e:
            print(e)

    def withdraw(self, amount: Amount):
        """Списывает сумму (>0 & <=balance) с текущего счёт"""
        try:
            Validator.valid_amount(amount)
            Validator.valid_withdraw(amount, self._current_account.balance)
            self._current_account.balance -= amount
            print(Message.WITHDRAW.value.format(amount))
        except (InvalidAmountError, InvalidTypeError, WithdrawError) as e:
            print(e)

    def out_transfer(self, account: int, other_account: int, amount: Amount):
        """Имитирует перевод на внешний счёт (вне системы).

        Средства списываются с указанного счёта пользователя, но получатель
        не пополняется (предполагается, что он в другой системе)"""
        try:
            Validator.valid_account(account)
            Validator.valid_exist_account(account, self._accounts)
            # Внешний счёт проверяется только на формат (5 цифр), но не на существование
            Validator.valid_account(other_account)
            Validator.valid_amount(amount)
            Validator.valid_withdraw(amount, self._accounts[account].balance)

            self._accounts[account].balance -= amount
            # Примечание: средства "уходят" из системы — получатель не пополняется

            print(Message.TRANSFER_OUT.value)
            print(Message.TRANSFER_INFO.value.format(account, amount, other_account))
        except (InvalidAccountError, InvalidTypeError, WithdrawError) as e:
            print(e)

    def into_transfer(self, first_account: int, second_account: int, amount: Amount):
        """Выполняет перевод между двумя счетами пользователя"""
        try:
            Validator.valid_account(first_account)
            Validator.valid_account(second_account)
            Validator.valid_exist_account(first_account, self._accounts)
            Validator.valid_exist_account(second_account, self._accounts)
            Validator.valid_amount(amount)
            Validator.valid_withdraw(amount, self._accounts[first_account].balance)

            self._accounts[first_account].balance -= amount
            self._accounts[second_account].balance += amount

            print(Message.TRANSFER_INTO.value)
            print(
                Message.TRANSFER_INFO.value.format(
                    first_account, amount, second_account
                )
            )
        except (
            InvalidAccountError,
            InvalidAmountError,
            InvalidTypeError,
            WithdrawError,
        ) as e:
            print(e)

    def display_current_account(self):
        """Выводит номер текущего счёта"""
        print(Message.ACCOUNT_CURRENT.value.format(self._current_account.account_id))

    def display_accounts(self):
        """Выводит список всех счетов пользователя с балансами"""
        print(Message.ACCOUNT_INFO_TITLE.value)
        for account_id in self._accounts:
            balance = self._accounts[account_id].balance.balance
            print(Message.ACCOUNT_INFO.value.format(account_id, balance))

    def select_account(self, account: int):
        """Устанавливает указанный счёт, если он существует, как текущий"""
        try:
            Validator.valid_account(account)
            Validator.valid_exist_account(account, self._accounts)
            self._current_account = self._accounts[account]
            print(Message.ACCOUNT_SELECT.value.format(account))
        except (InvalidAccountError, InvalidTypeError) as e:
            print(e)

    def create_account_id(self) -> int:
        """Создаёт новый уникальный счёт и возвращает его номер.
        Гарантирует уникальность через повторную генерацию при коллизии"""
        account_id = random.randint(MIN_ACCOUNT_ID, MAX_ACCOUNT_ID)
        while account_id in self._accounts:
            account_id = random.randint(MIN_ACCOUNT_ID, MAX_ACCOUNT_ID)
        self._accounts[account_id] = Account(account_id)
        print(Message.ACCOUNT_CREATE.value.format(account_id))
        return account_id

    def __initial_account(self):
        """Создаёт первый счёт при инициализации профиля."""
        account_id = self.create_account_id()
        self._current_account = self._accounts[account_id]


if __name__ == "__main__":

    def select_point(prompt: str) -> int:
        while True:
            n = input(prompt)
            if n.isnumeric():
                if int(n) >= 0:
                    return int(n)
            else:
                print(f"[ERROR] Недопустимое значение: {n}")

    def input_amount(prompt: str) -> float:
        n: float = 0
        try:
            n = float(input(prompt))
            return n
        except ValueError:
            print(f"[ERROR] Недопустимое значение: {n}")

    def menu():
        print(
            f"========== Меню ==========\n"
            f"1. Пополнение счета\n"
            f"2. Списание с текущего счёта\n"
            f"3. Перевод между своими счетами\n"
            f"4. Перевод \n"
            f"5. Проверка баланса\n"
            f"6. Показать счета\n"
            f"7. Создать счет\n"
            f"8. Выбрать счет\n"
            f"9. Текущий счет\n"
            f"0. Выход\n"
        )

    def main():
        user = UserBank()
        menu()
        while True:
            n = select_point("[>] Введите номер операции: ")
            if n == 1:
                user.deposit(input_amount("[>] Введите сумму: "))
            elif n == 2:
                user.withdraw(input_amount("[>] Введите сумму: "))
            elif n == 3:
                user.into_transfer(
                    select_point("[>] Введите номер первого счёта: "),
                    select_point("[>] Введите номер второго счёта: "),
                    input_amount("[>] Введите сумму перевода: "),
                )
            elif n == 4:
                user.out_transfer(
                    select_point("[>] Введите номер счета списания: "),
                    select_point("[>] Введите номер счета получателя: "),
                    input_amount("[>] Введите сумму перевода: "),
                )
            elif n == 5:
                user.check_balance()
            elif n == 6:
                user.display_accounts()
            elif n == 7:
                user.create_account_id()
            elif n == 8:
                user.display_accounts()
                user.select_account(select_point("[>] Введите номер счета: "))
            elif n == 9:
                user.display_current_account()
            elif n == 0:
                exit(0)
            else:
                print(f"[W] Данный пункт меню не существует: {n}")

    main()
