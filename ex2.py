# The main function
def main():
    ls = []  # List of numbers
    st = input("Please enter a number: ")
    # Loop for number inputs
    while st != "Stop":
        if st.isdigit():
            ls.append(int(st))
        else:  # if the input is not a number
            print("The input is not a number!")
        st = input("Please enter a new number: ")


if __name__ == "__main__":
    main()
