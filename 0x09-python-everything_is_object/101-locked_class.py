#!/usr/bin/python3
class LockedClass:
    """A class that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name."""
    __slots__ = ['first_name']

    def __init__(self):
        """Initializes an instance of LockedClass."""
        pass
