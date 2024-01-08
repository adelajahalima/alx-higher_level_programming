#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for t in range(len(matrix)):
        for h in range(len(matrix[t])):
            print("{:d}".format(matrix[t][h]), end="")
            if h != (len(matrix[t]) - 1):
                print(" ", end="")

        print("")
