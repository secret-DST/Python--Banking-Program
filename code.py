def show_balance(balance):
    print("**********************")
    print(f"Your balance is £{balance:.2f}")
    print("**********************")



def deposit():
    amount = float(input("How much would you like to deposit? "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("How much would you like to withdraw? "))
    if amount > balance:
        print("insufficient funds ")
        return 0
    elif amount < 0:
        print("You havent withdrawed anything! ")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("Banking app")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")
        print("**********************")

        choice = input("enter from option 1 - 4: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else: 
            print("Try again. Enter from options 1 - 4: ")
    print("**********************")
    print("Thank you have a nice day!")
    print("**********************")

if __name__ == '__main__':
    main()
