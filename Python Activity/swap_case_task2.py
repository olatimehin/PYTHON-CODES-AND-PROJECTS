'''Problem Statement:
How to swap all uppercase characters to lowercase and vice versa?

Questions:
- How the user will enter the character?
- How it will swap?
- Which commands will be used to convert each other?'''

# FIRST METHOD

# User input
# Swapping the case of characters using swapcase()
# Output the swapped string
user_input = input("Enter a string: ")


swapped_string = user_input.swapcase()


print("Swapped case string:", swapped_string)


# SECOND METHOD
# User input
# Initialize an empty string to store the result
# Iterate through each character in the input string
# Convert uppercase to lowercase
# Convert lowercase to uppercase
# Keep non-alphabetic characters as they are
# Output the swapped string

user_input = input("Enter a string: ")


swapped_string = ""


for char in user_input:
    
    if char.isupper():
        
        swapped_string += char.lower()
        
    elif char.islower():
       
        swapped_string += char.upper()
    else:
        
        swapped_string += char


print("Swapped case string:", swapped_string)


# THIRD METHOD 

def swap_case(swap):
    
    string = " "
    for char in swap:
        
        if char.islower():
            
            string += char.upper()
            
        else:
            
            string += char.lower()
            
    return string