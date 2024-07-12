def is_palindrome_permutation(input_str: str) -> bool:
    """
    Check if a string is a permutation of a palindrome.

    This function determines whether the characters in the input string
    can be rearranged to form a palindrome. It's case-insensitive and
    ignores spaces.

    Time Complexity: O(n), where n is the length of the input string
    Space Complexity: O(k), where k is the number of unique characters in the input

    Args:
    input_str (str): The input string to check

    Returns:
    bool: True if the string is a permutation of a palindrome, False otherwise

    Example:
    >>> is_palindrome_permutation("Tact Coa")
    True  # Because "taco cat" is a valid palindrome
    """
    # Convert to lowercase and create a frequency dictionary
    char_frequency = {}
    odd_count = 0

    for char in input_str.lower():
        # Ignore spaces
        if char != " ":
            # Update character frequency
            char_frequency[char] = char_frequency.get(char, 0) + 1
            
            # Update odd count
            if char_frequency[char] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

    # A palindrome permutation can have at most one character with odd frequency
    return odd_count <= 1
    
# Test cases
def test_is_palindrome_permutation():
    assert is_palindrome_permutation("Tact Coa") == True
    assert is_palindrome_permutation("race a car") == False
    assert is_palindrome_permutation("hello") == False
    assert is_palindrome_permutation("aab") == True
    assert is_palindrome_permutation("carerac") == True
    assert is_palindrome_permutation("") == True
    assert is_palindrome_permutation("a") == True
    assert is_palindrome_permutation("A man a plan a canal Panama") == True
    print("All test cases passed!")

# Run the tests
test_is_palindrome_permutation()

# Additional example
print(is_palindrome_permutation("No lemon, no melon"))  # Output: True