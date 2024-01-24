# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Display Message 
print ('Removing certain number of characters from original string...')

# Defining function 
def remove_characters (original_string,n):
    print ("The original string is", original_string)
    if n < len (original_string): 
        result = original_string [n:]
        return result

original_string = "programming"

# Remove first four characters from the original string 

print (remove_characters(original_string, 4))

# Remove first seven characters from the original string 

print (remove_characters(original_string, 7))
