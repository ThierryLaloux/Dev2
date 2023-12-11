from Fraction import Fraction

try:
    # Création des fractions
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(1, 4)

    # Affichage des fractions
    print("Fraction 1:", fraction1)
    print("Fraction 2:", fraction2)

    # Opération sur les fractions
    addition = fraction1 + fraction2
    subtraction = fraction1 - fraction2
    multiplication = fraction1 * fraction2
    division = fraction1 / fraction2
    power = fraction1 ** 2

    # Affichage des opération
    print("Addition:", addition)
    print("Soustraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
    print("Puissance:", power)

    # Egalité entre les fractions
    equality = fraction1 == fraction2

    print("Verification egalité:", equality)

    # Conversion en valeur flottante
    float_value = float(fraction1)

    print("Valeur flottante:", float_value)

    # Propriété des fractions
    zero_check = fraction1.is_zero()
    integer_check = fraction1.is_integer()
    proper_check = fraction1.is_proper()
    unit_check = fraction1.is_unit()
    adjacency_check = fraction1.is_adjacent_to(fraction2)

    print("Est Zero:", zero_check)
    print("Est entier:", integer_check)
    print("Est propre:", proper_check)
    print("Est unite:", unit_check)
    print("Est adjacent:", adjacency_check)
except Exception as e:
    print(f"Une erreur a eu lieu: {e}")
