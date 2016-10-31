from unittest import TestCase

import adder

class TestAdd(TestCase):
    def test_int(self):
        r = adder.add(3,4)
        self.assertEqual(r, 7)

    def test_float(self):
        r = adder.add(3.5, 4.5)
        self.assertEqual(r, 8.0)

    def test_string(self):
        r = adder.add("toast", "jam")
        self.assertEqual(r, "toastjam")

    def test_mixed(self):
        with self.assertRaises(TypeError):
            adder.add("toast", 3)
