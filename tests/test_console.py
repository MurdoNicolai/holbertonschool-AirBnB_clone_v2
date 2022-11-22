#!/usr/bin/python3
""" """
from console import HBNBCommand
import unittest

class test_console(unittest.TestCase):
    """
    testing the console
    """

    def setUp(self):
        """blank test"""
        self.assertEqual(HBNBCommand().cmdloop(), "(hbnb) ")
        pass
