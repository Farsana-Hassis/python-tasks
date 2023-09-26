# method to take input without any exceptions
def take_input():
    """
    This function takes the user's inputs and returns them without any exceptions.
    
    Returns:
        entry (int): The valid input
    """
    while True:
        try:
            entry=int(input("Enter a number to check whether it is prime or not:"))
            if entry <= 0:
                print("\n"+str(entry)+" is not a prime number.\nSince negative numbers and zero are not prime numbers.")
                check_again()
            else:
                return entry
        except:
            print("Please enter only natural numbers.\n Try entering again.\n")
        


# method to check whether the input is prime or not    
def is_prime(entry):
    """
    This function checks for primality of an integer entered by the user

    Args:
        entry (int): An integer value

    Returns:
        is_prime (bool): True for prime numbers and False for non-prime numbers
    """
    is_prime=True
    if entry==1:
        is_prime=False
    else:
        for i in range(2,int(entry**0.5+1)):
            if (entry%i== 0):
                is_prime=False
                break        
    return is_prime
            

# method to ask user's choice to repeat the program or not            
def check_again():
    """
    This function asks users' choices to continue with the program or quit

    Returns:
        (bool): Either Ture for continuing or False for quitting
    """
    while True:
        choice=str(input("\nDo you want to check again?\nEnter 'y' for yes and 'n' for no:"))
        if choice=='y' or choice=='Y':
            return True
        elif choice=='n' or choice=='N':
            print("\nThank you!!\n")
            return False
        else:
            print('Invalid Input')
        

# main program
while True:
    entry=take_input()  
    if is_prime(entry):
        print(f"\n{entry} is a prime number.")
    else:
        print(f"\n{entry} is not a prime number.")

    if not check_again():
        break

# The changes are:
# 1)Docstrings and comments has been added.
# 2)Validation error has been dealt.
# 3)A loop has been created so until user decide to leave, the program will be repeated.
# 4)Clear instructions has been added for the user.
