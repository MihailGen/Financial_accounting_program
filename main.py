import sys
from models.user import User
from models.account import Account
from services.account_management import save_account_to_json
from services.account_management import create_id_for_account
from services.authentication import login


print("******************************************")
print("@@@@@  FINANCIAL ACCOUNTING PROGRAM  @@@@@")
print("******************************************")
print("")


username = ''

while username == '':
    log = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if login(log, password):
        username = login(log, password)
    else:
        print("\nLogin or password is wrong!\nWant to try again?\n")
        response = input("If Yes, print Y,\nif You want to register, print R,\nif Exit, print E: ")
        if (response == "R" or response == "r"):
            print("Please register\n")
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            login = name + surname
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = User(login, password, email)
            user.register()
            print("")
            username = login
        if  (response == "E" or response == "e"):
            print("Thanks, goodbye!")
            exit()

while True:
    print("What would you like to do?")
    print("1. Registration")
    print("2. Login program")
    print("3. Update_profile")
    print("4. Create account")
    print("5. Exit")
    print("6. Display balance for account")
    print("7. Display total balance")
    print("8. Exit")
    print("9. Exit")
    print("10. Exit")
    print("11. Exit")
    print("12. Exit")
    print("13. Exit")
    print("14. Exit")

    choice = int(input("Enter your choice: "))

    # Registration
    if choice == 1:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        login = name + surname
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = User(login, password, email)
        user.register()
        print("")
        print(f"Congratulation!\nYou are registered as {login}")
        print("")
        print(f"Your password is: {password}")
        print("")

    # Login
    elif choice == 2:
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        user = User(login, password, "")
        user.login()

    # Update_profile
    elif choice == 3:
        print("Thanks, goodbye!")
        break

    # Create account
    elif choice == 4:
        login = input("Enter your login: ")
        name = input("Enter accounts name: ")
        currency = input("Enter the number of currency for your account\n 1 - Rub \n 2 - $ \n 3 - €\nYour choice: ")
        balance = float(input("Enter the balance in your account: "))
        acc = Account(create_id_for_account(login), name, currency, balance)
        save_account_to_json(login, acc)

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
        print("Thanks, goodbye!")
        break

    elif choice == 7:
        print("Thanks, goodbye!")
        break

    elif choice == 8:
        print("Thanks, goodbye!")
        break

    elif choice == 9:
        print("Thanks, goodbye!")
        break

    elif choice == 10:
        print("Thanks, goodbye!")
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

    elif choice == 17:
        print("Thanks, goodbye!")
        break

    # Other operation numbers
    else:
        print("Wrong operation number, please try again!")
        print("")


def main():
    pass


if __name__ == "__main__":
    main()