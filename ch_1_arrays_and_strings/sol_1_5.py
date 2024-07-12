def is_one_edit_away(str1, str2):
    """
    Determines if two strings are one edit away from each other using sets.
    An edit can be an insertion, deletion, or substitution of a character.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if the strings are one edit away, False otherwise.
    """
    # Ensure str1 is the shorter or equal length string for simplicity
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    # If the length difference is more than 1, they cannot be one edit away
    if len(str2) - len(str1) > 1:
        return False

    # Convert strings to sets to find the unique characters
    set1 = set(str1)
    set2 = set(str2)
    
    # Calculate the symmetric difference between the sets
    diff = set1.symmetric_difference(set2)
    
    # If the length of the symmetric difference is more than 2, they are not one edit away
    if len(diff) > 2:
        return False
    
    # Check if the position of characters can make them one edit away
    found_difference = False
    i = j = 0
    
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if found_difference:
                return False
            found_difference = True
            
            # If lengths are different, move the longer string pointer
            if len(str1) != len(str2):
                j += 1
                continue
        
        i += 1
        j += 1
    
    return True
    
    
print(is_one_edit_away("pale", "bale"))
# Comprehensive test cases
def run_tests():
    # Test cases where strings are one edit away
    assert is_one_edit_away("pale", "ple") == True  # Deletion
    assert is_one_edit_away("pales", "pale") == True  # Insertion
    assert is_one_edit_away("pale", "bale") == True  # Substitution
    assert is_one_edit_away("pale", "pales") == True  # Insertion
    assert is_one_edit_away("pale", "pate") == True  # Substitution

    # Test cases where strings are not one edit away
    assert is_one_edit_away("pale", "bake") == False  # More than one substitution
    assert is_one_edit_away("pale", "pse") == False  # More than one edit
    assert is_one_edit_away("pale", "palest") == False  # More than one insertion
    assert is_one_edit_away("pale", "pe") == False  # More than one deletion
    assert is_one_edit_away("pale", "ppale") == True  # More than one insertion

    # Edge cases
    assert is_one_edit_away("", "") == True  # No edit needed
    assert is_one_edit_away("a", "") == True  # Single deletion
    assert is_one_edit_away("", "a") == True  # Single insertion
    assert is_one_edit_away("a", "a") == True  # No edit needed

    print("All test cases pass")
    
run_tests()