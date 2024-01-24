# Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Defining function 
def remove_characters (original_string,n):
    print ("The original string is", original_string)
    if n < len (original_string): 
        result = original_string [n:]
        return result

