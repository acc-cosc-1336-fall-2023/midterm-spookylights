#write functions here, don't add input('') statements here!
def test_config():
    return True

x = 0

def global_x():
    global x
    return x

def use_global():
    global x
    x = 100

def global_change():
    global_x()    
    print_global()
    print("*************************************")
    choice = input("Would you like to change the global variable to 100? Y to change, any other key to exit.")

    if choice.lower() == "y":
        use_global()
        print_global()
    else:
        print_global()
        exit()  

def print_global():
    print("The global variable is", x)
    
