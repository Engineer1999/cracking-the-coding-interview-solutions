def string_compress(input_str):
    """
    Compresses the given string using counts of repeated characters.
    
    Args:
    input_str (str): The string to be compressed.

    Returns:
    str: The compressed string or the original string if the compressed version is not shorter.
    """
    # Return an empty string if input is empty
    if not input_str:
        return ""
    
    compressed_list = []
    count = 1
    
    # Iterate through the string up to the second-to-last character
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            count += 1
        else:
            compressed_list.append(input_str[i])
            compressed_list.append(str(count))
            count = 1
    
    # Append the last character and its count
    compressed_list.append(input_str[-1])
    compressed_list.append(str(count))
    
    # Join the list to form the compressed string
    compressed_str = "".join(compressed_list)
    
    # Return the original string if the compressed version is not shorter
    return compressed_str if len(compressed_str) < len(input_str) else input_str

# Comprehensive test cases
def run_tests():
    # Test cases where compression is expected
    assert string_compress("aabcccccaaa") == "a2b1c5a3"  # Expected: "a2b1c5a3"
    assert string_compress("aaaaaa") == "a6"  # Expected: "a6"

    # Test cases where compression is not expected
    assert string_compress("abc") == "abc"  # Expected: "abc" (since compression would not make it shorter)
    assert string_compress("aabbcc") == "aabbcc"  # Expected: "aabbcc" (since compression would not make it shorter)

    # Edge cases
    assert string_compress("a") == "a"  # Expected: "a" (single character)
    assert string_compress("") == ""  # Expected: "" (empty string)
    assert string_compress("aa") == "aa"  # Expected: "aa" (same length as "a2")

    print("All test cases pass")

run_tests()
