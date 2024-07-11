def check_unique_characters(input_str):
    """
    Check if all characters in the input string are unique.
    
    This function uses a dictionary to keep track of character frequencies.
    Time Complexity: O(n), where n is the length of the input string
    Space Complexity: O(k), where k is the number of unique characters (max 256 in ASCII)

    Args:
    input_str (str): The input string to check for unique characters

    Returns:
    bool: True if all characters are unique, False otherwise
    """
    char_frequency = {}
    
    for char in input_str:
        if char in char_frequency:
            return False
        char_frequency[char] = 1
    
    return True


def check_unique_characters_optimization_1(input_str):
    """
    Check if all characters in the input string are unique using sorting.
    
    This function first checks if the string length exceeds 256 (max ASCII chars),
    then sorts the string and checks adjacent characters for duplicates.
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for sorting

    Args:
    input_str (str): The input string to check for unique characters

    Returns:
    bool: True if all characters are unique, False otherwise
    """
    if len(input_str) > 256:
        return False
    
    sorted_str = ''.join(sorted(input_str))
    
    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    
    return True


def check_unique_characters_brute_force(input_str):
    """
    Check if all characters in the input string are unique using brute force.
    
    This function first checks if the string length exceeds 256 (max ASCII chars),
    then compares each character with every other character.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
    input_str (str): The input string to check for unique characters

    Returns:
    bool: True if all characters are unique, False otherwise
    """
    if len(input_str) > 256:
        return False
    
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str)):
            if input_str[i] == input_str[j]:
                return False
    
    return True


def test_check_unique_characters():
    """
    Test function to verify the correctness of the unique character checking functions.
    """
    test_cases = [
        ("", True),
        ("abcdefg", True),
        ("hello", False),
        ("a" * 257, False),
        (''.join(chr(i) for i in range(256)), True),
        ("!@#$%^&*()", True),
        ("1234567890", True),
        ("a b c d", False),
        ("aBcDeF", True)
    ]

    functions_to_test = [
        check_unique_characters,
        check_unique_characters_optimization_1,
        check_unique_characters_brute_force
    ]

    for func in functions_to_test:
        print(f"Testing {func.__name__}")
        for input_str, expected_result in test_cases:
            assert func(input_str) == expected_result, f"Failed for input: {input_str}"
        print(f"All test cases passed for {func.__name__}")

    print("All functions passed all test cases!")

# Run the tests
test_check_unique_characters()