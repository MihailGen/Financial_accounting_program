import sys
from models.user import User


money = 0
print("******************************************")
print("@@@@@  FINANCIAL ACCOUNTING PROGRAM  @@@@@")
print("******************************************")
print("")

while True:
    print("What would you like to do?")
    print("1. Registration")
    print("2. Login in program")
    print("3. Update_profile")
    print("4. Add income")
    print("5. Exit")
    print("6. Exit")
    print("7. Exit")
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
        name = str(input("Enter your name: "))
        surname = str(input("Enter your surname: "))
        login = name + surname
        email = str(input("Enter your email: "))
        password = str(input("Enter your password: "))
        user = User(login, password, email)
        user.register()
        print("")
        print(f"Congratulation!\nYou are registered as {login}")
        print("")
        print(f"Your password is: {password}")
        print("")

    # Login
    elif choice == 2:
        login = str(input("Enter your login: "))
        password = str(input("Enter your password: "))
        user = User(login, password, "")
        user.login()

    # Money withdraw
    elif choice == 3:
        if password != str(input("Enter your password: ")) or password == "":
            print("Wrong password!")
        else:
            print("Your current balance is: " + str(money))
            withdraw_bill = int(input("How much money do you want to withdraw from your account: "))
            money -= withdraw_bill
            print("Withdrawal completed successfully")
            print("Your current balance is: " + str(money))
            print("")

    # Display balance
    elif choice == 4:
        if password != str(input("Enter your password: ")) or password == "":
            print("Wrong password!")
        else:
            print("Your current balance is: " + str(money))
            print("")

    # Exit
    elif choice == 5:
        print("Thanks, goodbye!")
        break

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
