def is_prime(number) -> bool:

    if number == 1:
        return False

    for iterator in range(2, number, 1):
        if number % iterator == 0:
            return False

    return True


def test_is_prime():

  assert(is_prime(2) == True)
  assert(is_prime(3) == True)
  assert(is_prime(13) == True)
  assert(is_prime(59) == True)

  assert(is_prime(96) == False)
  assert(is_prime(124) == False)
  assert(is_prime(1) == False)


test_is_prime()
