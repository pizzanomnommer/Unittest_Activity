# Name: Max Radke   Date: Febuary 25, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Activity unittest, pytest
# Description: Returns the respective number of the fibonacci sequence

def fib(Input):
    # Make sure we got an int
    if not isinstance(Input, int):
            raise TypeError

    # Make sure it is positive
    if Input < 0:
        raise ValueError

    # Setup recursion terminators
    if Input == 0:
        return 0
    
    if Input == 1:
        return 1
    
    # Recurse
    return fib(Input - 1) + fib(Input - 2)

def fact(Input):
    # Make sure we got an int
    if not isinstance(Input, int):
            raise TypeError

    # Make sure it is positive
    if Input < 0:
        raise ValueError

    # Setup recursion terminators
    if Input == 0:
        return 1

    if Input == 1:
        return 1

    # Recurse
    return Input * fact(Input - 1)
