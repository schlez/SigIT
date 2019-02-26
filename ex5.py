# The function gets an ID as a string and checks if it's valid
def checkID(st):
    sum = 0
    if len(st) != 9:  # checks if the given ID has 9 digit
        return False
    for tav in range(8):
        x = int(st[tav])  # for shortcut
        sum += x if tav % 2 == 0 else (2 * x if x < 5 else 1 + (2 * x) % 10)  # sum the ID digits by the given formula
    if (sum + int(st[8])) % 10 == 0:  # check if the last digit is complementary to 10
        return True
    return False


def main():
    str = input("pleas enter your ID: ")  # call to check ID function
    print("Valid") if checkID(str) else print("Not Valid")


if __name__ == "__main__":
    main()
