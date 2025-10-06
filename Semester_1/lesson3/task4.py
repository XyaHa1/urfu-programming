import random
from typing import Dict, Optional


class Balance:
    def __init__(self, balance: float = 0):
        self._balance: float = balance


    def __str__(self):
        return f"[I] Баланс счета: {self._balance} рублей"


    def __iadd__(self, amount):
        if isinstance(amount, (float, int)):
            if amount > 0:
                print(f"[I] Пополнение счета на {amount} рублей. ")
                self._balance += amount
        return self


    def __isub__(self, amount):
        if isinstance(amount, (float, int)):
            if self._balance < amount:
                print(f"[W] Недостаточно средств на счете")
            else:
                print(f"[I] Списание со счета на {abs(amount)} рублей. ")
                self._balance -= amount
        return self


    def __lt__(self, other):
        if isinstance(other, Balance):
            return self._balance < other._balance
        return self._balance < other


    @property
    def balance(self):
        return self._balance


class Account:
    def __init__(self, account_id: int):
        self.account_id: int = account_id
        self.balance: Balance = Balance()


class UserBank:
    def __init__(self, name="user"):
        self._name = name
        self._accounts: Dict[int, Account] = {}
        self._current_account: Optional[Account] = None
        self.__initial_account()


    def check_balance(self): # Проверка баланса
        print(self._current_account.balance)


    def deposit(self, amount: float): # Пополнение счета
        if amount < 0:
            print(f"[ERROR] Недопустимое значение: отрицательное число")
        else:
            self._current_account.balance += amount


    def withdraw(self, amount: float): # Списание со счета
        if amount < 0:
            print(f"[ERROR] Недопустимое значение: отрицательное число")
        else:
            self._current_account.balance -= amount

    # Проверка существования счета
    def __check_transfer(self, account: int) -> bool:
        if account in self._accounts:
            return True
        print(f"[W] Данного счета не существует: #{account}")
        return False

    # Перевод на чужой счет
    def out_transfer(self, account: int, other_account: int, amount: float):
        if self.__check_transfer(account):
            if self._accounts[account].balance < amount :
                print(f"[W] Недостаточно средств на счете")
                return
            self._accounts[account] -= amount
            print(f"======= Перевод =======\n"
                  f"Счёт списания: #{account}\n"
                  f"Сумма: {amount}\n"
                  f"Счёт получателя: #{other_account}\n"
                  f"======================")

    # Перевод между своими счетами
    def into_transfer(self, first_account: int, second_account: int, amount: float):
        if self.__check_transfer(first_account) and self.__check_transfer(second_account):
            if self._accounts[first_account].balance < amount:
                print(f"[W] Недостаточно средств на счете")
                return
            self._accounts[first_account] -= amount
            self._accounts[second_account] += amount
            print(f"======= Перевод между счетами =======\n"
                  f"Счёт отправителя: #{first_account}\n"
                  f"Сумма: {amount}\n"
                  f"Счёт получателя: #{second_account}\n"
                  f"=====================================")


    def show_accounts(self): # Вывод всех своих счетов
        print(f"======= Счета пользователя =======")
        for account in self._accounts:
            print(f"> Номер счёта: #{account}\n"
                  f"{self._accounts[account].balance}\n")
        print(f"===================================")


    def select_account(self, account: int):
        if self.__check_transfer(account):
            self._current_account = self._accounts[account]


    def __initial_account(self):
        account_id = self.create_account_id()
        self._current_account = self._accounts[account_id]


    def create_account_id(self) -> int: # Создание уникального счета
        account_id = random.randint(10000, 99999)
        while account_id in self._accounts: # Проверка на уникальность
            account_id = random.randint(10000, 99999)
        self._accounts[account_id] = Account(account_id)
        print(f"[I] Создан счёт: #{account_id}")
        return account_id


def input_int(prompt: str):
    while True:
        n = input(prompt)
        if n.isnumeric():
            if int(n) > 0:
                return int(n)
            else:
                print(f"[ERROR] Недопустимое значение: отрицательное число")
        else:
            print(f"[ERROR] Недопустимое значение: {n}")


def menu():
    print(f"========== Меню ==========\n"
          f"1. Пополнение счета\n"
          f"2. Перевод между своими счетами\n"
          f"3. Перевод \n"
          f"4. Проверка баланса\n"
          f"5. Показать счета\n"
          f"6. Создать счет\n"
          f"7. Выбрать счет\n"
          f"0. Выход\n")


def main():
    user = UserBank()
    menu()
    while True:
        n = input_int("[>] Введите номер операции: ")
        if n == 1:
            user.deposit(input_int("[>] Введите сумму: "))
        elif n == 2:
            user.into_transfer(input_int("[>] Введите номер первого счёта: "),
                               input_int("[>] Введите номер второго счёта: "),
                               input_int("[>] Введите сумму перевода: "))
        elif n == 3:
            user.out_transfer(input_int("[>] Введите номер счета списания: "),
                              input_int("[>] Введите номер счета получателя: "),
                              input_int("[>] Введите сумму перевода: "))
        elif n == 4:
            user.check_balance()
        elif n == 5:
            user.show_accounts()
        elif n == 6:
            user.create_account_id()
        elif n == 7:
            user.show_accounts()
            user.select_account(input_int("[>] Введите номер счета: "))
        elif n == 0:
            exit(0)




if __name__ == "__main__":
    main()
