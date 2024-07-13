import datetime
import asyncio
from models.user import User
from models.account import Account
from models.transaction import Transaction
from services.transaction_management import create_id_for_transaction
from services.transaction_management import generate_report_user_story_6
from services.transaction_management import generate_report_user_story_7
from services.account_management import account_from_file, create_account_object_from_json
from services.account_management import create_account
from services.account_management import isValid
from services.account_management import account_proof
from services.authentication import login_fnc
from services.authentication import logout_fnc
from services.authentication import update_user_information
from utils.currency_converter import converter
from config.settings import Constants_and_variables
from services.account_management import check_if_account_exists

print("\n")
# print("*****************************************")
print("₽₽₽-----***------$$$$$------***---------₽₽₽")
print("€€€€€   FINANCIAL ACCOUNTING PROGRAM   €€€€")
print("₽₽₽-----***------$$$$$------***---------₽₽₽")
print("\n")

username = ''

while not username:
    log = input("Username: ")
    password = input("Password: ")
    if login_fnc(log, password):
        username = log
    else:
        print("\nLogin or password is wrong!\nWant to try again?\n")
        response = input("If yes, print Y,\nif You want to register, print R,\nif Exit, print any another key: ")
        if response == "R" or response == "r":
            print("Please register\n")
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            login = name + surname
            while True:
                email = input("Enter your email: ")
                if not isValid(email):
                    print("\nEmail is invalid!\n")
                else:
                    break
            password = input("Enter your password: ")
            user = User(login, password, email)
            user.register()
            print("")
            username = login
        elif response not in ("Y", "y", "Yes", "yes"):
            print("Thanks, goodbye!")
            exit()

while True:
    print("What would you like to do?")
    print("1. Update_profile")
    print("2. Create account")
    print("3. Create transaction")
    print("4. Display balance for account")
    print("5. Display total balance")
    print("6. Report user story 6")
    print("7. Report user story 7")
    print("8. Transfer")
    print("9. Currency converter")
    print("10. Logout")
    print("11. Exit")
    choice = int(input("\nEnter your choice: "))

    # Update_profile
    if choice == 1:
        password = input("Enter new password: ")
        while True:
            email = input("Enter new email: ")
            if not isValid(email):
                print("\nInvalid email forma!\n")
            else:
                break
        update_user_information(username, password, email)


    # Create account
    elif choice == 2:
        # login = input("Enter your login: ")
        name = input("Enter accounts name: ")
        currency = input("Enter the number of currency for your account\n 1 - Rub \n 2 - $ \n 3 - €\nYour choice: ")
        balance = float(input("Enter the balance in your account: "))
        create_account(username, name, currency, balance)

    # Create transaction
    elif choice == 3:
        # Генерируем ID для транзакции
        transaction_id = create_id_for_transaction(username)

        # Запрашиваем у пользователя данные о транзакции
        account_id = input("Enter the account ID: ")
        amount = float(input("Enter the amount: "))
        transaction_type = input("Enter the type of transaction\n1 - Adding income \n2 - Expense registration: ")
        if transaction_type == "1":
            transaction_type = "Income"
        elif transaction_type == "2":
            transaction_type = "Payment"
        else:
            print("Not correct number, please try again")
            break

        description = input("Write a description of transaction: ")
        # current_date = datetime.datetime.now()

        # Создаём объект
        transaction = Transaction(transaction_id, username, account_id, amount, transaction_type, description,
                                  datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

        # Вытаскиваем из файла данные о счёте хитрым способом
        data = account_from_file(username, account_id)

        currency = data['currency']
        name = data['name']
        balance = data['balance']

        # cоздаём объект account, на основе того, что вытащили, проводим операцию с балансом
        account = Account(account_id, username, name, currency, balance)
        if transaction_type == "Income":
            account.add_income(amount)
        if transaction_type == "Payment":
            account.add_expense(amount)

        # записываем операцию в JSON
        transaction.record_transaction()
        break

    # Display balance for account
    elif choice == 4:
        print("Thanks, goodbye!")
        break

    # Exit
    elif choice == 5:
        """""
        if password != str(input("Enter your password: ")) or password == "":
            print("Wrong password!")
        else:
            print("Your current balance is: " + str(money))
            withdraw_bill = int(input("How much money do you want to withdraw from your account: "))
            money -= withdraw_bill
            print("Withdrawal completed successfully")
            print("Your current balance is: " + str(money))
            print("")
        """

    elif choice == 6:
        account_id = account_proof(username)
        while True:
            try:
                dt_start = input(f'Enter the filtering start date in format "dd.mm.yyyy": ')
                except_generator = datetime.datetime.strptime(dt_start, "%d.%m.%Y")
                dt_end = input(f'Enter the filtering end date in format "dd.mm.yyyy": ')
                except_generator = datetime.datetime.strptime(dt_end, "%d.%m.%Y")
                break
            except:
                print(
                    f"Incorrect date format!\nPlease enter the date in the following format: {datetime.datetime.now().strftime('%d.%m.%Y')}")
        while True:
            try:
                trans_type = int(input("Enter the type of transaction: \n"
                                       "1 - Income, 2 - Payment: "))
                trans_type = Constants_and_variables.trans_type[trans_type - 1]
                break
            except ValueError:
                print("Not correct number, please try again")
        generate_report_user_story_6(username, account_id, dt_start, dt_end, trans_type)
        break


    elif choice == 7:
        account_id = account_proof(username)
        while True:
            try:
                dt_start = input(f'Enter the filtering start date in format "dd.mm.yyyy": ')
                except_generator = datetime.datetime.strptime(dt_start, "%d.%m.%Y")
                dt_end = input(f'Enter the filtering end date in format "dd.mm.yyyy": ')
                except_generator = datetime.datetime.strptime(dt_end, "%d.%m.%Y")
                break
            except:
                print(
                    f"Incorrect date format!\nEnter the date in the following format! Example: {datetime.datetime.now().strftime('%d.%m.%Y')}")

        generate_report_user_story_7(username, account_id, dt_start, dt_end)

        break

    elif choice == 8:
        account_id = account_proof(username)
        print(account_id)
        account = create_account_object_from_json(username, str(account_id))
        print(account.account_id)
        account.transfer('1', 20.21)
        # account = Account(account_id, username, name, currency, balance)

    elif choice == 9:
        # asyncio.run(get_content(Paths.service_path))
        # asyncio.run(list_currency_rates_to_file(Paths.service_path))
        asyncio.run(converter("kzt", "rub", 1000))
        break

    elif choice == 10:
        logout_fnc(username)
        break

    elif choice == 11:
        print("Thanks, goodbye!")
        break

    elif choice == 12:
        print("Thanks, goodbye!")
        break

    elif choice == 13:
        print("Thanks, goodbye!")
        break

    elif choice == 14:
        print("Thanks, goodbye!")
        break

    elif choice == 15:
        print("Thanks, goodbye!")
        break

    elif choice == 16:
        print("Thanks, goodbye!")
        break

    # Other operation numbers
    else:
        print("Wrong operation number, please try again!")
        print("")
