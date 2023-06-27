#!/usr/bin/python3
class Square:
    """class Square that defines a square """

    def __init__(self, size=0):
        """Instantiation with size """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
