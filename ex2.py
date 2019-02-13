# The function gets a list and sum all of its nodes
def sumlist(ls):
    sum = 0
    for i in range(len(ls)):  # Loop for summing numbers in the list
        sum += ls[i]
    print(sum)


# The main function build a list of numbers
def main():
    ls = []  # List of numbers
    st = input("Please enter a number: ")
    # Loop for number inputs until the input is equal to stop
    while st != "stop":
        if st.isdigit():  # checks if the input is a number
            ls.append(int(st))
        else:  # if the input is not a number
            print("The input is not a number!")
        st = input("Please enter a new number: ")
    sumlist(ls)  # Call to function


if __name__ == "__main__":
    main()
