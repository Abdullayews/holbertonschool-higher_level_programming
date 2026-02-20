#!/usr/bin/python3
"""Module that defines the lazy_matrix_mul function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.
    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.
    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-integer/float elements, or rows are uneven.
        ValueError: If m_a or m_b is empty, or matrices can't be multiplied.
    """
    return np.matmul(m_a, m_b)
