# The function get a list of variables and a function and operating the function on all the variables in the list
def functionenabling(lst, func):
    for i in range(len(lst)):
        lst[i] = func(lst[i])  # enable the given function on every variable and replace it with the result


def add(var):
    return var + 2


def main():
    lst = [2, 3, 4, 5]  # list of variables
    func = add  # The function that will be operated on the list
    functionenabling(lst, func)
    print(lst)


if __name__ == "__main__":
    main()
