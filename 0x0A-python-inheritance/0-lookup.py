#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of the available attributes of the object."""
    return (dir(obj))
