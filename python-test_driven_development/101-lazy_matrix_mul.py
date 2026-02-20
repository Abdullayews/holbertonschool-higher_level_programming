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
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_a == [[]] or m_b == [[]]:
        rows_a = len(m_a)
        cols_a = len(m_a[0]) if m_a else 0
        rows_b = len(m_b)
        cols_b = len(m_b[0]) if m_b else 0
        if m_a == [[]]:
            raise ValueError(
                "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)"
                .format(rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))
        if m_b == [[]]:
            raise ValueError(
                "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)"
                .format(rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))

    return np.matmul(m_a, m_b)
