import math


def sieve(number):  # taking a number as input and we'll find all prime values below it
    primes = [0] * number
    primes[0] = primes[1] = 1  # initialise 0 and 1 to not prime numbers
    for prime in range(2, int(math.sqrt(len(primes)))):
        if primes[prime] == 0:
            for y in range(prime * 2, len(primes), prime):
                primes[y] = 1
        else:
            pass

    return primes


while True:  # take input and reject any non integer inputs
    try:
        num = int(input("Type in a number: "))
        break

    except ValueError:
        print("Type in an integer!")

nums = sieve(num)

for num in range(len(nums)):
    if nums[num] == 0:
        print(num)
    else:
        pass
