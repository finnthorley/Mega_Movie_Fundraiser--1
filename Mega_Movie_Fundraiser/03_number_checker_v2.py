def int_check(question) :

    error = "Please enter a whole number that is more that 12 but less than 130"

    valid = False
    while not valid:
       
        # ask user for number and check it is valid
        try:
            response = int(input(question))
           

            if response <= 0:
              print(error)
            else:
              return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)
              

     