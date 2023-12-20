import unittest
from tp9_Fraction import Fraction, NulDenominatorException

class TestFraction(unittest.TestCase):

    def test_init(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 4)
        self.assertEqual(frac1.num, 1, "test du numérateur")
        self.assertEqual(frac1.den, 2, "test du denominateur")
        frac2._reduce()
        self.assertEqual(frac2.num, 1, "test du numérateur avec reduce")
        self.assertEqual(frac2.den, 2, "test du denominateur avec reduce")
        with self.assertRaises(NulDenominatorException):
            Fraction(1, 0)

    def test_str(self):
        frac1 = Fraction(1, 2)
        self.assertEqual(frac1.__str__(), f"{frac1.num}/{frac1.den}")

    def test_as_mixed_number(self):
        frac1 = Fraction(1, 2)
        integer_part = frac1.num // frac1.den
        proper_fraction = Fraction(frac1.num % frac1.den, frac1.den)
        if integer_part == 0:
            self.assertEqual(frac1.as_mixed_number(),f"{proper_fraction}")
        if proper_fraction.is_zero():
            self.assertEqual(frac1.as_mixed_number(), f"{integer_part}")

    def test_add_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        self.assertEqual(frac1.__add__(frac2), Fraction(3, 4))

    def test_truediv_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        self.assertEqual(frac1.__truediv__(frac2), Fraction(1, 8))
        with self.assertRaises(ZeroDivisionError):
            frac1.__truediv__(Fraction(0, 1))

    def test_eq_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        self.assertEqual(frac1.__eq__(frac2), False)

    def test_is_integer_fraction(self):
        frac1 = Fraction(1, 2)
        self.assertEqual(frac1.is_integer(), False)

    def test_is_proper_fraction(self):
        frac1 = Fraction(1, 2)
        self.assertEqual(frac1.is_proper(), True)

    def test_is_adjacent_to_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        self.assertEqual(frac1.is_adjacent_to(frac2), False)

if __name__ == '__main__':
    unittest.main()
