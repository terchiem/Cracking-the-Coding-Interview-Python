"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""


def zero_matrix(matrix):
    """Returns the input matrix where if an element is 0, its entire row and
    column are set to 0.

    >>> zero_matrix([[1,1,0],[1,1,1],[1,1,1]])
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

    >>> zero_matrix([[1,1,1],[1,0,1],[1,1,1]])
    [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    >>> zero_matrix([[1,1,0],[1,1,1],[0,1,1]])
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    """

    rows = set()
    cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in rows:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    for i in range(len(matrix)):
        for j in cols:
            matrix[i][j] = 0

    return matrix
