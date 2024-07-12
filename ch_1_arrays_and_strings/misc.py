from collections import Counter

def check_permutation(str1: str, str2: str) -> bool:
    """
    Check if the longer string contains any permutation of the shorter string.

    Args:
    str1 (str): First input string
    str2 (str): Second input string

    Returns:
    bool: True if the longer string contains a permutation of the shorter string, False otherwise

    Time complexity: O(n), where n is the length of the longer string
    Space complexity: O(k), where k is the number of unique characters in the shorter string
    """
    # Determine which string is shorter
    if len(str1) < len(str2):
        shorter, longer = str1, str2
    else:
        shorter, longer = str2, str1

    # If the shorter string is empty, return True (empty string is a permutation of itself)
    if not shorter:
        return True

    # If the longer string is shorter than the shorter string, return False
    if len(longer) < len(shorter):
        return False

    # Create a Counter for the shorter string
    shorter_counter = Counter(shorter)

    # Create a Counter for the first window in the longer string
    window_counter = Counter(longer[:len(shorter)])

    # Check if the first window is a permutation
    if shorter_counter == window_counter:
        return True

    # Slide the window through the rest of the longer string
    for i in range(len(shorter), len(longer)):
        # Remove the leftmost character from the window
        window_counter[longer[i - len(shorter)]] -= 1
        if window_counter[longer[i - len(shorter)]] == 0:
            del window_counter[longer[i - len(shorter)]]

        # Add the new rightmost character to the window
        window_counter[longer[i]] += 1

        # Check if the current window is a permutation
        if shorter_counter == window_counter:
            return True

    return False

def test_check_permutation():
    # Existing test cases
    assert check_permutation("abc", "cab") == True
    assert check_permutation("ab", "eidbaoo") == True
    assert check_permutation("abc", "def") == False
    assert check_permutation("", "") == True
    assert check_permutation("abc", "") == False
    assert check_permutation("hello", "hello") == True
    assert check_permutation("abc", "abcd") == False
    assert check_permutation("Abc", "cab") == False
    assert check_permutation("aab", "aba") == True
    assert check_permutation("abcde", "bcd") == True
    assert check_permutation("a!b@c#", "#c@b!a") == True
    assert check_permutation("123", "312") == True

    # New test cases for long strings
    # Test case 13: Long string with permutation at the beginning
    assert check_permutation("abcdefghij", "jihgfedcbaabcdefghij") == True

    # Test case 14: Long string with permutation at the end
    assert check_permutation("abcdefghij", "abcdefghijjihgfedcba") == True

    # Test case 15: Long string with permutation in the middle
    assert check_permutation("abcdefghij", "xxxxxjihgfedcbaxxxxx") == True

    # Test case 16: Long string without permutation
    assert check_permutation("abcdefghij", "xxxxxxxxxxxxxxxxxxxxxxxxx") == False

    # Test case 17: Very long strings (1000 characters)
    long_str1 = "a" * 500 + "b" * 500
    long_str2 = "b" * 250 + "a" * 500 + "b" * 250
    assert check_permutation(long_str1, long_str2) == True

    # Test case 18: Very long strings without permutation
    long_str3 = "a" * 1000
    long_str4 = "a" * 999 + "b"
    assert check_permutation(long_str3, long_str4) == False

    # Test case 19: Long string with repeating pattern
    pattern = "abcde" * 200
    shuffled_pattern = "bcdea" * 200
    assert check_permutation(pattern, shuffled_pattern) == True

    print("All test cases passed!")

test_check_permutation()