def is_prime(num):
    if num == 2:
        return True
    else:
        for i in (2, num):
            if (num % i == 0):
                return False
            else:
                return True
    
            
def run_is_prime():
    
    num = int(input("Please enter a whole number: "))
    

    if num <= 1:
        print("Invalid argument. Please constrain your query to natural numbers greater than one. Returning to main menu.")
        is_prime_menu()
    else:
        val = is_prime(num)
        if val == True:
            print("This number has no additional factors, it is prime.")
        else:
            print("This number has additional factors. It is not prime.")

def is_prime_menu():
    print("1 - Check if number is prime")
    print("2 - Exit")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        run_is_prime()
        cont = input("Check for another prime? Y to continue, any other key to exit the program.")

        if cont.lower() == "y":
            run_is_prime()
        else:
            exit()
    elif choice == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid selection. Please input either 1 or 2.")
        is_prime_menu()

   