# method for conversions of distances
def distance():
    """
    This function converts the distance from distance to meters according to the sub_choice.

    Args:
        sub_choice (int): choice from main options
    """
    print(
        "Following are available distance conversions.\n___________________________\n 1.Kilometer to meter conversion \n 2.Mile to meter conversion\n 3.Feet to meter conversion"
    )
    sub_choice = int(
        input(
            "Choose an option from above\n(Your choice has to be the numbers corresponding to the options.):"
        )
    )
    quantity = float(input("Enter the distance:"))

    match sub_choice:
        case 1:
            print(str(quantity) + " km is " + str(quantity * 1000) + " m")
        case 2:
            print(str(quantity) + " mile is " + str(quantity * 1609.34) + " m")
        case 3:
            print(str(quantity) + " feet is " + str(quantity * 0.3048) + " m")
        case _:
            print("Invalid input.")


# method for conversions of temperatures
def temperature():
    """
    This function perform different temperature conversions according to the sub_choice.

    Args:
        sub_choice (int): choice from main options
    """
    print(
        "Following are the available temperature conversions.\n____________________________\n 1.Celsius to farenheit \n 2.Farenheit to celsius"
    )
    sub_choice = int(
        input(
            "Choose an option from above\n(Your choice has to be the numbers corresponding to the options.):"
        )
    )

    quantity = float(input("Enter the temperature:"))

    if sub_choice == 1:
        print(
            str(quantity)
            + " celsius is "
            + str((quantity * (9 / 5)) + 32)
            + " farenheit"
        )
    elif sub_choice == 2:
        print(
            str(quantity)
            + " farenheit is "
            + str((quantity - 32) * (5 / 9))
            + " celsius"
        )
    else:
        print("Invalid input.")


# method to ask user's choice to repeat the program or not
def check_again():
    """
    This function asks whether the user wants to run this program again by entering y, yes and n, no.
    """
    while True:
        choice = str(
            input("\nDo you want to check again?\nEnter 'y' for yes and 'n' for no:")
        )
        if choice == "y" or choice == "Y":
            return True
        elif choice == "n" or choice == "N":
            print("\nThank you!!\n")
            return False
        else:
            print("Invalid Input")


# main program
while True:
    print(
        "\nWelcome to unit converter!!\nPlease choose an option from the following choices: \n******************************************************"
    )
    print("1.Distance conversions")
    print("2.Temperature conversions")
    try:
        main_choice = int(input("Choose '1' or '2' as your option:"))

        if main_choice == 1:
            while True:
                try:
                    distance()

                    if not check_again():
                        break
                except ValueError:
                    print("Please enter a valid input!!")

        elif main_choice == 2:
            while True:
                try:
                    temperature()

                    if not check_again():
                        break
                except ValueError:
                    print("Please enter a valid input!!")

        else:
            print("Invalid input!!")
    except ValueError:
        print("Please enter a valid input!!")

    print("Accept yes for the following option to go back to main options.")
    if not check_again():
        break
