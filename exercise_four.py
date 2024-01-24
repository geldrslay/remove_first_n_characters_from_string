# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Display Message 
print ('Removing certain number of first characters from original string...')

# Defining function 
def remove_characters (original_string,n):
    print ("The original string is", original_string)
    if n < len (original_string): 
        result = original_string [n:]
        return result

# Define original string 
original_string = "programming"

# Remove first seven characters from the original string 
print (remove_characters(original_string,7))

# Remove first ten characters from the original string 
