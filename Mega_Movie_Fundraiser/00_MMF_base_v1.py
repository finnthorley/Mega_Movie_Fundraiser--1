#import statements 


#functions go here
#Checks for an integer between two values

def int_check(question, low_num, high_num) :

  error = "Please enter a whole number between {} " \
          "and {}".format(low_num, high_num)
  
  valid = False
  while not valid:

      # ask user for number and check if it is valid
      try:
          response = int(input(question))
          

          if low_num <= response <= high_num:
              return response
          else:
              print(error)

      #if an integer is not entered, display an error
      except ValueError:
          print(error)

# main routine goes here 
age = int_check("Age: ", 12, 130)

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

# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user that only one seat is left
    else: 
        print("*** There is only one seat left! ***")

    # Get details...
    name = not_blank("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))

    # Get name (can't be blank)
    name = not_blank("Name: ")
    
    # Get age (between 12 and 130)
    
    # Calculate ticket price
    
    # Loop to ask for snacks
    
    # Calculate snack price

    #ask for payement method (and apply surcharge if nessecary)

# Calculate total sales and profit

# Output data to text file 