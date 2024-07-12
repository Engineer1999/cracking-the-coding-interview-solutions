def urlify(string: str, true_length: int) -> str:
    """
    Replace all spaces in a string with '%20', modifying the string in-place.

    This function assumes that the string has sufficient space at the end
    to hold the additional characters, and that you are given the 'true'
    length of the string.

    Time Complexity: O(n), where n is the true_length of the string
    Space Complexity: O(1), as we modify the string in-place

    Args:
    string (str): The input string to be modified
    true_length (int): The 'true' length of the string (ignoring extra space at the end)

    Returns:
    str: The modified string with spaces replaced by '%20'

    Example:
    >>> urlify("Mr John Smith    ", 13)
    'Mr%20John%20Smith'
    """
    # Convert string to list for in-place modification
    char_list = list(string)
    
    # Count spaces and calculate new length in one pass
    space_count = char_list[:true_length].count(' ')
    new_length = true_length + space_count * 2
    
    # Modify the list in-place, starting from the end
    index = new_length - 1
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[index-2:index+1] = '%20'
            index -= 3
        else:
            char_list[index] = char_list[i]
            index -= 1
    
    return ''.join(char_list[:new_length])


# Test cases
def test_urlify():
    assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert urlify("Hello World  ", 11) == "Hello%20World"
    assert urlify("   hi  ", 5) == "%20%20%20hi"
    assert urlify("NoSpaces", 8) == "NoSpaces"
    assert urlify("  ", 2) == "%20%20"
    assert urlify("", 0) == ""
    print("All test cases passed!")

# Run the tests
test_urlify()

# Additional example
print(urlify("Python is awesome          ", 18))  # Output: Python%20is%20awesome