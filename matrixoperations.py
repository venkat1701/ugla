# -*- coding: utf-8 -*-
"""matrixoperations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y2pkwRDU-e65DFQSzP8LENor1lKrSusP
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition
addition = A + B
print("Addition:\n", addition)

# Subtraction
subtraction = A - B
print("Subtraction:\n", subtraction)

# Multiplication (element-wise)
elementwise_multiplication = A * B
print("Element-wise Multiplication:\n", elementwise_multiplication)

# Matrix Multiplication (dot product)
matrix_multiplication = np.dot(A, B)
print("Matrix Multiplication:\n", matrix_multiplication)
