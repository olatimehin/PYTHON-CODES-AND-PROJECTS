# create a python file called finance_calculators
# import math 
# write a code to request the user to choose between investment and bond.change all input to lower case 
# if the user choose investment.
# write the following code:
# request user input amount,interest rate/100 and number of years
# request user input to choose between simple or compound interest
# print out the answer
# if the user choose bond.
# write the following code:
# request user input present value,interest rate and number of year.
# calculate how much user will repay each month and print the answer 
# if the user choose exit.
# print the program is hereby terminated 

import math

#while True:
    
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
exit       - to quit the program
""")
    selection_choice = input("""Enter either 'investment','bond' or 'exit' from the menu above to proceed : """).lower()

    if selection_choice == 'investment':
        
        principal = float(input("Please enter the amount: "))
        
        rate = float(input("Please enter the interest rate: "))/ 100
        
        time = int(input("Please enter the number of years: "))
    
        
        interest_selection = input("Please choose between 'simple' or 'compound' interest: ")
    
        if interest_selection == "simple":
            A = (principal * (1 + rate * time))
            print(A)
            continue
        
        elif interest_selection == "compound":
            A = (principal * math.pow((1 + rate), time))
            print(A)
            continue
        
        else:

            print("Invalid selection please choose simple or compound interest: ")
            continue
        
    elif selection_choice == "bond":
        
        principal = float(input("Please enter the amount: "))
        
        rate = float(input("Please enter the interest rate: "))/ 100
        
        rate = rate/12
        
        time = int(input("Please enter the number of years: "))
        
        repayment =(rate * principal) / (1 -(1 + rate)**(-time)) 
        
        print(repayment)  
    else:
        selection_choice == "exit"

        print('The program is hereby terminated,Thank you')
        break

while True: