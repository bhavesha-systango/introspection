from fractions import Fraction
def mixed_numeral(vulgar):
    if not (hasattr(vulgar,'numerator') and hasattr(vulgar,'denominator')):
        raise TypeError("{} is not a rational number".format(vulgar))

    integer = vulgar.denominator // vulgar.numerator
    print(integer)
    fraction = Fraction(vulgar.numerator, vulgar.denominator)
    return integer, fraction

print( mixed_numeral(Fraction('11/10')))
