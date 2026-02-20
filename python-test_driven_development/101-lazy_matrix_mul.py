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

    for row in m_a:
        if isinstance(row, list):
            if not all(isinstance(n, (int, float)) for n in row):
                raise TypeError("invalid data type for einsum")

    for row in m_b:
        if isinstance(row, list):
            if not all(isinstance(n, (int, float)) for n in row):
                raise TypeError("invalid data type for einsum")

    if len(set(len(row) for row in m_a if isinstance(row, list))) > 1:
        raise ValueError("setting an array element with a sequence.")

    if len(set(len(row) for row in m_b if isinstance(row, list))) > 1:
        raise ValueError("setting an array element with a sequence.")

    rows_a = len(m_a)
    cols_a = len(m_a[0]) if m_a and isinstance(m_a[0], list) else 0
    rows_b = len(m_b)
    cols_b = len(m_b[0]) if m_b and isinstance(m_b[0], list) else 0

    if m_a == [[]] or m_b == [[]]:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: "
            "{} (dim 1) != {} (dim 0)".format(
                rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))

    if cols_a != rows_b:
        raise ValueError(
            "shapes ({},{}) and ({},{}) not aligned: "
            "{} (dim 1) != {} (dim 0)".format(
                rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))

    return np.matmul(m_a, m_b)
