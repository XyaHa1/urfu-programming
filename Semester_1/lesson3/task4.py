import random
from enum import Enum
from typing import Dict, Optional, Union


class InvalidAccountError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InvalidTypeError(Exception):
    pass


class WithdrawError(Exception):
    pass


MIN_ACCOUNT_ID = 10000
MAX_ACCOUNT_ID = 99999

Amount = Union[float, int]


class Message(Enum):
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
    ACCOUNT_NOT_EXISTS = "[WARNING] Счет не существует: #{}"
    ACCOUNT_SELECT = "[I] Выбран счет: #{}"
    ACCOUNT_CURRENT = "[I] Текущий счет: #{}"
    WITHDRAW = "[I] Списание со счета на {} рублей. "
    DEPOSIT = "[I] Пополнение счета на {} рублей. "
    VIEW_BALANCE = "[I] Баланс счета: {} рублей"


class Balance:
    def __init__(self, balance: Amount = 0):
        self._balance: Amount = balance

    def __str__(self) -> str:
        return Message.VIEW_BALANCE.value.format(self._balance)

    def __iadd__(self, amount: Amount) -> "Balance":
        self._balance += amount
        return self

    def __isub__(self, amount: Amount) -> "Balance":
        self._balance -= amount
        return self

    def __lt__(self, other) -> bool:
        if isinstance(other, Balance):
            return self._balance < other._balance

        return self._balance < other

    @property
    def balance(self) -> Amount:
        return self._balance


class Account:
    def __init__(self, account_id: int):
        self.account_id: int = account_id
        self.balance: Balance = Balance()


class Validator:
    # Проверка на валидность счета
    @staticmethod
    def valid_account(account: int):
        if not isinstance(account, int):
            raise InvalidTypeError(Message.INVALID_TYPE.value)

        if not (MIN_ACCOUNT_ID <= account <= MAX_ACCOUNT_ID):
            raise InvalidAccountError(Message.INVALID_ACCOUNT.value.format(account))

    # Проверка на валидность суммы
    @staticmethod
    def valid_amount(amount: Amount):
        if not isinstance(amount, (float, int)):
            raise InvalidTypeError(Message.INVALID_TYPE.value)

        if amount <= 0:
            raise InvalidAmountError(Message.INVALID_AMOUNT.value)

    # Проверка на валидность суммы для списания со счета
    @staticmethod
    def valid_withdraw(amount: Amount, balance: "Balance"):
        if balance < amount:
            raise WithdrawError(Message.WITHDRAW_ERROR.value)

    # Проверка на существование счета
    @staticmethod
    def valid_exist_account(account: int, accounts: Dict[int, Account]):
        if account not in accounts:
            raise InvalidAccountError(Message.ACCOUNT_NOT_EXISTS.value.format(account))


