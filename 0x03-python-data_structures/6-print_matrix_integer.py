#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        count = 0
        for val in matrix[row]:
            print("{:d}".format(val), end="")
            if count < len(matrix[row]) - 1:
                print(end=" ")
            count += 1
        print()
