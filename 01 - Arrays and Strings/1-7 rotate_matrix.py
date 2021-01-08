"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""


def rotate_matrix(matrix):
    """Returns the input matrix with its elements rotated by 90 degrees.

    # >>> rotate_matrix([[1]])
    # [[1]]

    # >>> rotate_matrix([[1,2],[3,4]])
    # [[3, 1], [4, 2]]

    # >>> rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    >>> rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    """
    n = len(matrix)
    max_levels = len(matrix) // 2

    for level in range(max_levels):
        # Iterate through each element on the current level
        # and rotate by 90 degrees.
        end_index = n-level-1
        for i in range(level, end_index):
            offset = i - level
            top_val = matrix[level][i]

            # Left to Top
            matrix[level][i] = matrix[end_index-offset][level]
            # Bottom to Left
            matrix[end_index-offset][level] = matrix[end_index][end_index-offset]
            # Right to Bottom
            matrix[end_index][end_index-offset] = matrix[i][end_index]
            # Top to Right
            matrix[i][end_index] = top_val

    return matrix