class UserBank:
    def __init__(self, name="user"):
        self._name = name
        self._accounts: Dict[int, Account] = {}
        self._current_account: Optional[Account] = None
        self.__initial_account()

    # Проверка баланса
    def check_balance(self):
        print(self._current_account.balance)

    # Пополнение счета
    def deposit(self, amount: Amount):
        try:
            # Проверка на валидность суммы
            Validator.valid_amount(amount)

            self._current_account.balance += amount
            print(Message.DEPOSIT.value.format(amount))
        except (InvalidAmountError, InvalidTypeError) as e:
            print(e)

    # Списание со счета
    def withdraw(self, amount: Amount):
        try:
            # Проверка на валидность суммы
            Validator.valid_amount(amount)
            # Проверка на валидность суммы для списания со счета
            Validator.valid_withdraw(amount, self._current_account.balance)

            self._current_account.balance -= amount
            print(Message.WITHDRAW.value.format(amount))
        except (InvalidAmountError, InvalidTypeError, WithdrawError) as e:
            print(e)

    # Имитация перевода на внешний счет
    def out_transfer(self, account: int, other_account: int, amount: Amount):
        try:
            # Проверка на валидность счета
            Validator.valid_account(account)
            # Проверка на существование счета в личном кабинете
            Validator.valid_exist_account(account, self._accounts)
            # TODO: Проверка на существование внешнего счета
            # Проверка на валидность суммы
            Validator.valid_amount(amount)
            # Проверка на валидность суммы для списания со счета
            Validator.valid_withdraw(amount, self._accounts[account].balance)

            self._accounts[account].balance -= amount
            # TODO: Передача средств на внешний счет

            print(Message.TRANSFER_OUT.value)
            print(Message.TRANSFER_INFO.value.format(account, amount, other_account))
        except (InvalidAccountError, InvalidTypeError, WithdrawError) as e:
            print(e)

    # Перевод между своими счетами
    def into_transfer(self, first_account: int, second_account: int, amount: Amount):
        try:
            # Проверка на валидность счетов
            Validator.valid_account(first_account)
            Validator.valid_account(second_account)
            # Проверка на существование счетов в личном кабинете
            Validator.valid_exist_account(first_account, self._accounts)
            Validator.valid_exist_account(second_account, self._accounts)
            # Проверка на валидность суммы
            Validator.valid_amount(amount)
            # Проверка на валидность суммы для списания со счета
            Validator.valid_withdraw(amount, self._accounts[first_account].balance)

            self._accounts[first_account].balance -= amount
            self._accounts[second_account].balance += amount

            print(Message.TRANSFER_INTO.value)
            print(Message.TRANSFER_INFO.value.format(first_account, amount, second_account))
        except (InvalidAccountError, InvalidAmountError, InvalidTypeError, WithdrawError) as e:
            print(e)

    # Вывод текущего счета
    def display_current_account(self):
        print(Message.ACCOUNT_CURRENT.value.format(self._current_account.account_id))

    # Визуализация всех счетов
    def display_accounts(self):
        print(Message.ACCOUNT_INFO_TITLE.value)
        for account in self._accounts:
            print(
                Message.ACCOUNT_INFO.value.format(
                    account, self._accounts[account].balance.balance
                )
            )

    # Выбор счета
    def select_account(self, account: int):
        try:
            # Проверка на валидность счета
            Validator.valid_account(account)
            # Проверка на существование счета в личном кабинете
            Validator.valid_exist_account(account, self._accounts)

            self._current_account = self._accounts[account]
            print(Message.ACCOUNT_SELECT.value.format(account))
        except (InvalidAccountError, InvalidTypeError) as e:
            print(e)

    # Создание уникального счета
    def create_account_id(self) -> int:
        account_id = random.randint(MIN_ACCOUNT_ID, MAX_ACCOUNT_ID)

        # Гарантируем уникальность счета
        while account_id in self._accounts:
            account_id = random.randint(MIN_ACCOUNT_ID, MAX_ACCOUNT_ID)
        self._accounts[account_id] = Account(account_id)
        print(Message.ACCOUNT_CREATE.value.format(account_id))

        return account_id

    # Инициализация первичного счета
    def __initial_account(self):
        account_id = self.create_account_id()
        self._current_account = self._accounts[account_id]


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
        f"2. Перевод между своими счетами\n"
        f"3. Перевод \n"
        f"4. Проверка баланса\n"
        f"5. Показать счета\n"
        f"6. Создать счет\n"
        f"7. Выбрать счет\n"
        f"8. Текущий счет\n"
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
            user.into_transfer(
                select_point("[>] Введите номер первого счёта: "),
                select_point("[>] Введите номер второго счёта: "),
                input_amount("[>] Введите сумму перевода: "),
            )
        elif n == 3:
            user.out_transfer(
                select_point("[>] Введите номер счета списания: "),
                select_point("[>] Введите номер счета получателя: "),
                input_amount("[>] Введите сумму перевода: "),
            )
        elif n == 4:
            user.check_balance()
        elif n == 5:
            user.display_accounts()
        elif n == 6:
            user.create_account_id()
        elif n == 7:
            user.display_accounts()
            user.select_account(select_point("[>] Введите номер счета: "))
        elif n == 8:
            user.display_current_account()
        elif n == 0:
            exit(0)
        else:
            print(f"[W] Данный пункт меню не существует: {n}")


if __name__ == "__main__":
    main()
