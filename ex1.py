secret_code = "1234"


def menu():
    global secret_code
    func_dict={ #options dictionry
        "a": print_balance,
        "b": Withdraw_money,
        "c": change_code,
        "d": EXIT
    }
    while True:
        print("Welcome to the ATM")
        code = input("please enter your secrete code: ")
        if code != secret_code:
            print("ERROR")
            continue
        print("Please choose an option:")
        print("a. Print balance")
        print("b. Withdraw money")
        print("c. Changing secret code")
        print("d. Exit")
        option =input()
        while option not in func_dict:
            print("Please choose a function again")
            option = input()
        func_dict[option]()#call the function that we choose

def print_balance():


def Withdraw_money():


def change_code():


def EXIT():


def main():
    print(7)


if __name__ == "__main__":
    main()
