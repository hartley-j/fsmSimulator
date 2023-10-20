import unittest
from components import *


class TestFlipFlops(unittest.TestCase):

    def setUp(self):
        self.sr_flipflop = FlipFlop(False, False)

    def test_sr_flipflop(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
