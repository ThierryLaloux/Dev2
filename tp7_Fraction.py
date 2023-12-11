class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : The denominator cannot be zero (den != 0)
        POST : The fraction is created with a provised numerator and denominator.
            The fraction is build in the simplest form.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = num
        self.den = den
        self._reduce()


    @property
    def numerator(self):
        """Return the numerator of the fraction"""
        return self.num

    @property
    def denominator(self):
        """Return the denominator of the fraction"""
        return self.den

    def _reduce(self):
        """Reduce the fraction to its simplest form."""
        gcd = self._calculate_gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    @staticmethod
    def _calculate_gcd(a, b):
        """Calculate the Greatest Common Divisor (GCD) using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a
    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : A string representation of the reduced fraction is returned
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None
        POST : A string representation of the mixed number is returned.
        """
        integer_part = self.num // self.den
        proper_fraction = Fraction(self.num % self.den, self.den)
        if integer_part == 0:
            return str(proper_fraction)
        elif proper_fraction.is_zero():
            return str(integer_part)
        else:
            return f"{integer_part} + {proper_fraction}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is an instance for fraction
         POST : Returns a new Fraction which give the sum of other and self
         """
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is an instance for fraction
        POST : Returns a new Fraction which give the subtraction of other and self
        """
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is an instance for fraction
        POST : Returns a new Fraction which give the multiplication of other and self
        """
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is an instance for fraction which isn't equal to zero
        POST : Returns a new Fraction which give the division of self by other
        """
        if other.is_zero():
            raise ValueError("A fraction cannot divised by zero")
        new_num = self.num * other.num
        new_den = self.den = other.den
        return Fraction(new_num, new_den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other is an instance for fraction
        POST : Returns a new Fraction which give self raised to the power of other
        """
        new_num = self.num ** other
        new_den = self.den ** other
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is an instance for fraction
        POST : Returns a boolean which give an equal between other and self

        """
        return self.num * other.den == self.den * other.num

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : Return a floating value of fraction
        """
        return self.num / self.den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : Returns a boolean if the value fraction = 0
        """
        return self.num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None
        POST : Returns a boolean if the fraction is integer
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None
        POST : Returns a boolean if the fraction had an absolute value
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : Return a boolean if the fraction is equal 1 in its reduced form
        """
        return self.num == 1 and self.den == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other is an instance of fraction
        POST : Return a boolean if the fractions are adjacent or no
        """
        diff = abs(self.num * other.den - self.den * other.num)
        return diff == 1


