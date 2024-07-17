def isSubstring(s1, s2):
    """
    Checks if s2 is a substring of s1.

    Args:
    s1 (str): The string to be searched.
    s2 (str): The substring to search for.

    Returns:
    bool: True if s2 is a substring of s1, otherwise False.
    """
    return s2 in s1

def isRotation(s1, s2):
    """
    Checks if s2 is a rotation of s1 using only one call to isSubstring.

    Args:
    s1 (str): The original string.
    s2 (str): The string to check for rotation.

    Returns:
    bool: True if s2 is a rotation of s1, otherwise False.
    """
    # Check if s1 and s2 are of the same length and not empty
    if len(s1) != len(s2) or not s1:
        return False

    # Concatenate s1 with itself and check if s2 is a substring of the result
    concatenated = s1 + s1
    return isSubstring(concatenated, s2)

# Test cases
print(isRotation("waterbottle", "erbottlewat"))  # True
print(isRotation("hello", "llohe"))              # True
print(isRotation("hello", "lloeh"))              # False
print(isRotation("abcd", "dabc"))                # True
print(isRotation("abcd", "cdab"))                # True
print(isRotation("abcd", "abcdabcd"))            # False
print(isRotation("", ""))                        # False (assuming empty strings are not rotations of each other)
