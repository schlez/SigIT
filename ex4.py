# The function gets a string and compress it recursively
def compress(st1, i=0):
    # Increase counter in case that the string isn't over and the current character is equal to the next one
    while i < len(st1) - 1 and st1[i] == st1[i + 1]: i += 1
    # Return the replacement of the string with the compresses substring and call the function on the rest of the string
    return st1.replace((i + 1) * st1[i], st1[i] + str(i + 1))[:len(str(i + 1)) + 1] + (compress(st1[i + 1:]) if i < len(st1) - 1 else "")


# Another option to solve this exercise in a simplified way
# The function gets a string and compress it
def string_compress(str1):
    new_str, counter = "", 1  # declaring a new string to build the compressed string in it
    # Loop all over the characters of the string
    for i in range(0, len(str1)-1):
        # Checks if there is a sequence of more than one character in a row
        if str1[i] == str1[i + 1]:
            counter += 1  # Count the sequence
        else:  # In case that there is no sequence(the character appears one time in a row) or in case the sequence ends
            new_str += str1[i] + str(counter)  # creating the new compressed string
            counter = 1  # In order to initialize the sequence counter
    new_str += str1[i] + str(counter)  # Compress the end of the string
    return new_str


def main():
    str = input("please enter a string: ")
    print(compress(str))


if __name__ == "__main__":
    main()
