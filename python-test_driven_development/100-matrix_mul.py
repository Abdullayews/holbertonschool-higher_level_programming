#!/usr/bin/python3
"""Module that defines the matrix_mul function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-integer/float elements, or rows are uneven.
        ValueError: If m_a or m_b is empty, or matrices can't be multiplied.
    """
    # --- Type checks: must be a list ---
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # --- Must be a list of lists ---
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # --- Must not be empty ---
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # --- Must contain only integers or floats ---
    if not all(isinstance(n, (int, float)) for row in m_a for n in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n, (int, float)) for row in m_b for n in row):
        raise TypeError("m_b should contain only integers or floats")

    # --- All rows must be the same size ---
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # --- Matrices must be compatible for multiplication ---
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # --- Actual multiplication ---
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)
    return result
