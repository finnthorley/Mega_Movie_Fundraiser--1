#import statements 


#functions go here

# checks the ticket name is not blank
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    # If name is not blank, program continues 
    if response != "":
      return response 
    
    # If name is blank, show error (& repeat loop)
    else:
      print("Sorry - this can't be blank, "
          "please enter your name")


#********** Main Routine **********

# Set up dictionaries / lists need to hold data

# Ask user if they have used the program before & show inscructions if necessary

# Loop to get ticket details 

    # Get name (can't be blank)
    name = not_blank("Name: ")
    
    # Get age (between 12 and 130)
    
    # Calculate ticket price
    
    # Loop to ask for snacks
    
    # Calculate snack price

    #ask for payement method (and apply surcharge if nessecary)

# Calculate total sales and profit

# Output data to text file 