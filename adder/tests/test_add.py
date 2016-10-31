"""Tests for the add function"""
from unittest import TestCase

import adder

class TestAdd(TestCase):
    """Test the add function"""
    def test_int(self):
        """Test adding integers"""
        result = adder.add(3, 4)
        self.assertEqual(result, 7)

    def test_float(self):
        """Test adding floats"""
        result = adder.add(3.5, 4.5)
        self.assertEqual(result, 8.0)

    def test_string(self):
        """Test adding strings - should append"""
        result = adder.add("toast", "jam")
        self.assertEqual(result, "toastjam")

    def test_mixed(self):
        """Test that mixing types causes a TypeError"""
        with self.assertRaises(TypeError):
            adder.add("toast", 3)

class TestSubtract(TestCase):
    """Test the subtract function"""
    def test_sub(self):
        """Test subtracting integers"""
        result = adder.subtract(4,3)
        self.assertEqual(result, 1)
