def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is more than (or equal to) 1 and less than (or equal to) 200"
        
        try:    
            
            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero and less than 201
            if 1 <= response <= 200 :
                return response  
            

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


# Gets the input from the user
keep_going = ""
while keep_going == "":
    print()
    # ask user for an integer (must be more than / equal to 0)
    var_integer = num_check("Enter an integer: ")
    print()
    print("You selected {}".format(var_integer))
    