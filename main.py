import datetime
import asyncio
from models.user import User
from models.account import Account
from models.transaction import Transaction
from services.transaction_management import create_id_for_transaction, generate_report_user_story_6
from services.transaction_management import generate_report_user_story_7
from services.account_management import create_account_object_from_json
from services.account_management import create_account, isValid, account_proof
from services.authentication import login_fnc, logout_fnc, user_mail_from_Json
from services.authentication import update_user_information
from utils.currency_converter import converter
from config.settings import Constants_and_variables

print("\n")
# print("*****************************************")
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
    print("4. Display accounts balance")
    print("5. Delete account")
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
        user.update_profile(password, email)
        #update_user_information(username, password, email)


    # Create account
    elif choice == 2:
        name = input("Enter accounts name: ")
        currency = input("Enter the number of currency for your account\n 1 - Rub \n 2 - $ \n 3 - €\nYour choice: ")
        balance = float(input("Enter the start balance in your account: "))
        create_account(username, name, currency, balance)

    # Create transaction
    elif choice == 3:
        # Генерируем ID для транзакции
        transaction_id = create_id_for_transaction(username)

        # Запрашиваем у пользователя данные о транзакции
        account_id = account_proof(username, "Enter your account ID: ")
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

        # Создаём объект
        transaction = Transaction(transaction_id, username, account_id, amount, transaction_type, description,
                                  datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

        transaction.record_transaction()
        break

    # Display balance for account
    elif choice == 4:
        account_id = account_proof(username, "Please, enter your account ID: ")
        account = create_account_object_from_json(username, account_id)
        result = account.get_balance()
        print(f'Balance {account.name}: {account.get_balance()}')
        break

    # Exit
    elif choice == 5:
        account_id = account_proof(username, "Please enter the ID\nwhich you want to delete: ")

        user_response = input("Are You sure?: Υ or N: ")
        if user_response in ("Y", "y"):
            account = create_account_object_from_json(username, account_id)
            account.delete_account()
            print(f"Account: {account.name} successfully deleted!")
        elif user_response in ("N", "n"):
            break

        break

    elif choice == 6:
        account_id = account_proof(username, "Please, enter your account ID for report\n\"User history 6\" :")
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
        account_id = account_proof(username, "Please, enter your account ID for report\n\"User history 7\" :" )
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
        account_id = account_proof(username, "Enter the account ID from which you want to transfer: ")
        account_receiver = account_proof(username, "Enter the account ID to which you want to transfer: ")
        if account_id == account_receiver:
            print("Accounts ID for transfer must be different!")
            break
        while True:
            try:
                amount = round(float(input("Enter the amount: ")),2)
                break
            except ValueError:
                print("Not correct number, please try again")
        account = create_account_object_from_json(username, str(account_id))
        account.transfer(str(account_receiver), amount)

    elif choice == 9:
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
