import unittest
from Fraction import Fraction, NulDenominatorException

class TestFraction(unittest.TestCase):

    def test_init(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(0, 2)
        frac3 = Fraction(-9, 4)
        frac4 = Fraction(1, -2)
        frac5 = Fraction(2, 4)
        frac6 = Fraction(-6, -2)
        frac7 = Fraction(3, -12)
        frac8 = Fraction(-1, -6)
        #frac9 = Fraction(1, 0)

        self.assertEqual(frac1.num, 1, "test 1 du numérateur")
        self.assertEqual(frac1.den, 2, "test 1 du denominateur")

        self.assertEqual(frac2.num, 0, "test 2 du numérateur")
        self.assertEqual(frac2.den, 1, "test 2 du denominateur")

        self.assertEqual(frac3.num, -9, "test 3 du numerateur")
        self.assertEqual(frac3.den, 4, "test 3 du denominateur")

        self.assertEqual(frac4.num, -1, "test 4 du numerateur")
        self.assertEqual(frac4.den, 2, "test 4 du denominateur")

        self.assertEqual(frac5.num, 1, "test 5 du numérateur")
        self.assertEqual(frac5.den, 2, "test 5 du denominateur")

        self.assertEqual(frac6.num, 3, "test 6 du numerateur")
        self.assertEqual(frac6.den, 1, "test 6 du denominateur")

        self.assertEqual(frac7.num, -1, "test 7 du numerateur")
        self.assertEqual(frac7.den, 4, "test 7 du denominateur")

        self.assertEqual(frac8.num, 1, "test 8 du numerateur")
        self.assertEqual(frac8.den, 6, "test 8 du denominateur")
        with self.assertRaises(NulDenominatorException):
            Fraction(1, 0)

    def test_str(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(0, 2)
        frac3 = Fraction(-9, 4)
        frac4 = Fraction(1, -2)
        frac5 = Fraction(2, 4)
        frac6 = Fraction(-6, -2)
        frac7 = Fraction(3, -12)
        frac8 = Fraction(-1, -6)

        self.assertEqual(str(frac1), "1/2")
        self.assertEqual(str(frac2),"0/1")
        self.assertEqual(str(frac3),"-9/4")
        self.assertEqual(str(frac4), "-1/2")
        self.assertEqual(str(frac5), "1/2")
        self.assertEqual(str(frac6), "3/1")
        self.assertEqual(str(frac7), "-1/4")
        self.assertEqual(str(frac8), "1/6")

    def test_as_mixed_number(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(4, 2)
        frac3 = Fraction(-1, 2)
        frac4 = Fraction(2, 2)
        frac5 = Fraction(5, 2)
        frac6 = Fraction(-6, 4)
        frac7 = Fraction(-7, 2)
        frac8 = Fraction(-3, -3)
        frac9 = Fraction(5, -5)
        frac10 = Fraction(-8, -2)
        frac11 = Fraction(-1, -8)
        frac12 = Fraction(-3, -2)

        self.assertEqual(frac1.as_mixed_number(), "1/2")
        self.assertEqual(frac2.as_mixed_number(), "2")
        self.assertEqual(frac3.as_mixed_number(), "-1 + 1/2")
        self.assertEqual(frac4.as_mixed_number(), "1")
        self.assertEqual(frac5.as_mixed_number(), "2 + 1/2")
        self.assertEqual(frac6.as_mixed_number(), "-2 + 1/2")
        self.assertEqual(frac7.as_mixed_number(), "-4 + 1/2")
        self.assertEqual(frac8.as_mixed_number(), "1")
        self.assertEqual(frac9.as_mixed_number(), "-1")
        self.assertEqual(frac10.as_mixed_number(), "4")
        self.assertEqual(frac11.as_mixed_number(), "1/8")
        self.assertEqual(frac12.as_mixed_number(), "1 + 1/2")

    def test_add_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        frac3 = Fraction(0, 2)
        frac4 = Fraction(-1, 4)
        frac5 = Fraction(-1, 2)
        frac6 = Fraction(2, 2)
        frac7 = Fraction(-2, 2)

        self.assertEqual(frac1 + frac2, Fraction(3, 4))  # Addition de fractions positive
        self.assertEqual(frac3 + frac2, Fraction(1, 4))  # Addition de fraction nulle et fraction positive
        self.assertEqual(frac1 + frac4, Fraction(1, 4))  # Addition de fraction positive et fraction négatif
        self.assertEqual(frac5 + frac4, Fraction(-3, 4))  # Addition de fractions negative
        self.assertEqual(frac3 + frac4, Fraction(-1, 4))  # Addition de fraction nulle et fraction négative
        self.assertEqual(frac5 + frac2, Fraction(-1, 4))  # Addition de fraction négative et fraction positive
        self.assertEqual(frac3 + frac3, Fraction(0, 1))  # Addition de fractions nulle
        self.assertEqual(frac1 + frac6, Fraction(3, 2))  # Addition de fraction positive avec un entier
        self.assertEqual(frac1 + frac7, Fraction(-1, 2))  # Addition de fraction positive avec un entier negatif

    def test_truediv_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        frac3 = Fraction(-1, 2)
        frac4 = Fraction(-1, 4)
        frac5 = Fraction(4, 2)
        frac6 = Fraction(0, 4)
        frac7 = Fraction(2, 2)

        self.assertEqual(frac1 / frac2, Fraction(2, 1))  # Division de fractions positive
        self.assertEqual(frac3 / frac3, Fraction(1, 1))  # Division de fraction négative identique
        self.assertEqual(frac1 / frac4, Fraction(-2, 1))  # Division de fraction positive par fraction negative
        self.assertEqual(frac1 / frac5, Fraction(1, 4))  # Division de fractions positive par un entier > 1
        self.assertEqual(frac1 / frac7, Fraction(1, 2))  # Division de fractions positive par un entier == 1
        with self.assertRaises(ZeroDivisionError):
            frac1 / frac6

    def test_eq_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 4)
        frac3 = Fraction(1, 2)

        self.assertEqual(frac1 == frac2, False)
        self.assertEqual(frac1 == frac3, True)

    def test_is_integer_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(4, 2)

        self.assertEqual(frac1.is_integer(), False)
        self.assertEqual(frac2.is_integer(), True)

    def test_is_proper_fraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 2)

        self.assertEqual(frac1.is_proper(), True)
        self.assertEqual(frac2.is_proper(), False)

    def test_is_adjacent_to_fraction(self):
        frac1 = Fraction(1, 4)
        frac2 = Fraction(0, 2)
        frac3 = Fraction(4, 2)
        frac4 = Fraction(1, 2)
        frac5 = Fraction(-3, 2)
        frac6 = Fraction(-1, 2)
        frac7 = Fraction(-2, 2)

        self.assertEqual(frac1.is_adjacent_to(frac2), True)
        self.assertEqual(frac1.is_adjacent_to(frac3), False)
        self.assertEqual(frac1.is_adjacent_to(frac4), False)
        self.assertEqual(frac1.is_adjacent_to(frac1), False)
        self.assertEqual(frac1.is_adjacent_to(frac5), False)
        self.assertEqual(frac1.is_adjacent_to(frac6), False)
        self.assertEqual(frac1.is_adjacent_to(frac7), False)

if __name__ == '__main__':
    unittest.main()
