
'''Problem Statement:
Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

Questions:
- Which operator you will use in order to execute this code?'''

# this is a fizz buzz activity with three conditions
# you will loop through the range of 1 to 100 with thefollowing conditional statements:
# 1. if x is divisible by 15 print fizz buzz
# 2. if x is divisible by 5 print fizz
# 3. if x is divisible by 3 print buzz

for x in range(1,101):
    if x % 15 == 0:
        print("Fizz Buzz")
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 == 0:
        print("Buzz")
    else:
        print(x)
        
        