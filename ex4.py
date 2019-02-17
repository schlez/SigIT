# The function gets a string and compress it recursively
def compress(st1, i=0):
    # Increase counter in case that the string isn't over and the current character is equal to the next one
    while i < len(st1) - 1 and st1[i] == st1[i + 1]: i += 1
    # Return the replacement of the string with the compresses substring and call the function on the rest of the string
    return st1.replace((i + 1) * st1[i], st1[i] + str(i + 1))[:len(str(i + 1)) + 1] + (compress(st1[i + 1:]) if i < len(st1) - 1 else "")


def main():
    str = input("please enter a string: ")
    print(compress(str))


if __name__ == "__main__":
    main()
