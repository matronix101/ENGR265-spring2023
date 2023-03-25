import unittest
import chuck_a_luck

class TestPayout(unittest.TestCase):

    def test_calculate_payout_single_no_match(self):
        """ test_calculate_payout_single_no_match."""
        dice = [1, 2, 3]

        actual = chuck_a_luck.calculate_payout(dice, chuck_a_luck.SINGLE, 4, 100.0)
        expected = -100.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice, chuck_a_luck.SINGLE, 5, 200.0)
        expected = -200.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice, chuck_a_luck.SINGLE, 6, 300.0)
        expected = -300.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice, chuck_a_luck.SINGLE, 6, 0.0)
        expected = 0.0
        self.assertAlmostEqual(expected, actual, 4)

    def test_calculate_payout_single_one_match(self):
        dice1 = [4, 5, 6] #  We'll try each of 4,5,6 as a single
        dice2 = [1, 1, 2] #  Confirm duplicates don't cause errors

        actual = chuck_a_luck.calculate_payout(dice1, chuck_a_luck.SINGLE, 4, 100.0)
        expected = 100.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice1, chuck_a_luck.SINGLE, 5, 200.0)
        expected = 200.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice1, chuck_a_luck.SINGLE, 6, 300.0)
        expected = 300.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice1, chuck_a_luck.SINGLE, 6, 0.0)
        expected = 0.0
        self.assertAlmostEqual(expected, actual, 4)

        actual = chuck_a_luck.calculate_payout(dice2, chuck_a_luck.SINGLE, 2, 300.0)
        expected = 300.0
        self.assertAlmostEqual(expected, actual, 4)


if __name__ == '__main__':
    unittest.main()

