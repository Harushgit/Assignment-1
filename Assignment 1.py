def unique_char(s):
    # create an empty dictionary to store character counts
    char_count ={}

    #to count string occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    #checking character with only one occurrence
    for char in s:
        if char_count[char] == 1:
            return char

    # If no unique character found, return None
    return None

# Test the function with the example input
input_string = "swiss"
result = unique_char(input_string)
print("The first non-repeating character is:", result)


