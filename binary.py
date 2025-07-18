
# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?

# Pseudocode and steps to answer the question
 
# Define the function BINARY_SEARCH that takes an array (arr) and a (target) value.
# Initialize the low and high pointers to define the search range.
# In a loop, calculate the middle index (mid) and compare it with the target.
# Adjust the low or high pointers based on the comparison to narrow down the search range.
# After exiting the loop, return the index if found or -1 if the target is not present in the array.
# The main program gets inputs from the user, calls the function, and checks if the target is found, displaying appropriate output.


def binary_search(arr, target):
    low = 0           # the first number 
    high = len(arr)-1 # the last number 
    
    while low <= high:
        mid = (low + high) // 2 # calculate 
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1
# Take array input from the user

arr = list(map(int, input("Enter space seperated integers: ").split()))

# ask for index value to search
target = int(input("Enter the value to search: "))

# call binary search function
result = binary_search(arr,target)
#check for validation 
if result != -1:
    print(f"Target value {target} found at index {result}. ")
else:
    print(f"Target value {target} not found in the array.")