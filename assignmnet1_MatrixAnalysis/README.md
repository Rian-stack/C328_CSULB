Matrix Analysis

Authors
- Rafael Papa
- Rianne Papa
- Bailey Kwok

Overview

The isValidGrid function checks whether a given square matrix (grid) meets the criteria of having unique elements in each row, column, and quadrant. This functionality is commonly used in validating Sudoku puzzles or similar grid-based structures.
Function Definition

python

def isValidGrid(matrix):

Parameters

    matrix (list of list of int): A square matrix where each inner list represents a row. The function assumes the matrix is non-empty and is of equal width and height.

Returns

    bool: Returns True if the grid is valid (i.e., all rows, columns, and quadrants contain unique elements). Returns False otherwise.

Functionality

    Row Validation: The function iterates through each row of the matrix and checks for duplicate elements. If duplicates are found, it returns False.

    Column Validation: The function constructs each column and checks for duplicates in the same manner. If duplicates are detected, it returns False.

    Quadrant Validation: The matrix is divided into four quadrants (top-left, top-right, bottom-left, bottom-right). The function checks each quadrant for duplicates. If any quadrant contains duplicates, it returns False.

    If all checks pass, the function returns True, indicating the matrix is valid.

Example Usage

To use the isValidGrid function from the command line, follow these steps:

    Open a terminal or command prompt.

    Start the Python console:

    bash

python  # or python3, depending on your installation

Import the function and test it:

python

    >>> from cecs328pa1 import *
    >>> isValidGrid([[1, 2], [3, 4]])
    True

Additional Examples

python

>>> isValidGrid([[5, 3, 4, 6], [6, 7, 2, 1], [1, 9, 8, 3], [8, 5, 9, 7]])
True
>>> isValidGrid([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
False  # Duplicate in rows
>>> isValidGrid([[1, 2], [2, 1]])
False  # Duplicate in columns

Dependencies

    Python 3.x

Acknowledgments

This function can be useful for anyone working with grid-based puzzles, providing a straightforward method for validating the uniqueness of elements in rows, columns, and quadrants.
