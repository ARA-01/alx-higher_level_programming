#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2 elements
    padded_tuple_a = tuple_a + (0, 0)
    padded_tuple_b = tuple_b + (0, 0)

    # Sum the first elements and the second elements of the padded tuples
    sum_first = padded_tuple_a[0] + padded_tuple_b[0]
    sum_second = padded_tuple_a[1] + padded_tuple_b[1]

    # Return a new tuple containing the sums
    return (sum_first, sum_second)
