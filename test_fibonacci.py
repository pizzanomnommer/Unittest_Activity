# Name: Max Radke   Date: Febuary 25, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Activity unittest, pytest
# Description: Tests file "fibonacci.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that fibonacci.py is in the same directory.
#             Type "python ./test_fibonacci.py"

import unittest
import fibonacci

class Testfib(unittest.TestCase):
    # !! Start by testing the .fib function !!

    # Test the first 20 numbers of the fibonacci sequence
    def test1(self):
        fibnumbers = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181]
        result = True
        i = 0
        for x in fibnumbers:
            if fibonacci.fib(i) != x:
                result = False
            i = i + 1

        self.assertTrue(result)

    # Anything other than ints should throw TypeError
    def test2(self):
        with self.assertRaises(TypeError):
            fibonacci.fib("Test")

    # Negative numbers should throw ValueError
    def test3(self):
        with self.assertRaises(ValueError):
            fibonacci.fib(-1)

    # Floats should through type error
    def test4(self):
        with self.assertRaises(TypeError):
            fibonacci.fib(0.5)

    # !! End by testing the .fact function !!

    # Test the first 10 factorial numbers
    def test5(self):
        factnumbers = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
        result = True
        i = 0
        for x in factnumbers:
            if fibonacci.fact(i) != x:
                result = False
            i = i + 1
        
        self.assertTrue(result)

    # Anything other than ints should throw TypeError
    def test6(self):
        with self.assertRaises(TypeError):
            fibonacci.fact("Test")

    # Negative numbers should through ValueError
    def test7(self):
        with self.assertRaises(ValueError):
            fibonacci.fact(-1)

    # Floats should throw type error
    def test8(self):
        with self.assertRaises(TypeError):
            fibonacci.fact(0.5)

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)

