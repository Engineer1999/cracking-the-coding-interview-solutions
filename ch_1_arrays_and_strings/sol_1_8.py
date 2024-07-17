def zeroMatrix(matrix):
    """
    This function takes a matrix as input and modifies it such that if an element is 0, 
    its entire row and column are set to 0. This is achieved using an auxiliary list to 
    store the coordinates of the zero elements.

    Time Complexity: O(M*N), where M is the number of rows and N is the number of columns.
    Space Complexity: O(K), where K is the number of zero elements in the matrix.
    """
    coordinate_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                coordinate_list.append((i, j))
    
    for i, j in coordinate_list:
        matrix[i] = [0] * len(matrix[0])
        for k in range(len(matrix)):
            matrix[k][j] = 0
                
    return matrix

def zeroMatrix_optimized(matrix):
    """
    This function takes a matrix as input and modifies it such that if an element is 0, 
    its entire row and column are set to 0. This optimized version uses the first row 
    and first column to store the information about rows and columns to be zeroed out, 
    reducing space complexity.

    Time Complexity: O(M*N), where M is the number of rows and N is the number of columns.
    Space Complexity: O(1), since we use the input matrix itself for storage.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    first_row_has_zero = False
    first_col_has_zero = False
    
    # Check if first row has a zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break
            
    # Check if first column has a zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
    
    # Use first row and column to mark zeros
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Zero out rows based on the markers in the first column
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(cols):
                matrix[i][j] = 0
    
    # Zero out columns based on the markers in the first row
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(rows):
                matrix[i][j] = 0
    
    # Zero out the first row if needed
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Zero out the first column if needed
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0
    
    return matrix

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Test case 1
matrix1 = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]
print("Original matrix 1:")
print_matrix(matrix1)
print("\nZeroed matrix (optimized) 1:")
ans1 = zeroMatrix_optimized(matrix1)
print_matrix(ans1)
print()

# Test case 2
matrix2 = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix 2:")
print_matrix(matrix2)
print("\nZeroed matrix (optimized) 2:")
ans2 = zeroMatrix_optimized(matrix2)
print_matrix(ans2)
print()

# Test case 3
matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix 3:")
print_matrix(matrix3)
print("\nZeroed matrix (optimized) 3:")
ans3 = zeroMatrix_optimized(matrix3)
print_matrix(ans3)
