'''Problem Statement:
Write a code in python which will give you a Fibonacci series to a number when you enter it.

Questions:
- How you will you deal when a user inputs ‘0’?
- How the user will deal when a user inputs ‘1’?
- Which loops and statements do you use for the iterations?'''

while True:
    
    n = int(input("Enter the lenght of the Fibonancci Series: "))
    
    a, b = 0, 1
    
    count = 0 
    
    while True:
        
        if n < 0:
            
            print("Enter a positive integer")
            
        elif n == 1:
            
            print("Fibonacci Series upto ", n, ":",a)
            
        else:
            
            print("Fibonacci Sequence: ")
            
        while count < n:
            
            print(a)
            nth = a + b
            a = b
            b = nth
            count += 1
        break
            

# another way to solve the problem
# function to generate fibonacci series

def fibonacci_series():
    # Get user input
    n = int(input("Enter a number for Fibonacci series: "))
    
    # Handle negative numbers
    if n < 0:
        print("Please enter a positive number")
        return
    
    # Handle 0
    if n == 0:
        print("Fibonacci series: []")
        return
    
    # Handle 1
    if n == 1:
        print("Fibonacci series: [0]")
        return
    
    # Initialize first two numbers
    series = [0, 1]
    
    # Generate Fibonacci series
    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    
    print(f"Fibonacci series: {series}")

# Run the function
fibonacci_series()