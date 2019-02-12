secret_code = "1234"
balance = 1000
exit_flag = False  # Flag for exit the system


def menu():
    global secret_code
    func_dict = {  # options dictionary for menu
        "a": print_balance,
        "b": Withdraw_money,
        "c": change_code,
        "d": EXIT
    }
    while True:
        if exit_flag:  # In case the user decide to exit the ATM system
            break
        print("Welcome to the ATM")
        code = input("please enter your secrete code: ")
        if code != secret_code:  # If the entered code is incorrect
            print("ERROR")
            continue
        print("Please choose an option:(a/b/c/d)")
        print("a. Print balance")
        print("b. Withdraw money")
        print("c. Changing secret code")
        print("d. Exit")
        option = input()
        while option not in func_dict:
            # In case the selected option is not in the dictionary
            print("Please choose a function again")
            option = input()
        func_dict[option]()  # call the function that we choose


# The function prints the account balance
def print_balance():
    global balance
    print("Your balance: " + str(balance))


# The function withdraw money
def Withdraw_money():
    global balance

    amount_dict = {  # options dictionary for money menu
        "a": 20,
        "b": 50,
        "c": 0
    }
    print("Please choose the option you want (a/b/c)")
    print("a. 20")
    print("b. 50")
    print("c. Other")

    wdraw = input()
    # check if the selected option is avilable in the dictionary
    while wdraw not in amount_dict:
        print("Please choose the option you want")
        wdraw = input()
    wdraw = amount_dict[wdraw]
    if wdraw == 0:  # case of Other
        print("choose amount of money")
        wdraw = input()
    wdraw = int(wdraw)
    # check if we have enough money
    if balance >= wdraw:
        balance -= wdraw
    else:  # we got here if the balance is not enough
        print("There is not enough money in your account")
        print_balance()


# The function changing the secrete code
def change_code():
    global secret_code
    secret_code = input("Please enter a new secrete code:")


# the function end the ATM
def EXIT():
    global exit_flag
    exit_flag = True
    print("Thank you for using the ATM \n GOODBYE")


# Main function
def main():
    menu()


if __name__ == "__main__":
    main()
