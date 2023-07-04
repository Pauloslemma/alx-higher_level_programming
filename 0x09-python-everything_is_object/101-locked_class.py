#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    To stop user from instantiating new LockedClass attributes
    for anything and the attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
