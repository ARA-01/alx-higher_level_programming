#!/usr/bin/python3
"""THis defines a locked class."""


class LockedClass:
    """
    Prevents the user from instantiating the new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
