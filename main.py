import datetime
import asyncio
from models.user import User
from models.account import Account
from models.transaction import Transaction
from services.transaction_management import create_id_for_transaction, generate_report_user_story_6
from services.transaction_management import generate_report_user_story_7
from services.account_management import create_account_object_from_json, update_account, is_correct_amount
from services.account_management import create_account, is_correct_email, account_proof
from services.authentication import login_fnc, logout_fnc, user_mail_from_Json
from services.authentication import update_user_information
from utils.currency_converter import converter
from config.settings import Constants_and_variables

print("\n")
print("₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽")
print("€€€            ~~~~~~~~~~               €€€")
print("$$$    FINANCIAL ACCOUNTING PROGRAM©    $$$")
print("€€€             ~  v.1  ~               €€€")
print("₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽₽")
print("\n")

username = ''

while not username:
    log = input("Username: ")
    password = input("Password: ")
    if login_fnc(log, password):
        username = log
        user = User(log, password, user_mail_from_Json(username))
    else:
        print("\nLogin or password is wrong!\nWant to try again?\n")
        response = input("If yes, print Y,\nif You want to register, print R,\nif Exit, print any another key: ")

        # Registration new user
        if response == "R" or response == "r":
            print("Please register\n")
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            login = name + surname
            while True:
                email = input("Enter your email: ")
                if not is_correct_email(email):
                    print("\nEmail is invalid!\n")
                else:
                    break
            password = input("Enter your password: ")
            user = User(login, password, email)
            user.register()

            # Create start account
            name = input("Enter accounts name: ")
            while True:
                try:
                    currency = int(input(
                        "Enter the number of currency for your account\n 1 - rub \n 2 - $ \n 3 - €\n 4 - kzt\n 5 - cny\n 6 - byn\n Your choice: "))
                    if currency not in (1, 2, 3, 4, 5, 6):
                        print("Invalid choice. Please try again.")
                    else:
                        break
                except ValueError as err:
                    print(err)

            while True:
                balance = input("Enter the amount: ")
                if is_correct_amount(balance):
                    break
            create_account(login, name, currency, balance)

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
    print("4. Display accounts balance")
    print("5. Delete account")
    print("6. Report user story 6")
    print("7. Report user story 7")
    print("8. Update account")
    print("9. Transfer")
    print("10. Currency converter")
    print("11. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            break
        except ValueError:
            print("Invalid choice. Please try again.")

    # Update_profile
    if choice == 1:
        password = input("Enter new password: ")
        while True:
            email = input("Enter new email: ")
            if not is_correct_email(email):
                print("\nInvalid email forma!\n")
            else:
                break
        user.update_profile(password, email)
        # update_user_information(username, password, email)


    # Create account
    elif choice == 2:
        name = input("Enter accounts name: ")
        while True:
            try:
                currency = int(input(
                    "Enter the number of currency for your account\n 1 - rub \n 2 - $ \n 3 - €\n 4 - kzt\n 5 - cny\n 6 - byn\n Your choice: "))
                if currency not in (1, 2, 3, 4, 5, 6):
                    print("Invalid choice. Please try again.")
                else:
                    break
            except ValueError as err:
                print(err)

        while True:
            balance = input("Enter the amount: ")
            if is_correct_amount(balance):
                break

        create_account(username, name, currency, float(balance))

    # Create transaction
    elif choice == 3:
        # Генерируем ID для транзакции
        transaction_id = create_id_for_transaction(username)

        # Запрашиваем у пользователя данные о транзакции
        while True:
            account_id = account_proof(username, "Enter your account ID: ")
            if not account_id:
                print("Try again!")
            else:
                break
        while True:
            amount = input("Enter the amount: ")
            if is_correct_amount(amount):
                break
        transaction_type = input("Enter the type of transaction\n1 - Adding income \n2 - Expense registration: ")
        while True:
            if transaction_type == "1":
                transaction_type = "Income"
                break
            elif transaction_type == "2":
                transaction_type = "Payment"
                break
            else:
                print("Not correct number, please try again")

        description = input("Write a description of transaction: ")
        print("\n")

        # print(transaction_id, username, account_id, amount, transaction_type, description,
        #       datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

        # Create object of klass Transaction
        transaction = Transaction(transaction_id, username, account_id, float(amount), transaction_type, description,
                                  datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        transaction.record_transaction()

    # Display balance for account
    elif choice == 4:
        account_id = account_proof(username, "Please, enter your account ID: ")
        if account_id:
            account = create_account_object_from_json(username, account_id)
            result = account.get_balance()
            print(f'Balance {account.name}: {account.get_balance()} {Constants_and_variables.currency[account.currency]}')


    # Delete account
    elif choice == 5:
        account_id = account_proof(username, "Please enter the ID\nwhich you want to delete: ")
        if account_id:
            user_response = input("Are You sure?: Υ or N: ")
            if user_response in ("Y", "y"):
                account = create_account_object_from_json(username, account_id)
                account.delete_account()
                print(f"Account: {account.name} successfully deleted!\n")
            elif user_response in ("N", "n"):
                print("Continue work!\n")


    # Report user story 6
    elif choice == 6:
        account_id = account_proof(username, "Please, enter your account ID for report\n\"User history 6\": ")
        if account_id:
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


    # Report user story 7
    elif choice == 7:
        account_id = account_proof(username, "Please, enter your account ID for report\n\"User history 7\": ")
        if account_id:
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



    # Update account
    elif choice == 8:
        account_id = account_proof(username, "Please enter the ID\nwhich you want to update: ")
        user_response = input("Are You sure?: Υ or N: ")
        if user_response in ("Y", "y"):
            name = input("Enter the new account name: ")
            while True:
                try:
                    currency = int(input(
                        "Enter the number of currency for your account\n 1 - rub \n 2 - $ \n 3 - €\n 4 - kzt\n 5 - cny\n 6 - byn\n Your choice: "))
                    if currency not in (1, 2, 3, 4, 5, 6):
                        print("Invalid choice. Please try again\n")
                    else:
                        break
                except ValueError as err:
                    print(err)
            while True:
                balance = input("Enter the amount: ")
                if is_correct_amount(balance):
                    break

            update_account(username, account_id, name, currency, float(balance))
            print(f"Account: {name} successfully updated!\n")
        elif user_response in ("N", "n"):
            print("Continue work!\n")



    # Transfer
    elif choice == 9:
        # account_id = account_proof(username, "Enter the account ID from which you want to transfer: ")
        while True:
            account_id = account_proof(username, "Enter the account ID from which you want to transfer: ")
            if not account_id:
                print("Try again!")
            else:
                break
        while True:
            account_receiver = account_proof(username, "Enter the account ID from which you want to transfer: ")
            if not account_id:
                print("Try again!")
            else:
                break

        # account_receiver = account_proof(username, "Enter the account ID to which you want to transfer: ")
        if account_id == account_receiver:
            print("Accounts ID for transfer must be different!")
            break
        while True:
            amount = input("Enter the amount: ")
            if is_correct_amount(amount):
                break
        account = create_account_object_from_json(username, str(account_id))
        account.transfer(str(account_receiver), float(amount))

    # Currency convertor
    elif choice == 10:
        print("\n*************************************\nStart currency exchange calculator\n")
        while True:
            try:
                currency_first = int(input(
                    "Enter the number of the currency which you want to exchange:\n 1 - rub \n 2 - $ \n 3 - €\n 4 - kzt\n 5 - cny\n 6 - byn\n Your choice: "))
                if currency_first not in (1, 2, 3, 4, 5, 6):
                    print("Invalid choice. Please try again.")
                else:
                    break
            except ValueError as err:
                print(err)

        while True:
            try:
                currency_two = int(input(
                    "Enter the number of the currency into you want to exchange money:\n 1 - rub \n 2 - $ \n 3 - €\n 4 - kzt\n 5 - cny\n 6 - byn\n Your choice: "))
                if currency_two not in (1, 2, 3, 4, 5, 6):
                    print("Invalid choice. Please try again.")
                else:
                    break
            except ValueError as err:
                print(err)

        while True:
            amount = input("Enter the amount: ")
            if is_correct_amount(amount):
                break
        res = asyncio.run(
            converter(Constants_and_variables.currency[currency_first], Constants_and_variables.currency[currency_two],
                      float(amount)))
        print(
            f"{amount} {Constants_and_variables.currency[currency_first]} = "
            f"{res} {Constants_and_variables.currency[currency_two]} "
            f"rate {datetime.datetime.now().strftime('%d.%m.%Y')}\n")

    # Logout
    elif choice == 11:
        logout_fnc(username)
        break

    # Other operation numbers
    else:
        print("Wrong operation number, please try again!")
        print("")
