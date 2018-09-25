# wersja 1 - bez sensu, bo None
import unittest

from _27testing import eat, nap

class _testingTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(
            eat('broccoli', is_healthy=True),
            'Im eating it cause my body'
        )
        self.assertEqual(
            eat('pizza', is_healthy=False),
            'Im eating piza cause YOLO'
        )
if __name__ == "__main__":
    unittest.main()


import unittest
#
from _27testing import eat, nap, laugh, is_funny
#
class _27testingTests(unittest.TestCase):
    def test_eat_is_healthy(self):
        self.assertEqual(
            eat('broccoli', is_healthy=True),
            'Im eating broccoli, cause my body'
        )
    def test_eat_isunhealthy(self):
        self.assertEqual(
            eat('pizza', is_healthy=False),
            'Im eating pizza, because YOLO!'
        )
    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "Im feeling refreshed after 1hr"
        )
    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "I overslept 3hrs"
        )
    def test_ishealthy_is_boolean(self):
        with self.assertRaises(ValueError):
            """is_healthy must be boolean"""
            eat('pizza', is_healthy="who cares?"),
            raise AssertionError
    def test_laugh(self):
        self.assertIn(laugh(),('lol','haha','hehe'))
    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("gabi"),"gabi should be funny")
        self.assertTrue(is_funny("srabi"),"srabi should be funny")
    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"),False)
#self.assertFalse(is_funny=("tim"),"tim should be funny"
if __name__ == "__main__":
    unittest.main()


