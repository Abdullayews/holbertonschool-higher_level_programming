#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList class."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node.

        Returns:
            int: The node's data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data with validation.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node.

        Returns:
            Node or None: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with validation.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Prints all node values, one per line.

        Returns:
            str: All node data joined by newlines.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node in sorted (increasing) order.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)

        # Case 1: empty list or new value is smallest
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2 & 3: walk the list to find the right spot
        current = self.__head
        while current.next_node is not None:
            if value < current.next_node.data:
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node

        # Case 3: reached the end, attach last
        current.next_node = new_node
