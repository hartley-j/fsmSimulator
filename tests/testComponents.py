import unittest
from components.FlipFlop import *


class TestFlipFlops(unittest.TestCase):

    def setUp(self):
        self.sr_flipflop = FlipFlop(False, False)
        self.d_flipflop = DFlipFlop(False)

    def test_sr_flipflop(self):

        self.sr_flipflop.set_inputs(_s=True, _r=False)
        self.sr_flipflop.update()
        self.assertEqual(self.sr_flipflop.get_output(), False)

        self.sr_flipflop.set_inputs(_s=True, _r=True)
        self.sr_flipflop.update()
        self.assertEqual(self.sr_flipflop.get_output(), False)

        self.sr_flipflop.set_inputs(_s=False, _r=True)
        self.sr_flipflop.update()
        self.assertEqual(self.sr_flipflop.get_output(), True)

        self.sr_flipflop.set_inputs(_s=False, _r=False)
        with self.assertRaises(ValueError):
            self.sr_flipflop.update()

    def test_d_flipflop(self):

        self.d_flipflop.set_inputs(_d=False)
        self.d_flipflop.update()
        self.assertEqual(self.d_flipflop.get_output(), False)

        self.d_flipflop.set_inputs(_d=True)
        self.d_flipflop.update()
        self.assertEqual(self.d_flipflop.get_output(), True)


if __name__ == '__main__':
    unittest.main()
