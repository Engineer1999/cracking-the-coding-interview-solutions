def rotate_matrix(matrix):
    n = len(matrix)
    if n==0:
        return False
    if n!=len(matrix[0]):
        return False
    
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[n-j-1][i]
            matrix[n-j-1][i] = temp
    return matrix

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(rotate_matrix(matrix))