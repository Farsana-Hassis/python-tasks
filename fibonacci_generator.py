
# method to take input without any exception
def take_input():
    """
    Takes the user's choice of input and returns it by avoiding exceptions.

    Returns:
        limit (int): User input
    """
    while True:
        try:
            limit = int(input("Enter the n:"))
            if limit <= 0:
                print("You cannot enter a negative number or zero as limit.Please enter a natural number as limit.")
            elif limit > 20578:
                # since list is used for generating the fibonacci series and to avoid overflow error
                print("Please enter a lesser natural number than your current input.")
            else:
                return limit
        except ValueError:
            print("Please enter a natural number as limit without any decimal value.")


# method to display fibonacci series for given limit
def fibonacci(limit):
    """
    Find the fibonacci series and return it as a list

    Args:
        limit (int): An integer value

    Returns:
        fibonacci (list) : A list containing all values in Fibonacci Series upto 'n'
    """
    first_number = 0
    next_number = 1
    fibonacci = []
    if limit == 1:
        fibonacci = [first_number]
    elif limit == 2:
        fibonacci = [first_number, next_number]
    else:
        fibonacci = [first_number]
    for i in range(2, limit+1):
        try:
            after_next = first_number+next_number
            fibonacci.append(next_number)
            first_number = next_number
            next_number = after_next
        except OverflowError:
            print("Some mathematical error occured.Can you try entering a bit more smaller number.")
    return fibonacci


# method for asking the user to whether repeat or not
def display_again():
    """
    Ask users wheter they want to do it again or exit.

    Returns:
        (bool): True for continuing and False for exiting.
    """
    while True:
        choice = str(input("Do you want to try again?\nEnter 'y' for yes and 'n' for no:"))
        if choice == 'y' or choice == 'Y':
            return True
        elif choice == 'n' or choice == 'N':
            return False
        else:
            print("Invalid input")


# main program
while True:
    print('''Choose an option from below:
           a)Display n number of fibonacci series.
           b)Display the fibonacci series in nth position.''')
    decision = input("Choose 'a' or 'b':")

    match decision.lower():
        case 'a':
            limit = take_input()
            print(f"The fibonacci series for limit {limit} is:\n {fibonacci(limit)}")
        case 'b':
            limit = take_input()
            fibonacci_list = fibonacci(limit)
            print(f"The number in {limit}th position of fibonacci series is:\n{fibonacci_list[limit-1]}")
        case _:
            print("Invalid input.")

    if not display_again():
        print("Thank you!!")
        break

