def rotate_matrix(matrix):
    """
    Rotates the given N x N matrix 90 degrees clockwise.

    Args:
    matrix (list of list of int): A 2D list representing the matrix to be rotated.

    Returns:
    list of list of int: The rotated matrix if the input is valid, otherwise returns False.
    """
    n = len(matrix)
    
    # Check if the matrix is empty or not a square matrix
    if n == 0 or n != len(matrix[0]):
        return False
    
    # Perform the rotation in layers
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            temp = matrix[i][j]
            # Move left element to top
            matrix[i][j] = matrix[n - j - 1][i]
            # Move bottom element to left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            # Move right element to bottom
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            # Assign temp to right
            matrix[j][n - i - 1] = temp
    
    return matrix

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Test case 1
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Original matrix 1:")
print_matrix(matrix1)
print("\nRotated matrix 1:")
rotated_matrix1 = rotate_matrix(matrix1)
if rotated_matrix1:
    print_matrix(rotated_matrix1)
else:
    print("Invalid matrix")
print()

# Test case 2: Non-square matrix
matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Original matrix 2:")
print_matrix(matrix2)
print("\nRotated matrix 2:")
rotated_matrix2 = rotate_matrix(matrix2)
if rotated_matrix2:
    print_matrix(rotated_matrix2)
else:
    print("Invalid matrix")
print()

# Test case 3: Empty matrix
matrix3 = []
print("Original matrix 3: (Empty matrix)")
print(matrix3)
print("\nRotated matrix 3:")
rotated_matrix3 = rotate_matrix(matrix3)
if rotated_matrix3:
    print_matrix(rotated_matrix3)
else:
    print("Invalid matrix")
print()

# Test case 4: Single element matrix
matrix4 = [[1]]
print("Original matrix 4:")
print_matrix(matrix4)
print("\nRotated matrix 4:")
rotated_matrix4 = rotate_matrix(matrix4)
if rotated_matrix4:
    print_matrix(rotated_matrix4)
else:
    print("Invalid matrix")
print()
