def check_permutation(str_1: str, str_2: str) -> bool:
    """
    Check if one string is a permutation of the other.

    A permutation means that both strings contain the same characters,
    but possibly in a different order.

    Time Complexity: O(n log n), where n is the length of the strings
    (due to sorting)
    Space Complexity: O(n) for the sorted strings

    Args:
    str_1 (str): The first string to compare
    str_2 (str): The second string to compare

    Returns:
    bool: True if str_1 is a permutation of str_2, False otherwise
    """
    
    # First, check if the lengths are equal
    # If not, they can't be permutations of each other
    if len(str_1) != len(str_2):
        return False
    
    # Sort both strings and compare
    # If they are permutations, the sorted strings will be identical
    if sorted(str_1) == sorted(str_2):
        return True
    
    # If we've reached here, the strings are not permutations
    return False


# Example usage
print(check_permutation("abc", "bca"))  # Should print True
print(check_permutation("abc", ""))     # Should print False
print(check_permutation("hello", "olleh"))  # Should print True
print(check_permutation("python", "typhon"))  # Should print True
print(check_permutation("coding", "decoding"))  # Should print False