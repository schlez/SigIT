# The function operating another function and saving it results
def wrap(func):
    memory = {}  # Dictionary for saving the last calculation

    def wrapper(*var):
        if var in memory:  # checks if the variable is in the dictionary
            return memory[var]  # return the result of the operation that made to this variable
        else:
            n = func(*var)
            memory[var] = n  # save the result into the dictionary
            return n

    return wrapper


@wrap
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    print(fib(450))
    print(fib(450))


if __name__ == "__main__":
    main()
