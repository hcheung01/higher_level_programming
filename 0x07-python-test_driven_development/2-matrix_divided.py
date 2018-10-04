#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divide elements of matrix by div"""

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not div:
        raise ZeroDivisionError('division by zero')

    new = []
    array = []
    previous = len(matrix[0])
    for row in matrix:
        if len(row) != previous:
            raise TypeError('Each row of the matrix must have the same size')
        if not all(row) and all(matrix[row]) is False:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if isinstance(num, (int, float)) is False:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
            array.append(round(num / div, 2))
        new.append(array)
        array = []
    return new
