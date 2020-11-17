from math import sqrt

def is_number_perfect_square(number) -> bool:

    if sqrt(number) == int(sqrt(number)):
        return True

    return False


def test_is_number_perfect_square():

    assert(is_number_perfect_square(25) == True)
    assert(is_number_perfect_square(36) == True)
    assert(is_number_perfect_square(81) == True)

    assert(is_number_perfect_square(5) == False)
    assert(is_number_perfect_square(97) == False)
    assert(is_number_perfect_square(32) == False)

test_is_number_perfect_square()
